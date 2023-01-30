#
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2022 Indiscale GmbH <info@indiscale.com>
# Copyright (C) 2022 Florian Spreckelsen <f.spreckelsen@indiscale.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
try:
    from importlib import metadata as importlib_metadata
except ImportError:  # Python<3.8 dowesn"t support this so use
    import importlib_metadata

from packaging.version import parse as parse_version
from warnings import warn

# Read in version of locally installed caoscrawler package
version = importlib_metadata.version("caoscrawler")


class CfoodRequiredVersionError(RuntimeError):
    """The installed crawler version is older than the version specified in the
    cfood's metadata.

    """


def check_cfood_version(metadata: dict):

    if not metadata or "crawler-version" not in metadata:

        msg = """
No crawler version specified in cfood definition, so there is now guarantee that
the cfood definition matches the installed crawler version.

Specifying a version is highly recommended to ensure that the definition works
as expected with the installed version of the crawler.
        """

        warn(msg, UserWarning)
        return

    installed_version = parse_version(version)
    cfood_version = parse_version(metadata["crawler-version"])

    if cfood_version > installed_version:
        msg = f"""
Your cfood definition requires a newer version of the CaosDB crawler. Please
update the crawler to the required version.

Crawler version specified in cfood: {cfood_version}
Crawler version installed on your system: {installed_version}
        """
        raise CfoodRequiredVersionError(msg)

    elif cfood_version < installed_version:
        # only warn if major or minor of installed version are newer than
        # specified in cfood
        if (cfood_version.major < installed_version.major) or (cfood_version.minor < installed_version.minor):
            msg = f"""
The cfood was written for a previous crawler version. Running the crawler in a
newer version than specified in the cfood definition may lead to unwanted or
unexpected behavior. Please visit the CHANGELOG
(https://gitlab.com/caosdb/caosdb-crawler/-/blob/main/CHANGELOG.md) and check
for any relevant changes.

Crawler version specified in cfood: {cfood_version}
Crawler version installed on your system: {installed_version}
            """
            warn(msg, UserWarning)
            return

    # At this point, the version is either equal or the installed crawler
    # version is newer just by an increase in the patch version, so still
    # compatible. We can safely ...
    return
