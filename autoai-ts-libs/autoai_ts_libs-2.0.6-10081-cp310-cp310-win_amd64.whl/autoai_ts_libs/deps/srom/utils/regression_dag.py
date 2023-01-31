from sklearn.cluster import FeatureAgglomeration
from sklearn.cross_decomposition import PLSRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.decomposition import NMF, PCA, FastICA, KernelPCA, SparsePCA, TruncatedSVD
from sklearn.ensemble import (
    AdaBoostRegressor,
    BaggingRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.exceptions import NotFittedError
from sklearn.feature_selection import SelectKBest, SelectPercentile, VarianceThreshold
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.kernel_approximation import (
    AdditiveChi2Sampler,
    Nystroem,
    RBFSampler,
    SkewedChi2Sampler,
)
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import (
    BayesianRidge,
    ElasticNet,
    HuberRegressor,
    Lasso,
    LassoLars,
    LinearRegression,
    OrthogonalMatchingPursuit,
    PassiveAggressiveRegressor,
    RANSACRegressor,
    Ridge,
    SGDRegressor,
    TheilSenRegressor,
)
from sklearn.manifold import Isomap, LocallyLinearEmbedding
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import (
    MaxAbsScaler,
    MinMaxScaler,
    Normalizer,
    OneHotEncoder,
    PolynomialFeatures,
    QuantileTransformer,
    RobustScaler,
    StandardScaler,
)
from sklearn.tree import DecisionTreeRegressor
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.feature_engineering.model_based_feature_generator import (
    ModelbasedFeatureGenerator,
)
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from xgboost import XGBRegressor
from sklearn.preprocessing import KBinsDiscretizer, PowerTransformer
from sklearn.multioutput import MultiOutputRegressor
from sklearn.multioutput import RegressorChain

"""
This DAG type is not used now.
Kindly note that, we have 5 Regressors and
If we used this Dag type, we shd remove the
overlapping regressors used other place/pipeline.
"""


def get_tiny_dag():

    feature_transformation_set = [
        ("skiptransformation", NoOp()),
        ("polynomialfeatures", PolynomialFeatures()),
    ]

    scaler_set = [
        ("skipscaling", NoOp()),
        ("standardscaler", StandardScaler()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    feature_preprocessing_set = [
        ("skipfeaturepreprocessing", NoOp()),
        ("pca", PCA(random_state=42)),
    ]

    estimator_feature_generator = [
        ("SkipModelFeatureGeneration", NoOp()),
        ("lassolarsfeature", ModelbasedFeatureGenerator(LassoLars(random_state=42))),
        (
            "kneighborsregressorfeature",
            ModelbasedFeatureGenerator(KNeighborsRegressor()),
        ),
        (
            "decisiontreeregressorfeature",
            ModelbasedFeatureGenerator(DecisionTreeRegressor(random_state=42)),
        ),
        (
            "gradientboostingregressorfeature",
            ModelbasedFeatureGenerator(GradientBoostingRegressor(random_state=42)),
        ),
        (
            "baggingregressorfeature",
            ModelbasedFeatureGenerator(BaggingRegressor(random_state=42)),
        ),
        (
            "randomforestregressorfeature",
            ModelbasedFeatureGenerator(RandomForestRegressor(random_state=42)),
        ),
        # ("kernelridgefeature", ModelbasedFeatureGenerator(KernelRidge())),
    ]

    estimator_set = [
        ("linearregression", LinearRegression()),
        ("gradientboostingregressor", GradientBoostingRegressor(random_state=42)),
        ("extratreesregressor", ExtraTreesRegressor(random_state=42)),
        ("xgbregressor", XGBRegressor(random_state=42)),
    ]

    # initialize the stages of the pipeline
    stages = [
        feature_transformation_set,
        scaler_set,
        feature_preprocessing_set,
        estimator_feature_generator,
        estimator_set,
    ]

    return stages


"""
This Dag is used for a) Univariate Single Step Output,
b) Multi-variate Single Step problem based on Local Model.
and c) Recurssive Statetegy based Multi Step.
Note that Scaling is not used, but we have listed it here
for sack of not chaning the code too much
KNN and SGD should not used for Multi-Output.
"""


def get_flat_dag():

    scaler_set = [
        ("skipscaling", NoOp()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    estimator_set = [
        ("linearregression", LinearRegression()),
        ("gradientboostingregressor", GradientBoostingRegressor(random_state=42)),
        ("kneighborsregressor", KNeighborsRegressor()),
        ("sgdregressor", SGDRegressor(random_state=42, tol=0.001, max_iter=1000)),
        ("xgbregressor", XGBRegressor(random_state=42, objective="reg:squarederror")),
    ]
    # lgbm
    # try:
    #     from lightgbm import LGBMRegressor
    #     estimator_set.append(("lgbmregressor", LGBMRegressor(random_state=42)))
    # except:
    #     pass

    # initialize the stages of the pipeline
    stages = [
        scaler_set,
        estimator_set,
    ]

    return stages


"""
This DAG is used for All Remaining Multi-Output (Multi-Variate, Multi-Step).
Note that Scaling is not used, but we have listed it here
for sack of not chaning the code too much
KNN and SGD should not used for Multi-Output.
As they are very slow for doing prediction. 
"""


def get_multi_output_flat_dag(n_jobs=-1):
    scaler_set = [
        ("skipscaling", NoOp()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    estimator_set = [
        (
            "molinearregression",
            MultiOutputRegressor(LinearRegression(n_jobs=1), n_jobs=n_jobs),
        ),
        (
            "mosgdregressor",
            MultiOutputRegressor(
                SGDRegressor(random_state=42, tol=0.001, max_iter=1000), n_jobs=n_jobs
            ),
        ),
        (
            "moxgbregressor",
            MultiOutputRegressor(
                XGBRegressor(random_state=42, objective="reg:squarederror", n_jobs=1),
                n_jobs=n_jobs,
            ),
        ),
    ]

    # initialize the stages of the pipeline
    stages = [
        scaler_set,
        estimator_set,
    ]
    # multiouput lgbm
    # try:
    #     from lightgbm import LGBMRegressor
    #     estimator_set.append(("molgbmregressor",
    #                           MultiOutputRegressor(LGBMRegressor(random_state=42), n_jobs=-1)))
    # except:
    #     pass
    return stages


"""
This DAG is used for All Multi-Output (Multi-Variate, Multi-Step) 
Univariate Note that Scaling is not used, but we have listed it here
for sack of not chaning the code too much
If you want to use it, we need to disable RandomForestRegression
"""


def get_multi_output_tiny_dag(n_jobs=-1):

    feature_transformation_set = [
        ("skiptransformation", NoOp()),
        ("polynomialfeatures", PolynomialFeatures()),
    ]

    scaler_set = [
        ("skipscaling", NoOp()),
        ("standardscaler", StandardScaler()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    feature_preprocessing_set = [
        ("skipfeaturepreprocessing", NoOp()),
        ("pca", PCA(random_state=42)),
    ]

    estimator_feature_generator = [
        ("SkipModelFeatureGeneration", NoOp()),
        ("lassolarsfeature", ModelbasedFeatureGenerator(LassoLars(random_state=42))),
        (
            "kneighborsregressorfeature",
            ModelbasedFeatureGenerator(KNeighborsRegressor()),
        ),
        (
            "decisiontreeregressorfeature",
            ModelbasedFeatureGenerator(DecisionTreeRegressor(random_state=42)),
        ),
        (
            "gradientboostingregressorfeature",
            ModelbasedFeatureGenerator(GradientBoostingRegressor(random_state=42)),
        ),
        (
            "baggingregressorfeature",
            ModelbasedFeatureGenerator(BaggingRegressor(random_state=42)),
        ),
        (
            "randomforestregressorfeature",
            ModelbasedFeatureGenerator(RandomForestRegressor(random_state=42)),
        ),
        # ("kernelridgefeature", ModelbasedFeatureGenerator(KernelRidge())),
    ]

    estimator_set = [
        ("molinearregression", MultiOutputRegressor(LinearRegression(), n_jobs=n_jobs)),
        (
            "mogradientboostingregressor",
            MultiOutputRegressor(
                GradientBoostingRegressor(random_state=42), n_jobs=n_jobs
            ),
        ),
        (
            "moextratreesregressor",
            MultiOutputRegressor(ExtraTreesRegressor(random_state=42), n_jobs=n_jobs),
        ),
        (
            "moxgbregressor",
            MultiOutputRegressor(XGBRegressor(random_state=42), n_jobs=n_jobs),
        ),
    ]

    # initialize the stages of the pipeline
    stages = [
        feature_transformation_set,
        scaler_set,
        feature_preprocessing_set,
        estimator_feature_generator,
        estimator_set,
    ]

    return stages


"""
This DAG is used for testing purpose using Daisy Chain as a way to do multi-step forecast 
"""


def get_regression_chain_flat_dag():
    scaler_set = [
        ("skipscaling", NoOp()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    estimator_set = [
        ("rclinearregression", RegressorChain(LinearRegression())),
        (
            "rcgradientboostingregressor",
            RegressorChain(GradientBoostingRegressor(random_state=42)),
        ),
        ("rcxgbregressor", RegressorChain(XGBRegressor(random_state=42))),
    ]

    # initialize the stages of the pipeline
    stages = [
        scaler_set,
        estimator_set,
    ]

    return stages


"""
This DAG is used for testing puppose. 
"""


def get_regression_chain_tiny_dag():

    feature_transformation_set = [
        ("skiptransformation", NoOp()),
        ("polynomialfeatures", PolynomialFeatures()),
    ]

    scaler_set = [
        ("skipscaling", NoOp()),
        ("standardscaler", StandardScaler()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    feature_preprocessing_set = [
        ("skipfeaturepreprocessing", NoOp()),
        ("pca", PCA(random_state=42)),
    ]

    estimator_feature_generator = [
        ("SkipModelFeatureGeneration", NoOp()),
        ("lassolarsfeature", ModelbasedFeatureGenerator(LassoLars(random_state=42))),
        (
            "kneighborsregressorfeature",
            ModelbasedFeatureGenerator(KNeighborsRegressor()),
        ),
        (
            "decisiontreeregressorfeature",
            ModelbasedFeatureGenerator(DecisionTreeRegressor(random_state=42)),
        ),
        (
            "gradientboostingregressorfeature",
            ModelbasedFeatureGenerator(GradientBoostingRegressor(random_state=42)),
        ),
        (
            "baggingregressorfeature",
            ModelbasedFeatureGenerator(BaggingRegressor(random_state=42)),
        ),
        (
            "randomforestregressorfeature",
            ModelbasedFeatureGenerator(RandomForestRegressor(random_state=42)),
        ),
        # ("kernelridgefeature", ModelbasedFeatureGenerator(KernelRidge())),
    ]

    estimator_set = [
        ("molinearregression", RegressorChain(LinearRegression())),
        (
            "mogradientboostingregressor",
            RegressorChain(GradientBoostingRegressor(random_state=42)),
        ),
        ("moextratreesregressor", RegressorChain(ExtraTreesRegressor(random_state=42))),
        ("moxgbregressor", RegressorChain(XGBRegressor(random_state=42))),
    ]

    # initialize the stages of the pipeline
    stages = [
        feature_transformation_set,
        scaler_set,
        feature_preprocessing_set,
        estimator_feature_generator,
        estimator_set,
    ]

    return stages


"""
This DAG is used for testing purpose using MIMO (Multi-Input Multi-Output) 
as a way to do multi-step forecast 
"""


def get_MIMO_flat_dag():
    scaler_set = [
        ("skipscaling", NoOp()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    estimator_set = [
        ("linearregression", LinearRegression()),
        ("kneighborsregressor", KNeighborsRegressor()),
        ("extratreesregressor", ExtraTreesRegressor(random_state=42)),
    ]

    # initialize the stages of the pipeline
    stages = [
        scaler_set,
        estimator_set,
    ]
    return stages


"""
This DAG is used for testing purpose using MIMO (Multi-Input Multi-Output) 
as a way to do multi-step forecast 
"""


def get_MIMO_complete_flat_dag():
    scaler_set = [
        ("skipscaling", NoOp()),
        ("minmaxscaler", MinMaxScaler()),
    ]

    estimator_set = [
        ("linearregression", LinearRegression()),
        ("kneighborsregressor", KNeighborsRegressor()),
        ("extratreesregressor", ExtraTreesRegressor(random_state=42)),
        ("ridge", Ridge(random_state=42)),
        ("lasso", Lasso(random_state=42)),
        ("elasticnet", ElasticNet()),
        ("lassolars", LassoLars(random_state=42)),
        ("orthogonalmatchingpursuit", OrthogonalMatchingPursuit()),
        ("lassolars", LassoLars(random_state=42)),
        ("decisiontreeregressor", DecisionTreeRegressor(random_state=42)),
        ("mlpregressor", MLPRegressor(random_state=42)),
        ("baggingregressor", BaggingRegressor(random_state=42)),
        ("randomforestregressor", RandomForestRegressor(random_state=42)),
        ("plsregression", PLSRegression()),
        ("gaussianprocessregressor", GaussianProcessRegressor(random_state=42)),
        ("kernelridge", KernelRidge()),
        ("ransacregressor", RANSACRegressor(random_state=42)),
    ]

    # initialize the stages of the pipeline
    stages = [
        scaler_set,
        estimator_set,
    ]
    return stages


def get_xgboost_multi_dag(n_jobs=-1):
    estimator_set = [
        (
            "moxgbregressor",
            MultiOutputRegressor(XGBRegressor(random_state=42), n_jobs=n_jobs),
        )
    ]
    stages = [estimator_set]
    return stages


def get_lgbm_multi_dag(n_jobs=-1):
    from lightgbm import LGBMRegressor

    estimator_set = [
        (
            "molgbmregressor",
            MultiOutputRegressor(LGBMRegressor(random_state=42), n_jobs=n_jobs),
        )
    ]
    stages = [estimator_set]
    return stages


def get_xgb_dag():
    estimator_set = [("xgbregressor", XGBRegressor(random_state=42))]
    stages = [estimator_set]
    return stages


def get_lgbm_dag():
    from lightgbm import LGBMRegressor

    estimator_set = [("lgbmregressor", LGBMRegressor(random_state=42))]
    stages = [estimator_set]
    return stages


tiny_reg_dag = get_tiny_dag()
flat_reg_dag = get_flat_dag()
multi_output_flat_dag = get_multi_output_flat_dag()
multi_output_tiny_dag = get_multi_output_tiny_dag()
regression_chain_flat_dag = get_regression_chain_flat_dag()
regression_chain_tiny_dag = get_regression_chain_tiny_dag()
mimo_flat_dag = get_MIMO_flat_dag()
complete_mino_flat_dag = get_MIMO_complete_flat_dag()
xgb_dag = get_xgb_dag()
xgboost_multi_dag = get_xgboost_multi_dag()
try:
    lgbm_multi_dag = get_lgbm_multi_dag()
except:
    lgbm_multi_dag = None
try:
    lgbm_dag = get_lgbm_dag()
except:
    lgbm_dag = None
