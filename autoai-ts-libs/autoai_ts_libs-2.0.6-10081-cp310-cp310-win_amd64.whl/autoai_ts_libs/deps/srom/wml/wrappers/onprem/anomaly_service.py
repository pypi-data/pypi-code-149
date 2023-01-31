import logging
import os
from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.utils import s3utils
import sys
from autoai_ts_libs.deps.srom.wml.wrappers.onprem.training import WMLTrainer

anomaly_parameters = {
    "--outputdataName": "$RESULT_DIR/sample.json",
    "--execution_mode": "BATCH",
    "--train_test_split_ratio": 0.7,
    "--feature_columns": "sensor_1",
    "--target_columns": "sensor_1",
    "--time_column": "Time",
    "--time_format": "%Y-%m-%d %H:%M:%S",
    "--algorithm_type": "WINDOWAD",
    "--num_estimators": 4,
    "--dag_type": "EXT_ML",
    "--total_execution_time": 240,
    "--execution_type": "single_node_random_search",
    "--lookback_win": "auto",
    "--observation_window": 10,
    "--scoring_method": "CHISQUARE",
    "--scoring_threshold": 10,
    "--prediction_type": "RECENT",
    "--anomaly_estimator": "ISOLATION_FOREST",
}

LOGGER = logging.getLogger(__name__)

# CONSTANTS

_PYTHONMAJOR = sys.version_info.major
_PYTHONMINOR = sys.version_info.minor

PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}"
if _PYTHONMAJOR == 3 and _PYTHONMINOR == 7:
    PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}_opence"

PYTHON = "python"


