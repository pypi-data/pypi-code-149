# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

# FIXME: We have removed aconfig as submodule and added it in the requirements.txt file.
# In order to support the existing code that imports from autoai_ts_libs.deps.watson_core.toolkit,
# we have included the import statement here
# pylint: disable=unused-wildcard-import,wildcard-import

from aconfig import *
