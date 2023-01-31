# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


from sklearn.metrics.pairwise import pairwise_distances
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, ClassifierMixin
from autoai_ts_libs.deps.srom.auto.auto_imbalanced_classification import AutoImbalancedClassification
from sklearn.preprocessing import PolynomialFeatures, QuantileTransformer
from sklearn.decomposition import (
    PCA,
    FactorAnalysis,
    FastICA,
    IncrementalPCA,
    KernelPCA,
    NMF,
    SparsePCA,
    TruncatedSVD,
)
from sklearn.preprocessing import (
    MinMaxScaler,
    MaxAbsScaler,
    StandardScaler,
    RobustScaler,
)
from sklearn.feature_selection import SelectKBest, SelectPercentile
from sklearn.preprocessing import KBinsDiscretizer, PowerTransformer
from sklearn.exceptions import NotFittedError
from sklearn.manifold import (
    Isomap,
    LocallyLinearEmbedding,
    MDS,
    SpectralEmbedding,
    TSNE,
)
from autoai_ts_libs.deps.srom.auto.base_auto import SROMAutoPipeline
from autoai_ts_libs.deps.srom.feature_selection.variance_based_feature_selection import (
    LowVarianceFeatureElimination,
)
from sklearn.feature_selection import VarianceThreshold
from autoai_ts_libs.deps.srom.feature_engineering.model_based_feature_generator import (
    ModelbasedFeatureGenerator,
)
from autoai_ts_libs.deps.srom.utils.no_op import NoOp
from sklearn.preprocessing import OneHotEncoder, Normalizer
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis,
    QuadraticDiscriminantAnalysis,
)
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.kernel_approximation import (
    RBFSampler,
    AdditiveChi2Sampler,
    Nystroem,
    SkewedChi2Sampler,
)
from sklearn.cluster import KMeans, FeatureAgglomeration

