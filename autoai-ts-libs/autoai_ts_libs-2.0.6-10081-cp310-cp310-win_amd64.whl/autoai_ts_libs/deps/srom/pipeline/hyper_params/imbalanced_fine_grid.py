# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2019 All Rights Reserved.
# US Government Users Restricted Rights
# Use, duplication or disclosure restricted by
# GSA ADP Schedule Contract with IBM Corp.

"""
Imbalanced Classification Grid: Contains a dictionary of hyper-parameters of
to deal with class imbalance problem.
"""
from imblearn.under_sampling import (
    AllKNN,
    ClusterCentroids,
    NearMiss,
    EditedNearestNeighbours,
    RepeatedEditedNearestNeighbours,
    CondensedNearestNeighbour,
    InstanceHardnessThreshold,
    NeighbourhoodCleaningRule,
    TomekLinks,
    OneSidedSelection,
    RandomUnderSampler,
)

from imblearn.over_sampling import ADASYN, SMOTE

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    RandomForestClassifier,
    GradientBoostingClassifier,
)

AllKNN_dict = {}
# AllKNN_dict['base_sampler'] = [AllKNN()]
AllKNN_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]
AllKNN_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

ClusterCentroids_dict = {}
# ClusterCentroids_dict['base_sampler'] = [ClusterCentroids()]
ClusterCentroids_dict["base_sampler__voting"] = ["hard", "soft"]
ClusterCentroids_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

NearMiss_dict = {}
# NearMiss_dict['base_sampler'] = [NearMiss()]
NearMiss_dict["base_sampler__version"] = [1, 2, 3]
NearMiss_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

EditedNearestNeighbours_dict = {}
# EditedNearestNeighbours_dict['base_sampler'] = [EditedNearestNeighbours()]
EditedNearestNeighbours_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]
EditedNearestNeighbours_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

RepeatedEditedNearestNeighbours_dict = {}
# RepeatedEditedNearestNeighbours_dict['base_sampler'] = [RepeatedEditedNearestNeighbours()]
RepeatedEditedNearestNeighbours_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]
RepeatedEditedNearestNeighbours_dict["base_sampler__kind_sel"] = ["all", "mode"]
RepeatedEditedNearestNeighbours_dict["base_sampler__max_iter"] = [25, 50, 100, 150]
RepeatedEditedNearestNeighbours_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

CondensedNearestNeighbour_dict = {}
# CondensedNearestNeighbour_dict['base_sampler'] = [CondensedNearestNeighbour()]
CondensedNearestNeighbour_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]
CondensedNearestNeighbour_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

InstanceHardnessThreshold_dict = {}
# InstanceHardnessThreshold_dict['base_sampler'] = [InstanceHardnessThreshold()]
InstanceHardnessThreshold_dict["base_sampler__estimator"] = [
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    AdaBoostClassifier(),
    GradientBoostingClassifier(),
]
InstanceHardnessThreshold_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

NeighbourhoodCleaningRule_dict = {}
# NeighbourhoodCleaningRule_dict['base_sampler'] = [NeighbourhoodCleaningRule()]
NeighbourhoodCleaningRule_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]
NeighbourhoodCleaningRule_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]
NeighbourhoodCleaningRule_dict["base_sampler__threshold_cleaning"] = [0.5, 0.3, 0.1]

TomekLinks_dict = {}
# TomekLinks_dict['base_sampler'] = [TomekLinks()]
TomekLinks_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]

OneSidedSelection_dict = {}
# OneSidedSelection_dict['base_sampler'] = [OneSidedSelection()]
OneSidedSelection_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]
OneSidedSelection_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]

ADASYN_dict = {}
# ADASYN_dict['base_sampler'] = [ADASYN()]
ADASYN_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]
ADASYN_dict["base_sampler__n_neighbors"] = [1, 3, 5, 7, 10]

SMOTE_dict = {}
# SMOTE_dict['base_sampler'] = [SMOTE()]
SMOTE_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]
SMOTE_dict["base_sampler__k_neighbors"] = [1, 3, 5, 7, 10]

