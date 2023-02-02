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

import subprocess

from typing import Union

REQ_SUMMARY = "Please branch and build {pkg} in {branch}"

REQ_DESC = "Please branch and build {pkg} in {branch}.\n"

REQ_DESC_FAS = (
    "Please branch and build {pkg} in {branch}.\n"
    "\n"
    "If you do not wish to maintain {pkg} in {branch},\n"
    "or do not think you will be able to do this in a timely manner,\n"
    "I would be happy to be a co-maintainer of the package (FAS: {fas});\n"
    "please add me through https://src.fedoraproject.org/rpms/{pkg}/adduser\n"
)

REQ_DESC_SIG = (
    "Please branch and build {pkg} in {branch}.\n"
    "\n"
    "If you do not wish to maintain {pkg} in {branch},\n"
    "or do not think you will be able to do this in a timely manner,\n"
    "the EPEL Packagers SIG would be happy to be a co-maintainer of the package;\n"
    "please add the epel-packagers-sig group through\n"
    "https://src.fedoraproject.org/rpms/{pkg}/addgroup\n"
    "and grant it commit access, or collaborator access on epel* branches.\n"
)

REQ_DESC_FAS_SIG = REQ_DESC_SIG + (
    "\n"
    "I would also be happy to be a co-maintainer (FAS: {fas});\n"
    "please add me through https://src.fedoraproject.org/rpms/{pkg}/adduser\n"
)


def generate_request_cmd(
    pkg: str,
    branch: str,
    fas: str,
    is_sig: bool,
    blocked: list[str],
    in_epel: bool,
) -> Union[bool, str]:
    summary = REQ_SUMMARY.format(pkg=pkg, branch=branch)
    if fas:
        if is_sig:
            desc_template = REQ_DESC_FAS_SIG
        else:
            desc_template = REQ_DESC_FAS
    elif is_sig:
        desc_template = REQ_DESC_SIG
    else:
        desc_template = REQ_DESC
    desc = desc_template.format(pkg=pkg, branch=branch, fas=fas)
    if in_epel:
        cmd = (
            f"bugzilla new --product 'Fedora EPEL' --version '{branch}' "
            f"--component '{pkg}' --summary '{summary}' --comment '{desc}' "
            f"--blocked '{','.join(blocked)}'"
        )
    else:
        cmd = (
            f"bugzilla new --product 'Fedora' --version 'rawhide' "
            f"--component '{pkg}' --summary '{summary}' --comment '{desc}' "
            f"--blocked '{','.join(blocked)}'"
        )
    return cmd


def file_request(
    pkg: str,
    branch: str,
    fas: str = None,
    is_sig: bool = False,
    blocked: list[str] = ["EPELPackagersSIG"],
) -> Union[bool, str]:
    cmd = generate_request_cmd(pkg, branch, fas, is_sig, blocked, True)
    r = subprocess.run(cmd, capture_output=True, shell=True)

    # package not in EPEL
    if r.returncode == 3:
        cmd = generate_request_cmd(pkg, branch, fas, is_sig, blocked, False)
        r = subprocess.run(cmd, capture_output=True, shell=True)

    if r.returncode != 0:
        raise RuntimeError(r.stdout.decode())

    return r.stdout.decode()
