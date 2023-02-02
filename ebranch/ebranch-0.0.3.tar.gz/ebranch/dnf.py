#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) Meta Platforms, Inc. and affiliates.
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

import functools
import io
import json
import os
import subprocess
import sys
from collections import namedtuple

RepoConfig = namedtuple(
    "RepoConfig", ["name", "relver", "disable_repos", "enable_repos"]
)

REPOS = {
    "epel8": RepoConfig("centos-stream-legacy", "8", ["epel-next"], []),
    "epel9": RepoConfig("centos-stream", "9", ["epel-next"], []),
    "rawhide": RepoConfig("fedora", "rawhide", [], []),
}

SRC_REPOS = {
    "rawhide": RepoConfig("fedora", "rawhide", ["*"], ["fedora-source"]),
}

UNKNOWN = "UNKNOWN"


@functools.lru_cache(maxsize=4096)
def build_req_available_p(req: str, branch: str) -> bool:
    """
    Check to see if the build requirement for a package is available
    """
    repo_config = REPOS[branch]
    cmd = [
        "rpmdistro-repoquery",
        repo_config.name,
        repo_config.relver,
    ]
    if repo_config.disable_repos:
        cmd.append(f"--disablerepo={','.join(repo_config.disable_repos)}")
    if repo_config.enable_repos:
        cmd.append(f"--enablerepo={','.join(repo_config.enable_repos)}")
    cmd += ["--whatprovides", req]
    r = subprocess.run(
        cmd,
        capture_output=True,
        check=True,
    )

    # if there's no match, stdout is empty
    return bool(r.stdout)


