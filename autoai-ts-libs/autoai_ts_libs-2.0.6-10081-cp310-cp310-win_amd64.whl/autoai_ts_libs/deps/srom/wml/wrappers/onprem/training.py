# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import logging
import os
from pathlib import Path
import tempfile
import dill
import numpy as np
import pandas as pd
from autoai_ts_libs.deps.srom.utils import file_utils, piputils, s3utils
import zipfile
from retrying import retry
import sys

import logging

LOGGER = logging.getLogger(__name__)

try:
    from ibm_watson_machine_learning.client import APIClient
except ImportError:
    LOGGER.error("ImportError : ibm_watson_machine_learning is not installed ")
    pass

from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline
from uuid import uuid4
import ibm_boto3
from ibm_botocore.client import Config
import time

EXECTYPES = [
    "single_node_random_search",
    "pipeline_path_complete_search",
    "pipeline_path_random_search",
    "celery_node_random_search",
    "evolutionary_search",
    "rbfopt_search",
    "hyperband_search",
    "bayesian_search",
    "single_node_complete_search",
]

LOGGER = logging.getLogger(__name__)

# CONSTANTS

_PYTHONMAJOR = sys.version_info.major
_PYTHONMINOR = sys.version_info.minor

if _PYTHONMAJOR == 3 and _PYTHONMINOR == 7:
    PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}_opence"
else:
    PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}"

PYTHON = "python"


