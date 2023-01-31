import os
import requests
import lithops
import pandas as pd
import numpy as np
import tempfile
from uuid import uuid4
import logging
import ibm_boto3
import time
from ibm_platform_services import IamIdentityV1
from ibm_platform_services import GlobalCatalogV1
from ibm_platform_services import ResourceControllerV2
from ibm_code_engine_sdk.ibm_cloud_code_engine_v1 import IbmCloudCodeEngineV1
from autoai_ts_libs.deps.srom.utils import s3utils
import kubernetes
from autoai_ts_libs.deps.srom.time_series.run_timeseries_anomaly import run_timeseries_anomaly
from io import StringIO
from autoai_ts_libs.deps.srom.time_series.utils.types import (
    TSPDAGType,
    AnomalyAlgorithmType,
    AnomalyScoringPredictionType,
    AnomalyScoringAlgorithmType,
    WindowADAlgorithmType,
    AnomalyExecutionModeType,
)
from autoai_ts_libs.deps.srom.utils.lithops import exclude_modules_list
from autoai_ts_libs.deps.srom.pipeline.execution_types.srom_lithops_search import csv_to_pandasdf

LOGGER = logging.getLogger(__name__)


class CodeEngineTrainer:
    """[summary]"""

    def __init__(self, mode, pipeline=None, param_dict={}):
        """[summary]

        Args:
                api_key ([type]): [description]
                cos_creds ([type]): [description]
                project_name (str, optional): [description]. Defaults to "TestSROM".
        """
        self.mode = mode
        self.pipeline = pipeline
        self._metadata = {
            "train_bucket_name": None,
            "result_bucket_name": None,
            "data_X": None,
            "data_y": None,
        }
        self.param_dict = param_dict

    def connect(self, api_key, project_name, cos_credentials):
        """This method get the keys and cross verify all

        Args:
            api_key ([type]): [description]
            project_name ([type]): [description]
            cos_credentials ([type]): [description]
        """
        self.api_key = api_key
        self.cos_credentials = cos_credentials
        self.project_name = project_name
        self._cos_client = s3utils.boto3client(self.cos_credentials)
        self._set_environment_variables()
        self.guid_ = self._get_guid()

    def _set_environment_variables(
        self,
        iam_identity_type="iam",
        global_catalog_type="iam",
        resource_controlloer_type="iam",
    ):
        """[summary]"""
        os.environ["IAM_IDENTITY_URL"] = "https://iam.cloud.ibm.com"
        os.environ["IAM_IDENTITY_AUTHTYPE"] = iam_identity_type
        os.environ["IAM_IDENTITY_APIKEY"] = self.api_key
        os.environ["GLOBAL_CATALOG_URL"] = "https://globalcatalog.cloud.ibm.com/api/v1"
        os.environ["GLOBAL_CATALOG_AUTHTYPE"] = global_catalog_type
        os.environ["GLOBAL_CATALOG_APIKEY"] = self.api_key
        os.environ[
            "RESOURCE_CONTROLLER_URL"
        ] = "https://resource-controller.cloud.ibm.com/"

        os.environ["RESOURCE_CONTROLLER_AUTHTYPE"] = resource_controlloer_type
        os.environ["RESOURCE_CONTROLLER_APIKEY"] = self.api_key

    def _get_guid(self):
        """[summary]

        Returns:
                [type]: [description]
        """
        catalog_client = GlobalCatalogV1.new_instance()

        entry_search_result = catalog_client.list_catalog_entries(
            offset=0,
            limit=10,
            q="name:codeengine active:true",
            complete=True,
        ).get_result()

        guid_ = entry_search_result["resources"][0]["id"]
        return guid_

    def _get_kubeconfig(self):
        """[summary]

        Returns:
                [type]: [description]
        """
        resource_client = ResourceControllerV2.new_instance()
        ans = resource_client.list_resource_instances(
            limit=100, name=self.project_name
        ).get_result()
        pid = ans["resources"][0]["guid"]
        service_client = IamIdentityV1.new_instance()
        aut = service_client.authenticator

        ce_client = IbmCloudCodeEngineV1(authenticator=aut)
        ce_client.set_service_url(
            "https://api.us-south.codeengine.cloud.ibm.com/api/v1"
        )

        iam_response = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": self.api_key,
                "response_type": "delegated_refresh_token",
                "receiver_client_ids": "ce",
                "delegated_refresh_token_expiry": "3600",
            },
        )
        delegated_refresh_token = iam_response.json()["delegated_refresh_token"]

        kubeconfig_response = ce_client.get_kubeconfig(
            x_delegated_refresh_token=delegated_refresh_token,
            id=pid,
        )
        kubeconfig_response_ = kubeconfig_response.get_result().content
        kubeconfig_file, kubeconfig_filename = tempfile.mkstemp()
        os.write(kubeconfig_file, kubeconfig_response_)
        kubernetes.config.load_kube_config(config_file=kubeconfig_filename)
        kubeconfig_file = kubeconfig_file
        kubeconfig_filename = kubeconfig_filename
        kube_client = kubernetes.client.CoreV1Api()

        # Get something from project.
        contexts = kubernetes.config.list_kube_config_contexts(
            config_file=kubeconfig_filename
        )[0][0]
        namespace = contexts.get("context").get("namespace")
        configmaps = kube_client.list_namespaced_config_map(namespace)
        return (
            namespace,
            configmaps,
            kubeconfig_response_,
            kubeconfig_file,
            kubeconfig_filename,
        )

    def _create_train_result_bucket(
        self, train_bucket_name=None, result_bucket_name=None
    ):
        bucket_uid = str(uuid4())
        if train_bucket_name and result_bucket_name:
            buckets = [
                train_bucket_name + "-" + bucket_uid,
                result_bucket_name + "-" + bucket_uid,
            ]
        else:
            buckets = ["training-data-" + bucket_uid, "training-results-" + bucket_uid]

        self._metadata["train_bucket_name"] = buckets[0]
        self._metadata["result_bucket_name"] = buckets[1]

        for bucket in buckets:
            print('Creating bucket "{}"...'.format(bucket))
            try:
                self._cos_client.create_bucket(Bucket=bucket)
            except ibm_boto3.exceptions.ibm_botocore.client.ClientError as e:
                print("Error: {}.".format(e.response["Error"]["Message"]))

    def _upload_data(self, data, prefix):
        if (
            self._metadata["train_bucket_name"] is None
            and self._metadata["result_bucket_name"] is None
        ):
            self._create_train_result_bucket()

        if not isinstance(data, pd.DataFrame):
            raise Exception("data must be a pandas dataframe")

        _, atempfile = tempfile.mkstemp(prefix=prefix, suffix=".csv.gz")
        data.to_csv(atempfile, index=False, compression="gzip")
        basename = os.path.basename(atempfile)
        self._cos_client.upload_file(
            atempfile, self._metadata["train_bucket_name"], basename
        )
        try:
            time.sleep(1)
            os.remove(atempfile)
        except:
            pass
        return basename

    def add_data(self, X, y=None):
        if not isinstance(X, (pd.DataFrame, str, np.ndarray)):
            raise Exception(
                """Input data X should be either Pandas DataFrame, Numpy array or the
                    name of the object on Cloud Object storage."""
            )
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)

        self._metadata["data_X"] = self._upload_data(data=X, prefix="X_")

        if y is not None:
            if isinstance(y, (pd.core.series.Series, list)):
                y = pd.DataFrame({"target_label": list(y)})
            if not isinstance(y, (pd.DataFrame, str, np.ndarray)):
                raise Exception(
                    """Input target y should be either Pandas DataFrame, Numpy array or the
                        name of the object on Cloud Object storage."""
                )
            if isinstance(y, np.ndarray):
                y = pd.DataFrame(y)
            self._metadata["data_y"] = self._upload_data(data=y, prefix="y_")

        LOGGER.info("Data uploaded successfully.")

    def _create_config(self, compute_configuration_cpu, compute_configuration_memory):

        (
            self.namespace,
            self.configmaps,
            self.kubeconfig_response_,
            self.kubeconfig_file,
            self.kubeconfig_filename,
        ) = self._get_kubeconfig()

        config_dict = {
            "lithops": {
                "backend": "code_engine",
                "storage": "ibm_cos",
                "storage_bucket": "dhavalexp",
            },
            "ibm": {"iam_api_key": self.api_key},
            "code_engine": {
                "namespace": self.namespace,
                "region": "us-south",
                "kubecfg_path": str(self.kubeconfig_file)
                + str(self.kubeconfig_filename),
                "runtime_cpu": compute_configuration_cpu,
                "runtime_memory": compute_configuration_memory,
            },
            "ibm_cos": self.cos_credentials,
        }
        return config_dict

    def create_anomaly_function(self):
        """
        returns a function to be passed to lithops.
        """
        if "dag_type" in self.param_dict:
            del self.param_dict["dag_type"]

        param_dict = self.param_dict

        def anomaly_train_cf(anomaly_params):
            X_filename = anomaly_params[0][0]
            train_bucket_name = anomaly_params[0][1]
            tmp_cos_creds = anomaly_params[0][2]

            tmp_cos_creds["bucket"] = train_bucket_name

            X = csv_to_pandasdf(
                credentials=tmp_cos_creds,
                object_name=X_filename,
                region="us",
                public=True,
                resiliency="cross-region",
                location="us-geo",
                compression="gzip",
            )

            return run_timeseries_anomaly(
                dataName=X, dag_type=TSPDAGType.EXT_ML, **param_dict
            )

        return anomaly_train_cf

    def create_pipeline_function(self):
        """
        returns a function for pipeline execution
        """
        exec_config = self._exec_config
        pipeline = self.pipeline

        def pipeline_cf(anomaly_params):
            X_filename = anomaly_params[0][0]
            train_bucket_name = anomaly_params[0][1]
            tmp_cos_creds = anomaly_params[0][2]
            y_filename = anomaly_params[0][3]

            tmp_cos_creds["bucket"] = train_bucket_name

            X = csv_to_pandasdf(
                credentials=tmp_cos_creds,
                object_name=X_filename,
                region="us",
                public=True,
                resiliency="cross-region",
                location="us-geo",
                compression="gzip",
            )

            y = csv_to_pandasdf(
                credentials=tmp_cos_creds,
                object_name=y_filename,
                region="us",
                public=True,
                resiliency="cross-region",
                location="us-geo",
                compression="gzip",
            )

            # we assume execute does not need any other patameter? what about the
            # parameter we want to pass?
            # where is the pipeline object being stored on remote client
            return pipeline.execute(X, y, **exec_config)

        return pipeline_cf

    def set_exec_config(self, exec_config={}):
        # this is a common dictionary to be passed inside the pipeline.execute or a
        # anomaly function call or .Automate call
        if not exec_config:
            self._exec_config = {
                "exectype": "single_node_random_search",
                "execgranularity": "coarse",
                "asynchronous": False,
                "num_option_per_pipeline": 10,
                "label": "label",
                "n_jobs": None,
                "pre_dispatch": "2*n_jobs",
                "verbosity": "low",
            }
        self._exec_config = exec_config

    def execute(
        self,
        compute_configuration_cpu=2,
        compute_configuration_memory=4096,
        compute_runtime_image="us.icr.io/sromrelease/lithops-srom-v38:01",
    ):
        self.config_dict = self._create_config(
            compute_configuration_cpu, compute_configuration_memory
        )

        if self.mode == "Anomaly":
            if not self.param_dict:
                raise Exception(
                    "parameter dictionary is an required argument for anomaly training."
                )
            func = self.create_anomaly_function()
            lt = lithops.FunctionExecutor(
                backend="code_engine",
                runtime=compute_runtime_image,
                config=self.config_dict,
            )
            fun_arguments = [
                self._metadata["data_X"],
                self._metadata["train_bucket_name"],
                self.cos_credentials,
            ]
            future = lt.call_async(
                func, [fun_arguments], exclude_modules=exclude_modules_list
            )
            return future
        elif self.mode == "Pipeline":
            if not self.pipeline:
                raise Exception(
                    "Pipeline is an required argument for pipeline training."
                )
            func = self.create_pipeline_function()
            lt = lithops.FunctionExecutor(
                backend="code_engine",
                runtime=compute_runtime_image,
                config=self.config_dict,
            )
            fun_arguments = [
                self._metadata["data_X"],
                self._metadata["train_bucket_name"],
                self.cos_credentials,
                self._metadata["data_y"],
            ]
            future = lt.call_async(
                func, [fun_arguments], exclude_modules=exclude_modules_list
            )
            return future
        else:
            pass
