# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Survival Analysis Fine Grid:
Contains a dictionary of hyper-parameters for survival analysis.
"""
PARAM_GRID = {}

PARAM_GRID['aalenadditiveregression__base_model__coef_penalizer'] = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]
PARAM_GRID['aalenadditiveregression__base_model__fit_intercept'] = [True, False]
PARAM_GRID['aalenadditiveregression__base_model__smoothing_penalizer'] = [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]

PARAM_GRID['coxregression__base_model__penalizer'] = [0.0, 0.01, 0.1, 0.5, 1.0, 5.0, 10.0]

PARAM_GRID['nelsonaalen__base_model__nelson_aalen_smoothing'] = [True, False]
