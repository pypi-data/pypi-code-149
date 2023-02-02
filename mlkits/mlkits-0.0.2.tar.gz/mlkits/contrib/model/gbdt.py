# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import numpy as np
import pandas as pd
import lightgbm as lgb
from typing import List, Text, Tuple, Union
from qlib.model.base import ModelFT
from qlib.data.dataset import DatasetH
from qlib.data.dataset.handler import DataHandlerLP
from qlib.model.interpret.base import LightGBMFInt
from qlib.data.dataset.weight import Reweighter
from qlib.workflow import R


class LGBModel(ModelFT, LightGBMFInt):
    """LightGBM Model"""

    def __init__(self, loss="mse", early_stopping_rounds=50, num_boost_round=1000, categorical_feature=None, **kwargs):
        if loss not in {"mse", "binary", "huber", "rmse", "multiclass"}:
            raise NotImplementedError
        if loss == "multiclass":
            self.multiclass = True
        else:
            self.multiclass = False
        self.params = {"objective": loss, "verbosity": -1}
        self.params.update(kwargs)
        self.early_stopping_rounds = early_stopping_rounds
        self.num_boost_round = num_boost_round
        self.categorical_feature = categorical_feature
        self.model = None

    def _prepare_data(self, dataset: DatasetH, reweighter=None) -> List[Tuple[lgb.Dataset, str]]:
        """
        The motivation of current version is to make validation optional
        - train segment is necessary;
        """
        ds_l = []
        assert "train" in dataset.segments
        for key in ["train", "valid"]:
            if key in dataset.segments:
                df = dataset.prepare(key, col_set=["feature", "label", "weight"], data_key=DataHandlerLP.DK_L)
                if df.empty:
                    raise ValueError("Empty data from dataset, please check your dataset config.")
                x, y = df["feature"], df["label"]
                feature_names = x.columns.values.tolist()

                # Lightgbm need 1D array as its label
                if y.values.ndim == 2 and y.values.shape[1] == 1:
                    y = np.squeeze(y.values)
                else:
                    raise ValueError("LightGBM doesn't support multi-label training")

                if reweighter is None or key != "train":
                    w = None
                elif isinstance(reweighter, Reweighter):
                    w = reweighter.reweight(df)
                else:
                    raise ValueError("Unsupported reweighter type.")
                ds_l.append((lgb.Dataset(x.values, label=y, weight=w, feature_name=feature_names, 
                                         categorical_feature=self.categorical_feature), key))
        return ds_l

    def fit(
        self,
        dataset: DatasetH,
        num_boost_round=None,
        early_stopping_rounds=None,
        verbose_eval=20,
        evals_result=None,
        reweighter=None,
        **kwargs,
    ):
        if evals_result is None:
            evals_result = {}  # in case of unsafety of Python default values
        ds_l = self._prepare_data(dataset, reweighter)
        ds, names = list(zip(*ds_l))
        self.model = lgb.train(
            self.params,
            ds[0],  # training dataset
            num_boost_round=self.num_boost_round if num_boost_round is None else num_boost_round,
            valid_sets=ds,
            valid_names=names,
            early_stopping_rounds=(
                self.early_stopping_rounds if early_stopping_rounds is None else early_stopping_rounds
            ),
            verbose_eval=verbose_eval,
            evals_result=evals_result,
            **kwargs,
        )
        for k in names:
            for key, val in evals_result[k].items():
                name = f"{key}.{k}"
                for epoch, m in enumerate(val):
                    R.log_metrics(**{name.replace("@", "_"): m}, step=epoch)
                    
    def fit(
        self,
        dataset: list,
        num_boost_round=None,
        early_stopping_rounds=None,
        verbose_eval=20,
        evals_result=None,
        reweighter=None,
        **kwargs,
    ):
        if evals_result is None:
            evals_result = {}  # in case of unsafety of Python default values
        ds, names = list(zip(*dataset))
        self.model = lgb.train(
            self.params,
            ds[0],  # training dataset
            num_boost_round=self.num_boost_round if num_boost_round is None else num_boost_round,
            valid_sets=ds,
            valid_names=names,
            early_stopping_rounds=(
                self.early_stopping_rounds if early_stopping_rounds is None else early_stopping_rounds
            ),
            verbose_eval=verbose_eval,
            evals_result=evals_result,
            **kwargs,
        )
        
    def predict(self, dataset: DatasetH, segment: Union[Text, slice] = "test"):
        if self.model is None:
            raise ValueError("model is not fitted yet!")
        x_test = dataset.prepare(segment, col_set=dataset.feature_columns, data_key=DataHandlerLP.DK_I)
        return pd.Series(self.model.predict(x_test.values), index=x_test.index)
    
    def predict(self, dataset: pd.DataFrame):
        if self.model is None:
            raise ValueError("model is not fitted yet!")
        if self.multiclass:
            results = np.array(self.model.predict(dataset.values))
            columns = ["prob_"+str(n) for n in range(results.shape[1])] + ['label']
            labels = np.argmax(results, axis=1)
            results = np.insert(results, results.shape[1], labels, axis=1)
            return pd.DataFrame(data=results, index=dataset.index, columns=columns)
        else:
            return pd.Series(self.model.predict(x_test.values), index=x_test.index)

    def finetune(self, dataset: DatasetH, num_boost_round=10, verbose_eval=20, reweighter=None):
        """
        finetune model

        Parameters
        ----------
        dataset : DatasetH
            dataset for finetuning
        num_boost_round : int
            number of round to finetune model
        verbose_eval : int
            verbose level
        """
        # Based on existing model and finetune by train more rounds
        dtrain, _ = self._prepare_data(dataset, reweighter)  # pylint: disable=W0632
        if dtrain.empty:
            raise ValueError("Empty data from dataset, please check your dataset config.")
        self.model = lgb.train(
            self.params,
            dtrain,
            num_boost_round=num_boost_round,
            init_model=self.model,
            valid_sets=[dtrain],
            valid_names=["train"],
            verbose_eval=verbose_eval,
        )
