# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import warnings

from gluonts.mx.model.deepvar_hierarchical import (
    constraint_mat,
    null_space_projection_mat,
    DeepVARHierarchicalEstimator,
    reconcile_samples,
    coherency_error,
)

warnings.warn(
    "The module gluonts.model.deepvar_hierarchical has been moved to "
    "gluonts.mx.model.deepvar_hierarchical. In GluonTS v0.12 it will be no "
    "longer possible to use the old path. Try to use 'from gluonts.mx import "
    "DeepVARHierarchicalEstimator'.",
    FutureWarning,
)

__all__ = [
    "DeepVARHierarchicalEstimator",
    "constraint_mat",
    "null_space_projection_mat",
    "reconcile_samples",
    "coherency_error",
]
