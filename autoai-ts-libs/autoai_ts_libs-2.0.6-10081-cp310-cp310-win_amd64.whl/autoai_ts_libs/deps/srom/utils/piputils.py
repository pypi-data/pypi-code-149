# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Collection of utility methods for doing pip operations"""

import logging
import os
import subprocess
import sys
import tempfile

from autoai_ts_libs.deps.srom.utils.file_utils import possibly_unsafe_join

LOGGER = logging.getLogger(__name__)


def download_archive(
    package_name, version_filter, extra_index_url, pip_access_key, source_only
):
    """download a pip archive"""
    download_path = tempfile.mkdtemp()
    pip_args = ["pip", "download", "-d", download_path, "--timeout", "60"]
    if source_only:
        pip_args += ["--no-binary", ":all:"]
    if pip_access_key and extra_index_url:
        pip_args.append("--extra-index-url")
        pip_args.append("{}/{}".format(extra_index_url, pip_access_key))
    pip_args.append("{}{}".format(package_name, version_filter))
    pip_args.append("--no-deps")
    LOGGER.info("calling pip main with args %s", " ".join(pip_args))
    completed_process = subprocess.run(
        pip_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True
    )
    return_code = completed_process.returncode

    if return_code:
        sys.stdout.write(str(completed_process.stdout))
        sys.stdout.write(str(completed_process.stderr))
    # return tuple of return_code, [archives]
    archive = [
        possibly_unsafe_join(download_path, name) for name in os.listdir(download_path)
    ]
    if len(archive) != 1:
        raise Exception(
            "unexpected number ({}) of archives downloaded".format(len(archive))
        )
    archive = archive[0]  # it should always be 1-1 anyway
    print("pip downloaded {} with return_code {}".format(archive, return_code))
    return return_code, archive