class AnomalyWMLTrainer(WMLTrainer):
    def __init__(self):
        pipeline = SROMPipeline()
        super().__init__(pipeline)

    def _validate_metadata(self):
        """
        Validates if training data exists or not.
        """
        if not self._metadata["data_X"]:
            raise Exception(
                "No training data found. "
                "Please use add_data method before using this method."
            )
        if (
            not self._metadata["train_bucket_name"]
            or not self._metadata["result_bucket_name"]
        ):
            raise Exception(
                "Both train_bucket_name and result_bucket_name must be set."
            )

    def add_data(self, X):
        """
        Method to upload data to the Cloud Object Storage.

        Args:
        X ([Dataframe]): Data for anomaly estimation.

        """
        if not isinstance(X, (pd.DataFrame, str, np.ndarray)):
            raise Exception(
                """Input data X should be either Pandas DataFrame, Numpy array or the
                    name of the object on Cloud Object storage."""
            )

        # force a dataframe in all cases
        # to give us an easy path to to_csv
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)

        self._metadata["data_X"] = self._upload_data(data=X, prefix="X_")

        LOGGER.info("Data uploaded successfully.")

    def _generate_exec_command(self, param_dict):
        """
        Generates execution command to run on WML.
        """
        execution_cmd = ""
        execution_cmd += "pip install $DATA_DIR/{} && ".format(
            os.path.basename("srom-development_wml.zip")
        )

        # Add all the packages that are to be installed
        for _, adict in self._third_party_packages.items():
            archive = adict["archive"]
            execution_cmd += "pip install $DATA_DIR/{}[deep_learning,optimizer] && ".format(
                os.path.basename(archive)
            )

        # Add train script
        execution_cmd += "python -m srom.time_series.run_timeseries_anomaly"
        # Add references to training data
        execution_cmd += " -df $DATA_DIR/{}".format(self._metadata["data_X"])

        if param_dict:
            if "--outputdataName" in param_dict:
                st = param_dict["--outputdataName"]
                if not st.startswith("$RESULT_DIR/"):
                    st = "$RESULT_DIR/" + st
                    param_dict["--outputdataName"] = st
            for key, values in param_dict.items():
                if key in anomaly_parameters:
                    anomaly_parameters[key] = values

        for key, values in anomaly_parameters.items():
            execution_cmd += " " + str(key) + " " + str(values)

        # execution_cmd += " -output_df $RESULT_DIR/sample_out.json"

        return execution_cmd

    def set_exec_config(self, exec_config={}):
        """
        anomaly_parameters = {
            "--outputdataName": "$RESULT_DIR/sample.json",
            "--execution_mode": "BATCH",
            "--train_test_split_ratio": 0.7,
            "--feature_columns": "sensor_1",
            "--target_columns": "sensor_1",
            "--time_column": "Time",
            "--time_format": "%Y-%m-%d %H:%M:%S",
            "--algorithm_type": "WINDOWAD",
            "--num_estimators": 4,
            "--dag_type": "EXT_ML",
            "--total_execution_time": 240,
            "--execution_type": "single_node_random_search",
            "--lookback_win": "auto",
            "--observation_window": 10,
            "--scoring_method": "CHISQUARE",
            "--scoring_threshold": 10,
            "--prediction_type": "RECENT",
            "--anomaly_estimator": "ISOLATION_FOREST",
        }
        
        """
        if exec_config is None:
            raise Exception("execution config is necessary.")
        else:
            self._exec_config = exec_config

    def execute(self, compute_configuration="K80", asynchronous=False, verbose=False):
        """
        Method for execution of the anomaly Pipeline.

        args:
            compute_configuration[string] default ("L") : Configuration size 
            asynchronous[boolean] default (False) : whether to execute asynchornously.
        """
        self.verbose = verbose
        self._validate_metadata()
        self._metadata["definition_ids"] = []
        self._metadata["training_ids"] = []
        self._metadata["experiment_details"] = None
        self._metadata["experiment_uid"] = None
        self._metadata["experiment_run_details"] = None
        self._metadata["experiment_run_uid"] = None
        self._metadata["compute_configuration"] = compute_configuration
        self._metadata["asynchronous"] = asynchronous
        # Reset result variables
        self.best_estimator = None
        self.best_score = None
        self.best_estimators = []
        self.best_scores = []
        self.trained_pipeline = None

        LOGGER.info("current metadata: %s", self._metadata)

        # Pickle and store pipeline
        pipeline_dump_file = self._serialize_object([None])
        pipeline_dump_dir = os.path.dirname(pipeline_dump_file)

        if self._exec_config is None:
            raise Exception("execution config is necessary.")

        # Generate execution command
        execution_cmd = self._generate_exec_command(self._exec_config)
        if self.verbose:
            print(execution_cmd)

        archive_file = self._create_srom_archive(
            file_location=pipeline_dump_dir,
            archive_name="srom_pipeline.zip",
            pipeline_dump_file=pipeline_dump_file,
        )

        # create training references based on execgranularity
        repository = self._wml_client.model_definitions
        model_definition_metadata = self._get_model_definition_metadata(execution_cmd)

        definition_details = repository.store(
            archive_file, meta_props=model_definition_metadata
        )
        definition_id = repository.get_id(definition_details)
        self._metadata["definition_ids"].append(definition_id)

        # prepare training metadata
        training_metadata = {
            self._wml_client.training.ConfigurationMetaNames.NAME: "SROM_WML_EXECUTION",
            self._wml_client.training.ConfigurationMetaNames.SPACE_UID: self._deployment_space_guid,
            self._wml_client.training.ConfigurationMetaNames.DESCRIPTION: "SROM Wml Execution",
            self._wml_client.training.ConfigurationMetaNames.MODEL_DEFINITION: {
                "id": definition_id,
                "hardware_spec": {
                    "name": self._metadata["compute_configuration"],
                    "nodes": 1,
                },
                "software_spec": {"name": "tensorflow_2.4-py3.8"},
                "model_type": "scikit-learn_0.23",
            },
        }

        self.create_cos_bucket_connections()
        training_metadata[
            self._wml_client.training.ConfigurationMetaNames.TRAINING_RESULTS_REFERENCE
        ] = {
            "connection": {"id": self.output_connection_id,},
            "location": {"bucket": self._metadata["result_bucket_name"]},
            "type": "connection_asset",
        }
        training_metadata[
            self._wml_client.training.ConfigurationMetaNames.TRAINING_DATA_REFERENCES
        ] = [
            {
                "type": "connection_asset",
                "connection": {"id": self.input_connection_id,},
                "location": {"bucket": self._metadata["train_bucket_name"]},
            }
        ]
        training = self._wml_client.training.run(training_metadata)
        self._metadata["training_info_df"] = training
        self._metadata["training_ids"] = self._wml_client.training.get_uid(training)

        LOGGER.info(
            "Training Started: Experiment UID is %s. Experiment Run UID is %s.",
            self._metadata["training_ids"],
            self._metadata["training_info_df"],
        )

    def fetch_results(self):
        """
        method to return the results after training and scoring the data.
        """
        if self.status() == "completed":
            training_id = self._metadata["training_ids"]
            bucket_name = self._wml_client.training.get_details(training_id)["entity"][
                "results_reference"
            ]["location"]["bucket"]
            training_name = self._wml_client.training.get_details(training_id)[
                "entity"
            ]["results_reference"]["location"]["logs"]

            bucket_obj = self._cos_resource.Bucket(bucket_name)

            result_path = ""
            for obj in bucket_obj.objects.iterator():
                if training_name in obj.key and ".json" in obj.key:
                    result_path = obj.key

            if len(result_path) > 0:
                file_name = result_path.split("/")[-1]
                bucket_obj.download_file(result_path, file_name)
                return file_name
            else:
                return ""
        return ""
