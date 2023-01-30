#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function

from . import sqlobject


class RunConfig(sqlobject.SQLObject):
    """
    """

    table_name = 'runconfig'

    def attachToRun(self, run):
        self["run_id"] = run.id

    def addConfigFile(self, configfile):
        self["configfile_id"] = configfile.id

    def __init__(self, base):
        sqlobject.SQLObject.__init__(self, base)
        self.table_name = "runconfig"
        self.foreign_keys["run_id"] = "runs"
        self.foreign_keys["configfile_id"] = "configfiles"
        self.types["run_id"] = int
        self.types["configfile_id"] = int
