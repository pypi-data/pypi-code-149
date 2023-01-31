# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


from autoai_ts_libs.deps.srom.auto.auto_classification import AutoClassification
from autoai_ts_libs.deps.srom.auto.auto_imbalanced_classification import AutoImbalancedClassification
from autoai_ts_libs.deps.srom.utils.classification_dag import (
    auto_classification_dag,
    auto_imbalanced_classification_dag,
)
from sklearn.ensemble import RandomForestClassifier
import numpy as np



def prepare_classifier(mode="1", **params):
    """
    """
    if mode not in ["1", "2"]:
        raise NotImplementedError("multi-class prediction is not supported")

    if "stages" in params.keys():
        stages = params["stages"]
    else:
        stages = None

    if mode == "1":
        if stages == None:
            params["stages"] = auto_classification_dag
        classifier = AutoClassification(**params)
    elif mode == "2":
        if stages == None:
            params["stages"] = auto_imbalanced_classification_dag
        classifier = AutoImbalancedClassification(**params)

    return classifier

"""
def get_label_index_error_iid(train_x, train_y, clf = RandomForestClassifier()):
    '''
    This function call return a labeling error present in the dataset if any
    X : Numpy array
    y : Numpy array
    clf : can be any best pipeline you may get
    '''
    try:
        # FIXME cleanlab.util is an internal package which was patched out in
        #       https://github.com/cleanlab/cleanlab/pull/195 and hence will not work.
        from cleanlab.internal.util import (assert_inputs_are_valid,
        value_counts,)
        from cleanlab.count import (
        estimate_py_noise_matrices_and_cv_pred_proba,
        estimate_py_and_noise_matrices_from_probabilities,
        estimate_cv_predicted_probabilities,)
        from cleanlab.pruning import get_noise_indices
        

        K = len(np.unique(train_y))
        ps = value_counts(train_y) / float(len(train_y))
        confident_joint = None

        py, noise_matrix, inverse_noise_matrix, confident_joint, psx = estimate_py_noise_matrices_and_cv_pred_proba(
        X=train_x,
        s=train_y,
        clf=clf,
        cv_n_folds=3,
        thresholds=None,
        converge_latent_estimates=(False),
        seed=10,)

        noise_mask = get_noise_indices(
                train_y,
                psx,
                inverse_noise_matrix=inverse_noise_matrix,
                confident_joint=confident_joint,
                prune_method='prune_by_noise_rate',
                n_jobs=1,
            )
    
        return noise_mask
    except NameError:
        raise Exception("This function requires cleanlab library")
    except:
        raise Exception("plsease check input of get_label_index_error")
"""
