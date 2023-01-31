# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""This is a legacy file intentended to not break prior uses
It has been replaced by srom.wml.wrappers.onprem.scoring.WMLScorer.
Please start using that class instead.


*******DO NOT ADD ANY SPECIALIZED CODE TO THIS FILE *******

"""

from autoai_ts_libs.deps.srom.wml.wrappers.onprem.scoring import WMLScorer as TheRealScorer


class WMLScorer(TheRealScorer):
    """Legacy class to prevent existing uses from breaking.
    Please use srom.wml.wrappers.onprem.scoring.WMLScorer instead."""

    def __init__(self):
        super(WMLScorer, self).__init__()
        print("WARN: please use srom.wml.wrappers.onprem.scoring.WMLScorer instead.")