RandomUnderSampler_dict = {}
# RandomUnderSampler_dict['base_sampler'] = [RandomUnderSampler()]
RandomUnderSampler_dict["base_sampler__sampling_strategy"] = [
    "majority",
    "not minority",
    "not majority",
    "all",
]
RandomUnderSampler_dict["base_sampler__replacement"] = [True, False]

base_sampler_grid_name = [
    "allknn",
    "clustercentroid",
    "nearmiss",
    "editednearestneighbours",
    "repeatededitednearestneighbours",
    "instancehardnessthreshold",
    "neighbourhoodcleaningrule",
    "condensednearestneighbour",
    "tomeklinks",
    "onesidedselection",
    "randomundersampler",
]

base_sampler_grid = [
    AllKNN_dict,
    ClusterCentroids_dict,
    NearMiss_dict,
    EditedNearestNeighbours_dict,
    RepeatedEditedNearestNeighbours_dict,
    InstanceHardnessThreshold_dict,
    NeighbourhoodCleaningRule_dict,
    CondensedNearestNeighbour_dict,
    TomekLinks_dict,
    OneSidedSelection_dict,
    RandomUnderSampler_dict,
]

base_model_grid_name = [
    "decisiontreeclassifier",
    "extratreesclassifier",
    "randomforestclassifier",
    "kneighborsclassifier",
    "logisticregression",
    "xgbclassifier",
    "mlpclassifier",
    "baggingclassifier",
]

from .classification_fine_grid import PARAM_GRID as CGrid

base_model_grid = []
for item in base_model_grid_name:
    tmp_dict = {}
    for item_key in CGrid.keys():
        if item_key.startswith(item):
            tmp_dict["base_model__" + item_key.split("__")[1]] = CGrid[item_key]
    base_model_grid.append(tmp_dict)

PARAM_GRID = {}
for sampler_grid_ind, sampler_grid in enumerate(base_sampler_grid):
    for model_grid_ind, model_grid in enumerate(base_model_grid):
        tmp_grid = {}
        tmp_grid.update(sampler_grid)
        tmp_grid.update(model_grid)
        for tmp_key in tmp_grid.keys():
            new_key = (
                ""
                + base_sampler_grid_name[sampler_grid_ind]
                + "_"
                + base_model_grid_name[model_grid_ind]
                + "__"
                + tmp_key
            )
            PARAM_GRID[new_key] = tmp_grid[tmp_key]


# class_weight based classifier
clf_model_name = [
    "decisiontreeclassifier",
    "randomforestclassifier",
    "sgdclassifier",
    "logisticregression",
    "extratreesclassifier",
    "kerasclassifier",
    "xgboostclassifier",
]
clf_model_grid = {}
for item in clf_model_name:
    for item_key in CGrid.keys():
        if item_key.startswith(item):
            clf_model_grid[item_key] = CGrid[item_key]

sklearn_class_weights = [{0: 0.1, 1: 0.9}, {0: 0.3, 1: 0.7}]
clf_model_grid["decisiontreeclassifier__class_weight"] = [
    "balanced"
] + sklearn_class_weights
clf_model_grid["randomforestclassifier__class_weight"] = [
    "balanced",
    "balanced_subsample",
] + sklearn_class_weights
clf_model_grid["sgdclassifier__class_weight"] = ["balanced"] + sklearn_class_weights
clf_model_grid["logisticregression__class_weight"] = [
    "balanced"
] + sklearn_class_weights
clf_model_grid["extratreesclassifier__class_weight"] = [
    "balanced",
    "balanced_subsample",
] + sklearn_class_weights
clf_model_grid["kerasclassifier__class_weight"] = ["auto"] + sklearn_class_weights
clf_model_grid["xgboostclassifier__max_delta_step"] = [1, 3, 5, 7, 9]
clf_model_grid["xgboostclassifier__scale_pos_weight"] = [0.01, 0.05, 0.1, 0.2, 1.0]

PARAM_GRID.update(clf_model_grid)