from sklearn.ensemble import (
    AdaBoostClassifier,
    BaggingClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import (
    LogisticRegression,
    PassiveAggressiveClassifier,
    SGDClassifier,
    RidgeClassifier,
    Perceptron,
)
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC, NuSVC, SVC
from xgboost import XGBClassifier
from autoai_ts_libs.deps.srom.classification.sampler_based_imbalanced_classifier import ImbalancedClassifier
from imblearn.under_sampling import (
    AllKNN,
    # ClusterCentroids,
    NearMiss,
    EditedNearestNeighbours,
    RepeatedEditedNearestNeighbours,
    # CondensedNearestNeighbour,
    # InstanceHardnessThreshold,
    NeighbourhoodCleaningRule,
    TomekLinks,
    OneSidedSelection,
    RandomUnderSampler,
)

RANDOM_STATE = 42


def get_ac_dag():
    """ """
    feature_transformation_set = [
        ("skiptransformation", NoOp()),
        ("discretizer", KBinsDiscretizer()),
        ("powertransformer", PowerTransformer()),
        ("onehotencoder", OneHotEncoder(sparse=False)),
        ("polynomialfeatures", PolynomialFeatures()),
        ("normalizer", Normalizer()),
    ]

    scaler_set = [
        ("skipscaling", NoOp()),
        ("standardscaler", StandardScaler()),
        ("minmaxscaler", MinMaxScaler()),
        ("maxabsscaler", MaxAbsScaler()),
        ("robustscaler", RobustScaler(quantile_range=(25, 75))),
        (
            "quantilescalinguniform",
            QuantileTransformer(
                output_distribution="uniform", random_state=RANDOM_STATE
            ),
        ),
        (
            "quantilescalingnormal",
            QuantileTransformer(
                output_distribution="normal", random_state=RANDOM_STATE
            ),
        ),
    ]

    feature_preprocessing_set = [
        ("skipfeaturepreprocessing", NoOp()),
        ("pca", PCA(random_state=RANDOM_STATE)),
        ("fastica", FastICA(random_state=RANDOM_STATE)),
        ("kernelpca", KernelPCA(random_state=RANDOM_STATE)),
        ("selectkbest", SelectKBest()),
        ("variancethreshold", VarianceThreshold()),
        ("lowvariancefeatureelimination", LowVarianceFeatureElimination()),
        ("selectpercentile", SelectPercentile()),
        ("rbfsampler", RBFSampler(random_state=RANDOM_STATE)),
        ("additivechi2sampler", AdditiveChi2Sampler()),
        ("nmf", NMF(random_state=RANDOM_STATE)),
        ("nystroem", Nystroem(random_state=RANDOM_STATE)),
        ("truncatedsvd", TruncatedSVD(random_state=RANDOM_STATE)),
        ("skewedchi2sampler", SkewedChi2Sampler(random_state=RANDOM_STATE)),
        ("sparsepca", SparsePCA(random_state=RANDOM_STATE)),
        ("isomap", Isomap()),
        ("locallylinearembedding", LocallyLinearEmbedding(random_state=RANDOM_STATE)),
        ("featureagglomeration", FeatureAgglomeration()),
    ]

    estimator_feature_generator = [
        ("skipmodelfeaturegeneration", NoOp()),
        ("bernoullinbfeature", ModelbasedFeatureGenerator(BernoulliNB())),
        ("multinomialnbfeature", ModelbasedFeatureGenerator(MultinomialNB())),
        (
            "decisiontreeclassifierfeature",
            ModelbasedFeatureGenerator(
                DecisionTreeClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "extratreesclassifierfeature",
            ModelbasedFeatureGenerator(ExtraTreesClassifier(random_state=RANDOM_STATE)),
        ),
        (
            "randomforestclassifierfeature",
            ModelbasedFeatureGenerator(
                RandomForestClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "gradientboostingclassifierfeature",
            ModelbasedFeatureGenerator(
                GradientBoostingClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "kneighborsclassifierfeature",
            ModelbasedFeatureGenerator(KNeighborsClassifier()),
        ),
        # ('linearsvcfeature', ModelbasedFeatureGenerator(LinearSVC())),
        (
            "logisticregressionfeature",
            ModelbasedFeatureGenerator(LogisticRegression(random_state=RANDOM_STATE)),
        ),
        ("xgbclassifierfeature", ModelbasedFeatureGenerator(XGBClassifier())),
        # ('sgdclassifierfeature', ModelbasedFeatureGenerator(SGDClassifier())),
        ("svcfeature", ModelbasedFeatureGenerator(SVC(random_state=RANDOM_STATE))),
        # ('perceptronfeature', ModelbasedFeatureGenerator(Perceptron())),
        (
            "mlpclassifierfeature",
            ModelbasedFeatureGenerator(MLPClassifier(random_state=RANDOM_STATE)),
        ),
        # ('passiveaggressiveclassifierfeature', ModelbasedFeatureGenerator(PassiveAggressiveClassifier())),
        (
            "adaboostclassifierfeature",
            ModelbasedFeatureGenerator(AdaBoostClassifier(random_state=RANDOM_STATE)),
        ),
        ("gaussiannbfeature", ModelbasedFeatureGenerator(GaussianNB())),
        # ('lineardiscriminantanalysisfeature', ModelbasedFeatureGenerator(LinearDiscriminantAnalysis())),
        (
            "quadraticdiscriminantanalysisfeature",
            ModelbasedFeatureGenerator(QuadraticDiscriminantAnalysis()),
        ),
        (
            "gaussianprocessclassifierfeature",
            ModelbasedFeatureGenerator(
                GaussianProcessClassifier(random_state=RANDOM_STATE)
            ),
        ),
        # ('ridgeclassifierfeature', ModelbasedFeatureGenerator(RidgeClassifier())),
        (
            "baggingclassifierfeature",
            ModelbasedFeatureGenerator(BaggingClassifier(random_state=RANDOM_STATE)),
        ),
        (
            "kmeanclusterfeature",
            ModelbasedFeatureGenerator(KMeans(random_state=RANDOM_STATE)),
        ),
        ("nusvcfeature", ModelbasedFeatureGenerator(NuSVC(random_state=RANDOM_STATE))),
    ]

    estimator_set = [
        ("bernoullinb", BernoulliNB()),
        ("multinomialnb", MultinomialNB()),
        ("decisiontreeclassifier", DecisionTreeClassifier(random_state=RANDOM_STATE)),
        ("extratreesclassifier", ExtraTreesClassifier(random_state=RANDOM_STATE)),
        ("randomforestclassifier", RandomForestClassifier(random_state=RANDOM_STATE)),
        (
            "gradientboostingclassifier",
            GradientBoostingClassifier(random_state=RANDOM_STATE),
        ),
        ("kneighborsclassifier", KNeighborsClassifier()),
        # ('linearsvc', LinearSVC()),
        ("logisticregression", LogisticRegression(random_state=RANDOM_STATE)),
        ("xgbclassifier", XGBClassifier()),
        # ('sgdclassifier', SGDClassifier(loss='log')),
        ("svc", SVC(probability=True, random_state=RANDOM_STATE)),
        # ('perceptron', Perceptron()),
        ("mlpclassifier", MLPClassifier(random_state=RANDOM_STATE)),
        # ('passiveaggressiveclassifier', PassiveAggressiveClassifier()),
        ("adaboostclassifier", AdaBoostClassifier(random_state=RANDOM_STATE)),
        ("gaussiannb", GaussianNB()),
        # ('lineardiscriminantanalysis', LinearDiscriminantAnalysis()),
        ("quadraticdiscriminantanalysis", QuadraticDiscriminantAnalysis()),
        (
            "gaussianprocessclassifier",
            GaussianProcessClassifier(random_state=RANDOM_STATE),
        ),
        # ('ridgeclassifier', RidgeClassifier()),
        ("baggingclassifier", BaggingClassifier(random_state=RANDOM_STATE)),
        ("nusvc", NuSVC(probability=True, random_state=RANDOM_STATE)),
    ]

    # initialize the auto classification stages of the pipeline
    ac_stages = [
        feature_transformation_set,
        scaler_set,
        feature_preprocessing_set,
        estimator_feature_generator,
        estimator_set,
    ]
    return ac_stages


def get_aic_dag():
    """ """
    feature_transformation_set = [
        ("skiptransformation", NoOp()),
        ("discretizer", KBinsDiscretizer()),
        ("powertransformer", PowerTransformer()),
        ("onehotencoder", OneHotEncoder(sparse=False)),
        ("polynomialfeatures", PolynomialFeatures()),
        ("normalizer", Normalizer()),
    ]

    scaler_set = [
        ("skipscaling", NoOp()),
        ("standardscaler", StandardScaler()),
        ("minmaxscaler", MinMaxScaler()),
        ("maxabsscaler", MaxAbsScaler()),
        ("robustscaler", RobustScaler(quantile_range=(25, 75))),
        (
            "quantilescalinguniform",
            QuantileTransformer(
                output_distribution="uniform", random_state=RANDOM_STATE
            ),
        ),
        (
            "quantilescalingnormal",
            QuantileTransformer(
                output_distribution="normal", random_state=RANDOM_STATE
            ),
        ),
    ]

    feature_preprocessing_set = [
        ("skipfeaturepreprocessing", NoOp()),
        ("pca", PCA(random_state=RANDOM_STATE)),
        ("fastica", FastICA(random_state=RANDOM_STATE)),
        ("kernelpca", KernelPCA(random_state=RANDOM_STATE)),
        ("selectkbest", SelectKBest()),
        ("variancethreshold", VarianceThreshold()),
        ("lowvariancefeatureelimination", LowVarianceFeatureElimination()),
        ("selectpercentile", SelectPercentile()),
        ("rbfsampler", RBFSampler(random_state=RANDOM_STATE)),
        ("additivechi2sampler", AdditiveChi2Sampler()),
        ("nmf", NMF(random_state=RANDOM_STATE)),
        ("nystroem", Nystroem(random_state=RANDOM_STATE)),
        ("truncatedsvd", TruncatedSVD(random_state=RANDOM_STATE)),
        ("skewedchi2sampler", SkewedChi2Sampler(random_state=RANDOM_STATE)),
        ("sparsepca", SparsePCA(random_state=RANDOM_STATE)),
        ("isomap", Isomap()),
        ("locallylinearembedding", LocallyLinearEmbedding(random_state=RANDOM_STATE)),
        ("featureagglomeration", FeatureAgglomeration()),
    ]

    estimator_feature_generator = [
        ("skipmodelfeaturegeneration", NoOp()),
        ("bernoullinbfeature", ModelbasedFeatureGenerator(BernoulliNB())),
        ("multinomialnbfeature", ModelbasedFeatureGenerator(MultinomialNB())),
        (
            "decisiontreeclassifierfeature",
            ModelbasedFeatureGenerator(
                DecisionTreeClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "extratreesclassifierfeature",
            ModelbasedFeatureGenerator(ExtraTreesClassifier(random_state=RANDOM_STATE)),
        ),
        (
            "randomforestclassifierfeature",
            ModelbasedFeatureGenerator(
                RandomForestClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "gradientboostingclassifierfeature",
            ModelbasedFeatureGenerator(
                GradientBoostingClassifier(random_state=RANDOM_STATE)
            ),
        ),
        (
            "kneighborsclassifierfeature",
            ModelbasedFeatureGenerator(KNeighborsClassifier()),
        ),
        # ('linearsvcfeature', ModelbasedFeatureGenerator(LinearSVC())),
        (
            "logisticregressionfeature",
            ModelbasedFeatureGenerator(LogisticRegression(random_state=RANDOM_STATE)),
        ),
        ("xgbclassifierfeature", ModelbasedFeatureGenerator(XGBClassifier())),
        # ('sgdclassifierfeature', ModelbasedFeatureGenerator(SGDClassifier())),
        ("svcfeature", ModelbasedFeatureGenerator(SVC(random_state=RANDOM_STATE))),
        # ('perceptronfeature', ModelbasedFeatureGenerator(Perceptron())),
        (
            "mlpclassifierfeature",
            ModelbasedFeatureGenerator(MLPClassifier(random_state=RANDOM_STATE)),
        ),
        # ('passiveaggressiveclassifierfeature', ModelbasedFeatureGenerator(PassiveAggressiveClassifier())),
        (
            "adaboostclassifierfeature",
            ModelbasedFeatureGenerator(AdaBoostClassifier(random_state=RANDOM_STATE)),
        ),
        ("gaussiannbfeature", ModelbasedFeatureGenerator(GaussianNB())),
        #        ('lineardiscriminantanalysisfeature', ModelbasedFeatureGenerator(LinearDiscriminantAnalysis())),
        (
            "quadraticdiscriminantanalysisfeature",
            ModelbasedFeatureGenerator(QuadraticDiscriminantAnalysis()),
        ),
        (
            "gaussianprocessclassifierfeature",
            ModelbasedFeatureGenerator(
                GaussianProcessClassifier(random_state=RANDOM_STATE)
            ),
        ),
        #        ('ridgeclassifierfeature', ModelbasedFeatureGenerator(RidgeClassifier())),
        (
            "baggingclassifierfeature",
            ModelbasedFeatureGenerator(BaggingClassifier(random_state=RANDOM_STATE)),
        ),
        (
            "kmeanclusterfeature",
            ModelbasedFeatureGenerator(KMeans(random_state=RANDOM_STATE)),
        ),
        ("nusvcfeature", ModelbasedFeatureGenerator(NuSVC(random_state=RANDOM_STATE))),
    ]
    base_sampler_name = [
        "allknn",
        # "clustercentroid",
        "nearmiss",
        "editednearestneighbours",
        "repeatededitednearestneighbours",
        # "instancehardnessthreshold",
        "neighbourhoodcleaningrule",
        # "condensednearestneighbour",
        "tomeklinks",
        "onesidedselection",
        "randomundersampler",
    ]

    base_sampler_model = [
        AllKNN(),
        # ClusterCentroids(random_state=RANDOM_STATE),
        NearMiss(),
        EditedNearestNeighbours(),
        RepeatedEditedNearestNeighbours(),
        # InstanceHardnessThreshold(random_state=RANDOM_STATE),
        NeighbourhoodCleaningRule(),
        # CondensedNearestNeighbour(random_state=RANDOM_STATE),
        TomekLinks(),
        OneSidedSelection(random_state=RANDOM_STATE),
        RandomUnderSampler(random_state=RANDOM_STATE),
    ]

    base_model_name = [
        "decisiontreeclassifier",
        "kneighborsclassifier",
        "logisticregression",
        "xgbclassifier",
    ]

    base_model_model = [
        DecisionTreeClassifier(random_state=RANDOM_STATE),
        KNeighborsClassifier(),
        LogisticRegression(random_state=RANDOM_STATE),
        XGBClassifier(),
    ]

    tmp_set_ = []
    for sampler_grid_ind, sampler_mdl in enumerate(base_sampler_model):
        for model_grid_ind, model_mdl in enumerate(base_model_model):
            new_key = (
                ""
                + base_sampler_name[sampler_grid_ind]
                + "_"
                + base_model_name[model_grid_ind]
            )
            tmp_set_.append(
                (
                    new_key,
                    ImbalancedClassifier(
                        base_sampler=sampler_mdl, base_model=model_mdl
                    ),
                )
            )

    estimator_set = [
        ("decisiontreeclassifier", DecisionTreeClassifier(random_state=RANDOM_STATE)),
        ("extratreesclassifier", ExtraTreesClassifier(random_state=RANDOM_STATE)),
        ("randomforestclassifier", RandomForestClassifier(random_state=RANDOM_STATE)),
        ("logisticregression", LogisticRegression(random_state=RANDOM_STATE)),
        ("xgbclassifier", XGBClassifier()),
        # ('sgdclassifier',SGDClassifier(loss='log'))
    ]
    estimator_set = estimator_set + tmp_set_
    aic_stages = [
        feature_transformation_set,
        scaler_set,
        feature_preprocessing_set,
        estimator_feature_generator,
        estimator_set,
    ]
    return aic_stages


auto_classification_dag = get_ac_dag()
auto_imbalanced_classification_dag = get_aic_dag()
