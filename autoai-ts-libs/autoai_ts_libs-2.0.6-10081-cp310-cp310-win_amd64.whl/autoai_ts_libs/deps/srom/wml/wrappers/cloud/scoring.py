# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Implements functionality to deploy and score a model over WML environment using WatsonMachineLearningAPIClient-v4."""

import logging

from autoai_ts_libs.deps.srom.wml.wrappers.onprem.scoring import WMLScorer as OnPremScorer

LOGGER = logging.getLogger(__name__)


class WMLScorer(OnPremScorer):
    ...


# Not much to see here
