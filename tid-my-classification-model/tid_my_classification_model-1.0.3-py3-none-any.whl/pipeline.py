from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from model.config.core import config

price_pipe = Pipeline(
    [
        # ===== Standard Scaler =====
        # Make the features to be in the same scale
        (
            "StandardScaler",
            StandardScaler(),
        ),
        (
            "rf",
            RandomForestClassifier(
                n_estimators=config.model_config.n_estimators,
                bootstrap=config.model_config.bootstrap,
                criterion=config.model_config.criterion,
                max_depth=config.model_config.max_depth,
                max_features=config.model_config.max_features,
                max_leaf_nodes=config.model_config.max_leaf_nodes,
                max_samples=config.model_config.max_samples,
                n_jobs=config.model_config.n_jobs,
            ),
        ),
    ]
)
