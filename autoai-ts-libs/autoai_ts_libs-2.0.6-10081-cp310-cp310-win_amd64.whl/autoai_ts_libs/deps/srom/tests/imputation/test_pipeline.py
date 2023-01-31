# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
import pandas as pd
from warnings import simplefilter

from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import cross_validate_impute
from autoai_ts_libs.deps.srom.imputation.pipeline_utils import ImputationKFold
from autoai_ts_libs.deps.srom.imputation.metrics import r2_imputation_score
from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid

RANDOM_STATE = 7  # seed for simulations


def test1(
    iterations, missing_vals, test_classifier_pipeline=True, compare_imputers=True
):
    simplefilter(action="ignore", category=FutureWarning)
    simplefilter(action="ignore", category=DeprecationWarning)
    simplefilter(action="ignore", category=UserWarning)
    simplefilter(action="ignore", category=RuntimeWarning)
    simplefilter(action="ignore", category=UserWarning)
    X = pd.read_csv("./datasets/banana.csv")
    X, y = X[["c1", "c2"]].values.reshape(-1, 2), X[["label"]].values.reshape(-1, 1)
    A = SROMPipeline()
    if test_classifier_pipeline:
        A.set_stages(
            [
                [
                    ("meanimputer", SimpleImputer(strategy="mean")),
                    ("medianimputer", SimpleImputer(strategy="median")),
                    ("mostfrequentimputer", SimpleImputer(strategy="most_frequent")),
                ],
                [("decisiontreeclassifier", DecisionTreeClassifier())],
            ]
        )
        # Image(a.create_graph())
        A.execute(X, y)
        ParamDict = {}

        ParamDict["decisiontreeclassifier__max_depth"] = [1, 3, 5, 7, 9]
        sDict = SROMParamGrid()
        sDict.set_param_grid(ParamDict)
        A.execute(
            X,
            y,
            param_grid=sDict,
            exectype="single_node_random_search",
            num_option_per_pipeline=10,
        )

    if compare_imputers:
        ParamDict = {}
        A = SROMPipeline()
        A.set_stages(
            [
                [
                    ("meanimputer", SimpleImputer(strategy="mean")),
                    ("medianimputer", SimpleImputer(strategy="median")),
                    ("mostfrequentimputer", SimpleImputer(strategy="most_frequent")),
                ]
            ]
        )
        A.set_cross_val_score(cross_validate_impute)
        cv = ImputationKFold(
            n_iteration=iterations, impute_size=missing_vals, random_state=RANDOM_STATE
        )
        A.set_cross_validation(cv)
        A.set_scoring(r2_imputation_score)
        A.execute(X, X, exectype="spark_node_random_search")


if __name__ == "__main__":
    test1(10, 0.2, True, True)