class WMLTrainer:
    def __init__(self, pipeline):
        """[summary]

        Args:
            pipeline ([type]): [description]

        Raises:
            Exception: [description]
        """
        if not isinstance(pipeline, SROMPipeline):
            raise Exception("Pipeline should be an instance of SROMPipeline.")

        self.pipeline = pipeline
        self._wml_client = None
        self._cos_client = None
        self._cos_resource = None
        self._deployment_space_guid = None
        self._package_extension_uids = []
        self._software_spec_uid = None
        self._deployment_details = None
        self._model_details = None
        self._metadata = {
            "train_bucket_name": None,
            "result_bucket_name": None,
            "data_X": None,
            "data_y": None,
            "definition_urls": None,
            "verbosity": None,
            "asynchronous": None,
            "exectype": None,
            "num_option_per_pipeline": None,
            "n_jobs": None,
            "pre_dispatch": None,
            "execgranularity": None,
            "label": None,
            "training_references": None,
            "experiment_details": None,
            "experiment_uid": None,
            "experiment_run_details": None,
            "experiment_run_uid": None,
            "training_info_df": None,
        }
        self._third_party_packages = {}
        self._exec_config = {}
        self._cos_endpoint = "https://iam.cloud.ibm.com/identity/token"
        self._cos_service_endpoint = (
            "https://s3.us-south.cloud-object-storage.appdomain.cloud"
        )
        self._cos_api_key = None
        self._cos_service_instance_id = None
        self._cos_access_key = None
        self._cos_secret_key = None
        self.verbose = False

        LOGGER.setLevel(logging.INFO)

    @classmethod
    def _guid_from_space_name(cls, client, space_name):
        """[summary]

        Args:
            client ([type]): [description]
            space_name ([type]): [description]

        Returns:
            [type]: [description]
        """
        space = client.spaces.get_details()
        ans = [
            item["metadata"]["id"]
            for item in space["resources"]
            if item["entity"]["name"] == space_name
        ]
        if len(ans) > 0:
            return ans[0]
        return None

    def cos_connection(self):
        if self._cos_credentials != None:
            self._cos_api_key = self._cos_credentials["apikey"]
            self._cos_service_instance_id = self._cos_credentials[
                "resource_instance_id"
            ]
            self._cos_access_key = self._cos_credentials["cos_hmac_keys"][
                "access_key_id"
            ]
            self._cos_secret_key = self._cos_credentials["cos_hmac_keys"][
                "secret_access_key"
            ]
        else:
            creds = self._wml_client.spaces.get_details(
                space_id=self._deployment_space_guid
            )["entity"]["storage"]["properties"]

            self._cos_service_endpoint = creds["endpoint_url"]
            self._cos_service_instance_id = creds["credentials"]["editor"][
                "resource_key_crn"
            ]
            self._cos_api_key = creds["credentials"]["editor"]["api_key"]
            self._cos_access_key = creds["credentials"]["editor"]["access_key_id"]
            self._cos_secret_key = creds["credentials"]["editor"]["secret_access_key"]

        self._cos_resource = ibm_boto3.resource(
            "s3",
            ibm_api_key_id=self._cos_api_key,
            ibm_service_instance_id=self._cos_service_instance_id,
            ibm_auth_endpoint=self._cos_endpoint,
            config=Config(signature_version="oauth"),
            endpoint_url=self._cos_service_endpoint,
        )
        self._cos_client = ibm_boto3.client(
            "s3",
            ibm_api_key_id=self._cos_api_key,
            ibm_service_instance_id=self._cos_service_instance_id,
            ibm_auth_endpoint=self._cos_endpoint,
            config=Config(signature_version="oauth"),
            endpoint_url=self._cos_service_endpoint,
        )

    @retry(stop_max_attempt_number=3)
    def connect(self, wml_credentials, deployment_space_name, cos_credentials):
        """[summary]

        Args:
            wml_credentials ([type]): [description]
            deployment_space_name (str): [description]
            cos_credentials ([type]): [description]
        """
        try:
            self._wml_client = APIClient(wml_credentials)
            self._deployment_space_guid = WMLTrainer._guid_from_space_name(
                client=self._wml_client, space_name=deployment_space_name
            )
            self._wml_client.set.default_space(self._deployment_space_guid)
            self._wml_credentials = wml_credentials
            self._cos_credentials = cos_credentials
            self.cos_connection()

            LOGGER.info("Connected successfully.")
        except Exception as e:
            LOGGER.exception(e)
            print(
                "Could not establish connection, check credentials and deployment space name."
            )

    def create_cos_bucket_connections(self):
        datasource_type = self._wml_client.connections.get_datasource_type_uid_by_name(
            "bluemixcloudobjectstorage"
        )

        auth_endpoint = self._cos_endpoint
        service_endpoint = self._cos_service_endpoint

        input_conn_meta_props = {
            self._wml_client.connections.ConfigurationMetaNames.NAME: "Input COS connection",
            self._wml_client.connections.ConfigurationMetaNames.DATASOURCE_TYPE: datasource_type,
            self._wml_client.connections.ConfigurationMetaNames.PROPERTIES: {
                "bucket": self._metadata["train_bucket_name"],
                "access_key": self._cos_access_key,
                "secret_key": self._cos_secret_key,
                "iam_url": auth_endpoint,
                "url": service_endpoint,
            },
        }

        output_conn_meta_props = {
            self._wml_client.connections.ConfigurationMetaNames.NAME: f"Output COS connection",
            self._wml_client.connections.ConfigurationMetaNames.DATASOURCE_TYPE: datasource_type,
            self._wml_client.connections.ConfigurationMetaNames.PROPERTIES: {
                "bucket": self._metadata["result_bucket_name"],
                "access_key": self._cos_access_key,
                "secret_key": self._cos_secret_key,
                "iam_url": auth_endpoint,
                "url": service_endpoint,
            },
        }

        input_conn_details = self._wml_client.connections.create(
            meta_props=input_conn_meta_props
        )
        output_conn_details = self._wml_client.connections.create(
            meta_props=output_conn_meta_props
        )
        self.input_connection_id = self._wml_client.connections.get_uid(
            input_conn_details
        )
        self.output_connection_id = self._wml_client.connections.get_uid(
            output_conn_details
        )

    def _validate_metadata(self):
        """
        Validates if training data exists or not.
        """
        if not self._metadata["data_X"] or not self._metadata["data_y"]:
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

    def _serialize_object(self, aobject):
        """
        Serialize given object and returns the pickled file path.
        """
        answer = Path(tempfile.mkdtemp()) / Path(tempfile.mkstemp()[1]).name
        dill.dump(aobject, open(answer, "wb"))
        return answer

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
            if (
                not self._cos_resource.Bucket(bucket)
                in self._cos_resource.buckets.all()
            ):
                if self.verbose:
                    print('Creating bucket "{}"...'.format(bucket))
                try:
                    self._cos_resource.create_bucket(Bucket=bucket)
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

    def add_data(self, X, y):
        if not isinstance(X, (pd.DataFrame, str, np.ndarray)):
            raise Exception(
                """Input data X should be either Pandas DataFrame, Numpy array or the
                    name of the object on Cloud Object storage."""
            )
        if isinstance(y, (pd.core.series.Series, list)):
            y = pd.DataFrame({"target_label": list(y)})
        if not isinstance(y, (pd.DataFrame, str, np.ndarray)):
            raise Exception(
                """Input target y should be either Pandas DataFrame, Numpy array or the
                    name of the object on Cloud Object storage."""
            )

        # force a dataframe in all cases
        # to give us an easy path to to_csv
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X)
        if isinstance(y, np.ndarray):
            y = pd.DataFrame(y)

        self._metadata["data_X"] = self._upload_data(data=X, prefix="X_")
        self._metadata["data_y"] = self._upload_data(data=y, prefix="y_")

        LOGGER.info("Data uploaded successfully.")

    def add_local_library(self, path):
        """
        method to add local srom library to wml.
        args:
            path: path of the compressed zip file of srom.
        """
        if (
            self._metadata["train_bucket_name"] is None
            and self._metadata["result_bucket_name"] is None
        ):
            self._create_train_result_bucket()
        self._cos_client.upload_file(
            path, self._metadata["train_bucket_name"], "srom-development_wml.zip"
        )

    def add_local_package(
        self,
        archive_path: str,
        package_name: str,
        package_description: str = "default description",
        package_type: str = "pip_zip",
    ):
        """
        Adds a local package to the deployment runtime. Should be used if custom libraries are needed to support the model deployment.

        Arguments:
            archive_path {string} -- The file name with fully qualified path pointing to the local package
            package_name {string} -- The name of the package to be used for WML purposes
            package_description {string} -- Description of the package. The default is empty string
            package_type {string} -- Look at WML documentation for the right values. Default is `pip_zip`

        Returns:
             dict -- the JSON representing the metadata of the created package
             string -- package extension UID
             string -- package extension URL

        """

        if (
            not os.path.isfile(archive_path)
            or not os.path.exists(archive_path)
            or not zipfile.is_zipfile(archive_path)
        ):
            raise Exception(
                """{} is either a directory, missing, or not a valid zip archive.""".format(
                    archive_path
                )
            )
        meta_prop_pkg_extn = {
            self._wml_client.package_extensions.ConfigurationMetaNames.NAME: package_name,
            self._wml_client.package_extensions.ConfigurationMetaNames.DESCRIPTION: package_description,
            self._wml_client.package_extensions.ConfigurationMetaNames.TYPE: package_type,
        }

        pkg_extn_details = self._wml_client.package_extensions.store(
            meta_props=meta_prop_pkg_extn, file_path=archive_path
        )
        pkg_extn_uid = self._wml_client.package_extensions.get_uid(pkg_extn_details)
        LOGGER.info("Created Package extension with ID %s", pkg_extn_uid)
        pkg_extn_url = self._wml_client.package_extensions.get_href(pkg_extn_details)
        self._package_extension_uids.append(pkg_extn_uid)

        LOGGER.info(
            "Package Extension UIDs in the list = %s", self._package_extension_uids
        )
        return pkg_extn_details, pkg_extn_uid, pkg_extn_url

    def add_pip_package(
        self, package_name, version, extra_index_url=None, pip_access_key=None
    ):
        """
        Adds a package obtained from public or private pip repository
        to the WML execution and/or runtime (deployment) services.

        Args:
            name (string): The name of the package to add (e.g., "srom", "numpy", etc.)
            version (string): A version tag (e.g., "1.1.0")
            extra_index_url (string, optional): An url to add to pip command line interface
                                                (see pip's documentation)
            pip_access_key (string, optional): A key or token for extra_index_url access. Note that
            unless both extra_index_url and pip_access_key are specified, neither will have any
            effect.
            Returns:
                tuple: return_code, downloaded_archive.
                0 is normal return, anything else should be treated with skepticism as
                pip itself is returning this to us. A non-zero code does not necessarily mean that
                the package could not be found and added only that you should take care to confirm
                it was via reading the stdout and stderr trace that will be echoed upon a non-zero
                return.
        """
        return_code, archive = piputils.download_archive(
            package_name=package_name,
            version_filter="=={}".format(version),
            extra_index_url=extra_index_url,
            pip_access_key=pip_access_key,
        )

        self.add_local_package(archive_path=archive, package_name=package_name)

        return return_code, archive

    def _add_software_specification(
        self,
        software_spec_name: str = "software_spec_name",
        software_spec_description: str = "software_spec_description",
        software_spec_type: str = PYTHON_SPEC,
        package_extn_uid_list: list = [],
    ):
        """
        Adds a software specification to the deployment runtime. Should be used if custom libraries are needed to support the model deployment.

        Arguments:
            software_spec_name {string} -- The name of the software spec to be used for the runtime purposes of the model
            software_spec_description {string} -- Description of the package. The default is empty string
            base_software_spec_name {string} -- Look at WML documentation for the right values. Default is `PYTHON_SPEC`
            package_extn_uid_list {list} -- The list of package extension UIDs if created outside this class, and need to be passed in. By default this is empty list

        Returns:
             dict -- the JSON representing the metadata of the software spec
             string -- softwars spec UID

        """
        if len(package_extn_uid_list) > 0:
            self._package_extension_uids.extend(package_extn_uid_list)

        LOGGER.info("Package Extension UIDs = %s", self._package_extension_uids)
        meta_prop_sw_spec = {
            self._wml_client.software_specifications.ConfigurationMetaNames.NAME: software_spec_name,
            self._wml_client.software_specifications.ConfigurationMetaNames.DESCRIPTION: software_spec_description,
            self._wml_client.software_specifications.ConfigurationMetaNames.BASE_SOFTWARE_SPECIFICATION: {
                "guid": self._wml_client.software_specifications.get_uid_by_name(
                    software_spec_type
                )
            },
        }

        sw_spec_details = self._wml_client.software_specifications.store(
            meta_props=meta_prop_sw_spec
        )
        sw_spec_uid = self._wml_client.software_specifications.get_uid(sw_spec_details)
        for package_extension_uid in self._package_extension_uids:
            self._wml_client.software_specifications.add_package_extension(
                sw_spec_uid, package_extension_uid
            )

        self._software_spec_uid = sw_spec_uid

        return sw_spec_details, sw_spec_uid

    def _generate_exec_command(self):
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
            execution_cmd += (
                "pip install $DATA_DIR/{}[deep_learning,optimizer] && ".format(
                    os.path.basename(archive)
                )
            )

        # Add train script
        execution_cmd += "python -m srom.wml.pipeline_skeleton"
        # Add references to training data
        execution_cmd += " --train_x {} --train_y {}".format(
            self._metadata["data_X"], self._metadata["data_y"]
        )
        # Add other details
        execution_cmd += (
            " --exectype "
            + self._metadata["exectype"]
            + " --num_option_per_pipeline "
            + str(self._metadata["num_option_per_pipeline"])
            + " --verbosity "
            + self._metadata["verbosity"]
            + " --execgranularity "
            + self._metadata["execgranularity"]
            + " --label "
            + self._metadata["label"]
            + " --n_jobs "
            + str(self._metadata["n_jobs"])
            + " --pre_dispatch "
            + self._metadata["pre_dispatch"]
        )

        return execution_cmd

    def _create_srom_archive(self, file_location, archive_name, pipeline_dump_file):
        """
        Creates archive file which contains necessary files for training.
        """
        archive_file = file_utils.possibly_unsafe_join(file_location, archive_name)
        archive = zipfile.ZipFile(archive_file, "w")
        archive.write(
            pipeline_dump_file,
            compress_type=zipfile.ZIP_DEFLATED,
            arcname="tmp_pipeline.pkl",
        )
        archive.close()
        return archive_file

    def _get_model_definition_metadata(self, execution_cmd):
        definition_meta_names = (
            self._wml_client.model_definitions.ConfigurationMetaNames
        )

        return {
            definition_meta_names.NAME: "srom-pipeline_execution",
            definition_meta_names.DESCRIPTION: "---",
            definition_meta_names.SPACE_UID: self._deployment_space_guid,
            definition_meta_names.PLATFORM: {"name": "python", "versions": ["3.8"]},
            definition_meta_names.VERSION: "{}.{}".format(
                sys.version_info.major, sys.version_info.minor
            ),
            definition_meta_names.COMMAND: execution_cmd,
        }

    def set_exec_config(self, exec_config={}):
        self._exec_config = exec_config

    def _process_exec_config(self):
        if not self._exec_config:
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

        for key in self._exec_config:
            self._metadata[key] = self._exec_config[key]

    def execute(
        self,
        compute_configuration="k80",
        compute_configuration_node=1,
        software_spec="tensorflow_2.4-py3.8",
        verbose=False,
    ):
        self.verbose = verbose
        self._process_exec_config()
        self._validate_metadata()
        self._metadata["definition_ids"] = []
        self._metadata["training_ids"] = []
        self._metadata["experiment_details"] = None
        self._metadata["experiment_uid"] = None
        self._metadata["experiment_run_details"] = None
        self._metadata["experiment_run_uid"] = None
        self._metadata["compute_configuration"] = compute_configuration
        self._metadata["compute_configuration_node"] = compute_configuration_node
        self._metadata["software_spec"] = software_spec

        # Reset result variables
        self.best_estimator = None
        self.best_score = None
        self.best_estimators = []
        self.best_scores = []
        self.trained_pipeline = None

        LOGGER.info("current metadata: %s", self._metadata)

        # Pickle and store pipeline
        pipeline_dump_file = self._serialize_object(self.pipeline)
        pipeline_dump_dir = os.path.dirname(pipeline_dump_file)

        # Generate execution command
        execution_cmd = self._generate_exec_command()
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
        self.create_cos_bucket_connections()
        training_metadata = {
            self._wml_client.training.ConfigurationMetaNames.NAME: "SROM_WML_EXECUTION",
            self._wml_client.training.ConfigurationMetaNames.SPACE_UID: self._deployment_space_guid,
            self._wml_client.training.ConfigurationMetaNames.DESCRIPTION: "SROM Wml Execution",
            self._wml_client.training.ConfigurationMetaNames.TRAINING_RESULTS_REFERENCE: {
                "connection": {
                    "id": self.output_connection_id,
                },
                "location": {"bucket": self._metadata["result_bucket_name"]},
                "type": "connection_asset",
            },
            self._wml_client.training.ConfigurationMetaNames.MODEL_DEFINITION: {
                "id": definition_id,
                "hardware_spec": {
                    "name": self._metadata["compute_configuration"],
                    "nodes": self._metadata["compute_configuration_node"],
                },
                "software_spec": {"name": self._metadata["software_spec"]},
            },
            self._wml_client.training.ConfigurationMetaNames.TRAINING_DATA_REFERENCES: [
                {
                    "type": "connection_asset",
                    "connection": {
                        "id": self.input_connection_id,
                    },
                    "location": {"bucket": self._metadata["train_bucket_name"]},
                }
            ],
        }
        training = self._wml_client.training.run(training_metadata)
        self._metadata["training_info_df"] = training
        self._metadata["training_ids"] = self._wml_client.training.get_uid(training)

        LOGGER.info(
            "Training Started: Experiment UID is %s. Experiment Run UID is %s.",
            self._metadata["training_ids"],
            self._metadata["training_info_df"],
        )

    def status(self):
        """
        Returns training status dataframe.
        """
        return self._wml_client.training.get_status(self._metadata["training_ids"])[
            "state"
        ]

    def retrieve_logs(self):
        """
        Download and save locally, log from Cloud Object storage for training.
        """
        # Path where logs will be stored
        while self.status() == "pending" or self.status() == "running":
            logging.debug("wml still not completed")
            time.sleep(5)

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
                if (
                    training_name in obj.key
                    and ".txt" in obj.key
                    and "learner" in obj.key
                ):
                    result_path = obj.key

            if len(result_path) > 0:
                file_name = result_path.split("/")[-1]
                bucket_obj.download_file(result_path, file_name)
                print("downloaded at {}".format(file_name))
                LOGGER.info("Downloaded at %s", file_name)
                return file_name
            else:
                return ""

    def display_logs(self, trimmed=False):
        """
        Display logs from Cloud Object storage for training
        models without saving it on local.

        Parameters:
            trimmed(bool, optional): If true, will skip printing
                installation logs.
        """
        while self.status() == "pending" or self.status() == "running":
            logging.debug("wml still not completed")
            time.sleep(5)
        training_id = self._metadata["training_ids"]
        bucket_name = self._wml_client.training.get_details(training_id)["entity"][
            "results_reference"
        ]["location"]["bucket"]
        training_name = self._wml_client.training.get_details(training_id)["entity"][
            "results_reference"
        ]["location"]["logs"]

        bucket_obj = self._cos_resource.Bucket(bucket_name)
        for obj in bucket_obj.objects.iterator():
            if training_name in obj.key and ".txt" in obj.key and "learner" in obj.key:
                output = obj.get("Body")
                out = output["Body"].read().decode("ascii")
                if trimmed:
                    print("*" * 80)
                    if self.__class__.__name__ == "WMLTrainer":
                        skipped_logs = out.split("--- WML EXECUTION ---")
                    else:
                        skipped_logs = out.split("run parameters are: ")
                    # Below condition is necessary as
                    # it might happen that setup is still in progress
                    if len(skipped_logs) > 1:
                        print(skipped_logs[1], end="")
                else:
                    print("*" * 80)
                    print(out, end="")
        print("*" * 80)

    def clean_up(self):
        """
        method for cleaning the training data and model definitions from wml.

        """
        try:
            for training in self._metadata["training_ids"]:
                self._wml_client.training.cancel(training)
        except Exception:
            pass
        for def_id in self._metadata["definition_ids"]:
            self._wml_client.model_definitions.delete(def_id)
        self._cos_resource.Bucket(
            self._metadata["train_bucket_name"]
        ).objects.all().delete()
        self._cos_resource.Bucket(self._metadata["train_bucket_name"]).delete()
        self._cos_resource.Bucket(
            self._metadata["result_bucket_name"]
        ).objects.all().delete()
        self._cos_resource.Bucket(self._metadata["result_bucket_name"]).delete()
        LOGGER.info("Clean up successful.")

    def fetch_results(self):
        """
        method to return the file name of results. User can find the returned result file in the COS bucket.
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
                if training_name in obj.key and ".pkl" in obj.key and "output":
                    result_path = obj.key

            if len(result_path) > 0:
                file_name = result_path.split("/")[-1]
                return file_name
            else:
                return ""
        return ""
