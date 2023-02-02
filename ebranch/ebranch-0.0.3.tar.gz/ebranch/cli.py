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

import json
import subprocess
import sys
import click
import requests
from . import (
    __version__,
    bugzilla,
    dependencies as deps,
    dnf,
    pagure,
)


@click.group("Main CLI")
def cli() -> None:
    """
    Tool for branching Fedora packages for EPEL
    """


@cli.group()
def dependencies():
    """
    Commands for working with dependencies
    """


@cli.group()
def issues():
    """
    Commands for issue tracker integration
    """


@cli.command(help="Display ebranch version information")
def version() -> None:
    """
    Display ebranch version information
    """
    click.echo(__version__)


@dependencies.command(help="lists build requirements for a package")
@click.argument("pkgname")
@click.option("-r", "--ref-branch", default="rawhide", show_default=True)
def build_reqs(pkgname: str, ref_branch: str):
    """
    Lists build requirements for a package
    """
    for req in dnf.get_pkg_build_reqs(pkgname, ref_branch):
        click.echo(req)


@issues.command(help="file a branch request")
@click.argument("pkg")
@click.argument("branch")
@click.option(
    "-f",
    "--fas",
    default=None,
    show_default=True,
    help="FAS of reporter, if willing to co-maintain",
)
@click.option(
    "--sig/--no-sig",
    default=False,
    show_default=True,
    help="If reporter is in EPEL Packagers SIG, offer to have the SIG co-maintain this",
)
@click.option(
    "--blocked",
    default="EPELPackagersSIG",
    show_default=True,
    help="CSV list of issues blocked by this request",
)
def file_request(pkg: str, branch: str, fas: str, sig: bool, blocked: str):
    """
    File a branch request
    """
    click.echo(bugzilla.file_request(pkg, branch, fas, sig, blocked.split(",")))


@dependencies.command(help="Calculate chain build")
@click.argument("report")
def calculate_chain_build(report: str):
    """
    Calculate chain build
    """
    _deps = deps.DependencyAnalyzer.from_file(report)
    click.echo(_deps.calculate_chain_build())


@dependencies.command(help="Find dependency cycles")
@click.argument("report")
def find_cycles(report: str):
    """
    Find dependency cycles
    """
    _deps = deps.DependencyAnalyzer.from_file(report)
    click.echo(json.dumps(_deps.find_cycles(), indent=2))


@dependencies.command(help="checks if a package is branched")
@click.argument("pkgname")
@click.argument("branch")
def is_branched(pkgname: str, branch: str):
    """
    Checks if a package is branched
    """
    try:
        if pagure.is_pkg_branched(pkgname, branch):
            click.echo(f"{pkgname} is branched for {branch}")
        else:
            click.echo(f"{pkgname} is NOT branched for {branch}")
            sys.exit(1)
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            click.echo(f"{pkgname} does not exist in dist-git")
            sys.exit(2)


@dependencies.command(help="lists branches for a package")
@click.argument("pkgname")
def ls_branches(pkgname: str):
    """
    Lists branches for a package
    """
    try:
        click.echo(json.dumps(pagure.get_pkg_branches(pkgname)))
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            click.echo(f"{pkgname} does not exist in dist-git")
            sys.exit(2)


@dependencies.command(help="lists missing build requirements to build for a branch")
@click.argument("pkgname")
@click.argument("branch")
@click.option("-f", "--report-file", envvar="EBRANCH_FILE", default="")
@click.option(
    "-r",
    "--ref-branch",
    envvar="EBRANCH_REF",
    default="rawhide",
    show_default=True,
)
@click.option("--update/--no-update", default=False, show_default=True)
def missing_build_reqs(
    pkgname: str, branch: str, report_file: str, ref_branch: str, update: bool
):
    """
    Lists missing build requirements to build for a branch
    """
    try:
        click.echo(
            json.dumps(
                dnf.report_missing_serialized(
                    pkgname,
                    branch,
                    report_file=report_file,
                    ref_branch=ref_branch,
                    update=update,
                ),
                indent=2,
            )
        )
    except subprocess.CalledProcessError as error:
        click.echo(error.stderr)
        sys.exit(2)


@dependencies.command(help="adds new missing BRs to the top-level list")
@click.argument("report_file")
def unfold(report_file: str):
    """
    Adds new missing BRs to the top-level list
    """
    click.echo(
        json.dumps(
            dnf.unfold_report_serialized(
                report_file,
            ),
            indent=2,
        )
    )


@dependencies.command(help="computes missing BRs for new top-level packages")
@click.argument("report_file")
@click.argument("branch")
@click.option(
    "-r",
    "--ref-branch",
    envvar="EBRANCH_REF",
    default="rawhide",
    show_default=True,
)
def iterate(report_file: str, branch: str, ref_branch: str):
    """
    Computes missing BRs for new top-level packages
    """
    click.echo(
        json.dumps(
            dnf.iterate_report_serialized(report_file, branch, ref_branch=ref_branch),
            indent=2,
        )
    )
