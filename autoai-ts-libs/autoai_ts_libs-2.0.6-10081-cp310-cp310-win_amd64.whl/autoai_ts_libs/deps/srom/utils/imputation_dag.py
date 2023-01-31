# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.

from autoai_ts_libs.deps.srom.imputation.interpolators import (
    AkimaImputer,
    BaryCentricImputer,
    CubicImputer,
    QuadraticImputer,
    LinearImputer,
    PolynomialImputer,
    SplineImputer,
)


def get_timeseries_imputers_dag():

    """
    this function should return a list of imputers as DAG that can be directly feeded inside the 
    SROM DAG for the imputation
    """

    stages = [
        [
            ("akimaimputer", AkimaImputer()),
            ("barycentricimputer", BaryCentricImputer()),
            ("cubicimputer", CubicImputer()),
            ("quadraticimputer", QuadraticImputer()),
            ("linearimputer", LinearImputer()),
            ("polynomialimputer", PolynomialImputer()),
            ("splineImputer", SplineImputer()),
        ]
    ]

    return stages
