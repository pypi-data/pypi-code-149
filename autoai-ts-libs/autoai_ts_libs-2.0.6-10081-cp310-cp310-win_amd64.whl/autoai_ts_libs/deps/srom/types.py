# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Defines types (typically use as return types) in SROM
The purpose of this module is to try to encourage us to move
away from returning undocumeted tuples using undocumented orderings.

"""

from collections import namedtuple

# General return object for pipeline.execute
# calls. It's fine to have one or more of these
# as None depending on the context.
# Feel free to *append* values here
# as the case might be. Please do not
# remove values without checking use elsewhere
# in the code. Callers should not unpack values
# as regular tuples (although nothing prevents them)
# from doing so. It's better to obtain values by
# derefernecing the specific attribute. For example
# per = PipeLineExecutionReturn(best_estimators=a,best_scores=b,None, None, None)
# best_estimators = per.best_estimators
PipelineExecuteReturn = namedtuple(
    "PipelineExecuteReturn",
    [
        "best_estimators",
        "best_scores",
        "trained_pipelines",
        "best_estimator",
        "best_score",
        "trained_pipeline",
    ],
)