def dedup_build_reqs(reqs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    De-duplicate build requirements
    """
    res = {}
    for src, buildreq in reqs:
        res.setdefault(src, []).append(buildreq)
    return res


def filter_build_reqs(reqs: list[str], branch: str) -> list[str]:
    """
    Filter build requirements
    """
    return [
        (get_srpm_providing(req), req)
        for req in reqs
        if not build_req_available_p(req, branch)
    ]


@functools.lru_cache(maxsize=4096)
def get_pkg_build_reqs(pkg: str, ref_branch: str = "rawhide") -> list[str]:
    """
    Get the packages required to build a package
    """
    repo_config = SRC_REPOS[ref_branch]
    cmd = [
        "rpmdistro-repoquery",
        repo_config.name,
        repo_config.relver,
    ]
    if repo_config.disable_repos:
        cmd.append(f"--disablerepo={','.join(repo_config.disable_repos)}")
    if repo_config.enable_repos:
        cmd.append(f"--enablerepo={','.join(repo_config.enable_repos)}")
    cmd += ["--requires", pkg]
    r = subprocess.run(
        cmd,
        capture_output=True,
        check=True,
    )
    return r.stdout.decode().splitlines()


def get_pkg_missing_build_reqs(
    pkg: str,
    branch: str,
    ref_branch: str = "rawhide",
) -> list[str]:
    """
    Get the missing build requirements for a package
    """
    reqs = get_pkg_build_reqs(pkg, ref_branch)
    return filter_build_reqs(reqs, branch)


@functools.lru_cache(maxsize=4096)
def get_srpm_providing(req: str, ref_branch: str = "rawhide") -> str:
    """
    Get the source rpm providing a requirement
    """
    repo_config = REPOS[ref_branch]
    cmd = [
        "rpmdistro-repoquery",
        repo_config.name,
        repo_config.relver,
    ]
    if repo_config.disable_repos:
        cmd.append(f"--disablerepo={','.join(repo_config.disable_repos)}")
    if repo_config.enable_repos:
        cmd.append(f"--enablerepo={','.join(repo_config.enable_repos)}")
    cmd += [
        "--qf",
        "%{source_name}",
        "--whatprovides",
        req,
    ]
    r = subprocess.run(
        cmd,
        capture_output=True,
        check=True,
    )
    res = r.stdout.decode().splitlines()
    if len(res) != 1:
        print(f"Error determining SRPM providing {req}: {res}", file=sys.stderr)
        return UNKNOWN
    return res[0]


def report_missing_build_reqs(
    pkg: str,
    branch: str,
    ref_branch: str = "rawhide",
) -> dict[str, dict]:
    """
    Outputs a dictionary containing a mapping of src.rpm to the dependencies
    """
    res = get_pkg_missing_build_reqs(pkg, branch, ref_branch)
    dedup_reqs = dedup_build_reqs(res)
    return {pkg: {"build": dedup_reqs}}


def unfold_report(report: dict[str, dict]) -> dict[str, dict]:
    """
    Adds new missing BRs to the top-level list
    """
    expanded_report = {}
    for pkg in report:
        pkg_data = report[pkg]
        expanded_report[pkg] = pkg_data
        if pkg_data.get("skip", False):
            # package marked as not to be processed
            continue
        buildreqs = pkg_data.get("build", {})
        for buildreq in buildreqs:
            if buildreq == UNKNOWN:
                # unknown package
                continue
            if buildreq in report:
                continue
            expanded_report[buildreq] = {}
    return expanded_report


def unfold_report_serialized(report_file: str):
    """
    Adds new missing BRs and save to the report file
    """
    report = load_report(report_file)
    expanded_report = unfold_report(report)
    save_report(expanded_report, report_file)
    return expanded_report


def iterate_report(
    report: dict[str, dict],
    branch: str,
    ref_branch: str = "rawhide",
) -> dict[str, dict]:
    """
    Computes missing BRs for new top-level packages
    """
    expanded_report = {}
    for pkg in report:
        pkg_data = report[pkg]
        expanded_report[pkg] = pkg_data
        if pkg_data.get("skip", False):
            # package marked as not to be processed
            continue
        if "build" not in pkg_data:
            pkg_report = report_missing_build_reqs(pkg, branch, ref_branch)
            new_pkg_data = pkg_report[pkg]
            expanded_report[pkg] = {**pkg_data, **new_pkg_data}
    return expanded_report


def iterate_report_serialized(
    report_file: str,
    branch: str,
    ref_branch: str = "rawhide",
) -> dict[str, dict]:
    """
    Computes missing BRs for new top-level packages and save to the report file
    """
    existing_report = load_report(report_file)
    expanded_report = iterate_report(existing_report, branch, ref_branch)
    if existing_report == expanded_report:
        print("Report unchanged", file=sys.stderr)
    elif len(existing_report) > len(expanded_report):
        print(
            "ERROR: new report is shorter, cowardly refusing to save it",
            file=sys.stderr,
        )
    else:
        save_report(expanded_report, report_file)
    return expanded_report


def load_report(report_file: str) -> dict[str, dict]:
    if not os.path.exists(report_file):
        return {}
    try:
        with io.open(report_file, "r", encoding="utf-8") as fp:
            try:
                report = json.load(fp)
            except json.decoder.JSONDecodeError:
                report = {}
    except OSError as ex:
        print(f"{ex.strerror}: {report_file}", file=sys.stderr)
        report = {}
    return report


def save_report(report: dict[str, dict], report_file: str):
    try:
        with io.open(report_file, "w", encoding="utf-8") as fp:
            json.dump(report, fp, indent=2)
    except OSError as ex:
        print(f"{ex.strerror}: {report_file}", file=sys.stderr)


def report_missing_serialized(
    pkg: str,
    branch: str,
    report_file: str = "",
    ref_branch: str = "rawhide",
    update: str = False,
) -> dict[str, dict]:
    existing_report = load_report(report_file) if report_file else {}
    if pkg in existing_report and not update:
        return existing_report
    else:
        pkg_report = report_missing_build_reqs(pkg, branch, ref_branch)
        if pkg in existing_report:
            existing_report[pkg].update(pkg_report[pkg])
        else:
            existing_report.update(pkg_report)
        save_report(existing_report, report_file)
        return existing_report
