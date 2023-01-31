# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import joblib
import sys
import sklearn
import pandas as pd
import numpy as np
import tempfile

sys.modules["sklearn.externals.joblib"] = joblib

import logging

LOGGER = logging.getLogger(__name__)


try:
    from ibm_watson_machine_learning.helpers import DataConnection, S3Connection, S3Location
    from ibm_watson_machine_learning.experiment import AutoAI
    from ibm_watson_machine_learning import APIClient
except ImportError:
    LOGGER.error("ImportError : ibm_watson_machine_learning is not installed ")
    pass


class AutoAIEstimator:
    """[summary]
    """

    def __init__(
        self,
        wml_credentials=None,
        cos_credentials=None,
        space_id=None,
        target_column=None,
        scoring=None,
        prediction_type=None,
        experiment_name="AUTOAI_",
        background_mode=False,
        t_shirt_size="l",
        positive_label=None,
    ):
        """[summary]

        Args:
            wml_credentials ([type], optional): [description]. Defaults to None.
            cos_credentials ([type], optional): [description]. Defaults to None.
            space_id ([type], optional): [description]. Defaults to None.
            target_column ([type], optional): [description]. Defaults to None.
            scoring ([type], optional): [description]. Defaults to None.
            prediction_type ([type], optional): [description]. Defaults to None.
            experiment_name (str, optional): [description]. Defaults to "AUTOAI_".
            background_mode (bool, optional): [description]. Defaults to False.
            t_shirt_size (str, optional): [description]. Defaults to "l".
            positive_label ([type], optional): [description]. Defaults to None.
        """
        self.experiment_name = experiment_name
        self.wml_credentials = wml_credentials
        self.cos_credentials = cos_credentials
        self.autoai_optimizer = None
        self.best_pipeline = None
        self.background_mode = background_mode
        self.t_shirt_size = t_shirt_size
        self.positive_label = positive_label

        if not scoring:
            self.scoring = AutoAI.Metrics.ROOT_MEAN_SQUARED_ERROR
        else:
            self.scoring = scoring
        self.target_column = target_column
        self.space_id = space_id

        if prediction_type == "regression":
            self.prediction_type = AutoAI.PredictionType.REGRESSION
        else:
            self.prediction_type = "classification"

        if self.cos_credentials is None and self.space_id is not None:
            self.client = APIClient(wml_credentials)
            self.cos_credentials = self.client.spaces.get_details(space_id=space_id)[
                "entity"
            ]["storage"]["properties"]

    def store_data_on_cos(self, filepath=None):
        """[summary]

        Args:
            filepath ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        data_conn = DataConnection(
            connection=S3Connection(
                endpoint_url=self.cos_credentials["endpoint_url"],
                access_key_id=self.cos_credentials["credentials"]["editor"][
                    "access_key_id"
                ],
                secret_access_key=self.cos_credentials["credentials"]["editor"][
                    "secret_access_key"
                ],
            ),
            location=S3Location(
                bucket=self.cos_credentials["bucket_name"], path=filepath
            ),
        )
        data_conn.write(data=filepath, remote_name=filepath)
        return [data_conn]

    def fit(self, X, y):
        """[summary]

        Args:
            X ([type]): [description]
            y ([type]): [description]

        Returns:
            [type]: [description]
        """

        temp_dir = tempfile.TemporaryDirectory()
        data = pd.DataFrame(np.column_stack((X, y)))
        filelocation = temp_dir.name + "/data.csv"
        data.to_csv(
            filelocation, header=["{}".format(x) for x in data.columns], index=False
        )
        training_data_reference = self.store_data_on_cos(filelocation)
        # use temp_dir, and when done:
        temp_dir.cleanup()

        if self.prediction_type == "classification":
            if len(np.unique(y)) == 2:
                self.prediction_type = AutoAI.PredictionType.BINARY
            else:
                self.prediction_type = AutoAI.PredictionType.MULTICLASS
                # self.scoring = None

        experiment = AutoAI(self.wml_credentials, space_id=self.space_id)
        self.pipeline_optimizer = experiment.optimizer(
            name=self.experiment_name,
            prediction_type=self.prediction_type,
            prediction_column=self.target_column,
            scoring=self.scoring,
            t_shirt_size=self.t_shirt_size,
            positive_label=self.positive_label,
        )
        self.pipeline_optimizer.fit(
            training_data_reference=training_data_reference,
            background_mode=self.background_mode,
        )

        if not self.background_mode:
            self.best_pipeline = self.pipeline_optimizer.get_pipeline(
                astype=AutoAI.PipelineTypes.SKLEARN
            )
        return self

    def predict(self, data):
        """[summary]

        Args:
            data ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.best_pipeline.predict(data)

    def check_status(self):
        """[summary]
        """
        if self.pipeline_optimizer.get_run_status() == "completed":
            return self.best_pipeline == self.pipeline_optimizer.get_pipeline(
                astype=AutoAI.PipelineTypes.SKLEARN
            )

    def predict_proba(self, data):
        """[summary]

        Args:
            data ([type]): [description]

        Returns:
            [type]: [description]
        """
        try:
            return self.best_pipeline.predict_proba(data)
        except:
            return None

    def summary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.pipeline_optimizer.summary()

    def get_best_pipeline(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.best_pipeline

    def get_number_of_pipeline_enhancement(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        try:
            tmp_df = self.summary()
            return tmp_df.shape[0] + len(tmp_df["Enhancements"].sum().split(","))
        except:
            return np.NaN

    def get_pipeline_details(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        details = []
        opt = self.pipeline_optimizer
        summary_df = self.summary()
        for index in summary_df.index:
            detail = opt.get_pipeline_details(index)
            details.append(detail)
        return pd.DataFrame(details)

    def get_all_pipelines(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        details = []
        opt = self.pipeline_optimizer
        summary_df = self.summary()
        for index in summary_df.index:
            detail = opt.get_pipeline(index, astype=AutoAI.PipelineTypes.SKLEARN)
            details.append(detail)
        return details
