################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

from watson_ts.blocks.augmentors.srom_jitter import Jitter
from watson_ts.blocks.augmentors.srom_noise import Noise
from watson_ts.blocks.augmentors.srom_trend_outlier import TrendOutlier


def get_perturbed_data(
    x, feature_columns, target_columns, repeatations=1, random_state=5
):
    perturbed_mr = []
    augmentors = [Jitter, Noise, TrendOutlier]
    for i in range(0, repeatations):
        for augmentor in augmentors:
            if augmentor == Noise:
                aug = augmentor(
                    feature_columns=feature_columns,
                    target_columns=target_columns,
                    seed=random_state + i
                )
            else:
                aug = augmentor(
                    feature_columns=feature_columns,
                    target_columns=target_columns,
                    random_state=random_state + i,
                )
            tf_x = aug.fit(x).transform(x)
            # print(augmentor, tf_x)
            perturbed_mr.append(tf_x)
    return perturbed_mr
