# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""Implements functionality to deploy and score a model over WML environment"""

import gzip
import logging
import os
import re
from autoai_ts_libs.deps.srom.utils.file_utils import is_gzip
import uuid

# import warnings
import zipfile
import gzip

# import json
# from pprint import pprint

from retrying import retry
import sys
from autoai_ts_libs.deps.srom.utils import piputils

import logging

LOGGER = logging.getLogger(__name__)


try:
    from ibm_watson_machine_learning.client import APIClient
except ImportError:
    LOGGER.error("ImportError : ibm_watson_machine_learning is not installed ")
    pass
    


LOGGER = logging.getLogger(__name__)

# CONSTANTS

_PYTHONMAJOR = sys.version_info.major
_PYTHONMINOR = sys.version_info.minor

if _PYTHONMAJOR == 3:
    if _PYTHONMINOR == 7:
        PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}_opence"
    elif _PYTHONMINOR == 8:
        PYTHON_SPEC = f"default_py{_PYTHONMAJOR}.{_PYTHONMINOR}"
    elif _PYTHONMINOR == 9:
        PYTHON_SPEC = f"runtime-22.1-py{_PYTHONMAJOR}.{_PYTHONMINOR}"
    else:
        raise Exception('Invalid Python version. Only Python 3.9 is supported')
else: 
    raise Exception('Invalid Python version. Only Python 3.9 is supported')

    
PYTHON = "python"

class WMLScorer:
    """
    Contains functionality to deploy and score a model over WML environment.
    """

    def __init__(self):
        self._wml_client = None
        self._deployment_space_guid = None
        self._package_extension_uids = []
        self._software_spec_uid = None
        self._deployment_details = None
        self._model_details = None
        LOGGER.setLevel(logging.INFO)

    @retry(stop_max_attempt_number=3)
    def connect(self, wml_credentials, deployment_space_name: str):
        """Creates connection for the WML service and performs some other internal bookeeping operations.

        Arguments:
            wml_credentials {dict} -- WML instance credentials
            deployment_space_name {str} -- WML Scoring deployment space name
        """
        self.__init__()

        try:
            self._wml_client = APIClient(wml_credentials)
            self._deployment_space_guid = WMLScorer._guid_from_space_name(
                client=self._wml_client, space_name=deployment_space_name
            )
            self._wml_client.set.default_space(self._deployment_space_guid)

            LOGGER.info("Connected successfully.")
        except Exception as e:
            LOGGER.exception(e)
            print(
                "Could not establish connection, check credentials and deployment space name."
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

        # must not be directory
        # must exist
        # must be a zip or gzip
        if (
            not os.path.isfile(archive_path)
            or not os.path.exists(archive_path)
            or (not zipfile.is_zipfile(archive_path) and not is_gzip(archive_path) and not archive_path.lower().endswith('yaml'))
        ):
            raise Exception(
                """{} is either a directory, missing, or not a valid zip archive or a yaml file name.""".format(
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
        self,
        package_name,
        version,
        extra_index_url=None,
        pip_access_key=None,
        source_only=False,
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
            source_only (bool, False): if True will use the pip --download option --no-binary ":all:".
             This is useful if you're deploying from a machine with different architecture as the
             WML target container (such as from your Mac, for example).
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
            source_only=source_only,
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
            # self._wml_client.software_specifications.ConfigurationMetaNames.PACKAGE_EXTENSIONS: self._package_extension_uids,
            # self._wml_client.software_specifications.ConfigurationMetaNames.TYPE:
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

    def wml_client(self) -> APIClient:
        """returns a reference to the active wml client

        Returns:
            APIClient -- client instance
        """
        return self._wml_client

    def clear_local_packages(self):
        """clears all local packages from deployment libraries"""
        self._package_extension_uids = []

    def deploy_function(
        self,
        function_obj: object,
        function_name: str,
        function_description: str = " ",
        software_spec=PYTHON_SPEC,
        function_type=PYTHON,
    ):
        """
         Deploys a python function in WML runtime

        Arguments:
            function_obj {object} -- The actual function to be deployed
            function_name {string} -- Name of the function
            function_description {string} -- Description of the function. The default is a blank string

        Returns:
             dict -- the JSON representing the metadata of the function
             dict -- the JSON representing the metadata of the deployed unction

        """

        if not self._software_spec_uid:
            self._software_spec_uid = self._wml_client.software_specifications.get_uid_by_name(
                software_spec
            )

        function_props = {
            self._wml_client.repository.FunctionMetaNames.NAME: function_name,
            self._wml_client.repository.FunctionMetaNames.DESCRIPTION: function_description,
            self._wml_client.repository.FunctionMetaNames.TYPE: function_type,
            self._wml_client.repository.FunctionMetaNames.SOFTWARE_SPEC_ID: self._software_spec_uid,
        }
        published_function = self._wml_client.repository.store_function(
            function=function_obj, meta_props=function_props
        )
        # LOGGER.info('Published function ', published_function)
        published_function_uid = self._wml_client.repository.get_function_id(
            published_function
        )
        # LOGGER.info('Published function UID = ', published_function_uid)
        metadata = {
            self._wml_client.deployments.ConfigurationMetaNames.NAME: function_name,
            self._wml_client.deployments.ConfigurationMetaNames.NAME: function_description,
            self._wml_client.deployments.ConfigurationMetaNames.ONLINE: {},
        }
        deployed_function_details = self._wml_client.deployments.create(
            published_function_uid, meta_props=metadata
        )
        return published_function, deployed_function_details

    def deploy_model(
        self,
        model_object: object,
        model_name: str,
        model_type: str = "scikit-learn_0.23",
        model_description: str = " ",
        randomize_name: bool = False,
        software_spec_name="default software spec name",
        software_spec_description="default software spec description",
        software_spec_type=PYTHON_SPEC,
        list_existing=True,
        training_data=None,
        training_target=None,
        feature_names=None,
        label_column_names=None,
        batch=False,
        hardware_spec={},
    ):
        """All in one shot deployment of packages added via add_local_packages plus the model.

        Arguments:
            model_object {object} -- A model (typically an estimator)
            model_name {str} -- an name for the deployment.
            model_description {str} -- a description for the deployment. If nothing is provided a string blank string will be used
            model_type {str} -- model type is a set of pre-defined strings indicating the library the model is based on. Refer to the WML decumentation for prescribed values. Default is scikit-learn_0.23
            randomize_name {bool} -- if true all runtime, deployment, and model names will have a randomzied component

        Returns:
            dict of model details -- a dictionary of model related metadata as returned from WML
            dict of deployment details -- a dictionary of deployment related metadata after successfully deploying the model in WML
        """

        # wml seems to be sensitive (but not clear about)
        # non-alphanumeric characters
        try:

            if list_existing:
                print("********EXISTING DEPLOYMENTS*************")
                self.wml_client().deployments.list()
                print("********EXISTING MODELS*************")
                self.wml_client().repository.list_models()

            self._add_software_specification(
                software_spec_name, software_spec_description, software_spec_type
            )

            model_name = WMLScorer._nonalphafixer(model_name)
            # first add the libraries
            # library_uids = []
            # client = self._wml_client
            random_name_component = uuid.uuid4().hex if randomize_name else ""

            if not self._software_spec_uid:
                self._software_spec_uid = self._wml_client.software_specifications.get_uid_by_name(
                    software_spec_type
                )

            print("Software Spec UID: ", self._software_spec_uid)
            model_props = {
                self._wml_client.repository.ModelMetaNames.NAME: model_name
                + random_name_component,
                self._wml_client.repository.ModelMetaNames.DESCRIPTION: model_description,
                self._wml_client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: self._software_spec_uid,
                self._wml_client.repository.ModelMetaNames.TYPE: model_type,
            }
            self._model_details = self._wml_client.repository.store_model(
                model=model_object,
                meta_props=model_props,
                training_data=training_data,
                training_target=training_target,
                feature_names=feature_names,
                label_column_names=label_column_names,
            )
            model_uid = self._wml_client.repository.get_model_uid(self._model_details)

            LOGGER.info("Stored Model Details = %s", self._model_details)
            LOGGER.info("Stored Model UID = %s", model_uid)

            if batch:
                deployment_props = {
                    self._wml_client.deployments.ConfigurationMetaNames.NAME: model_name
                    + random_name_component,
                    self._wml_client.deployments.ConfigurationMetaNames.BATCH: {},
                    self._wml_client.deployments.ConfigurationMetaNames.HARDWARE_SPEC: hardware_spec,
                }
            else:
                deployment_props = {
                    self._wml_client.deployments.ConfigurationMetaNames.NAME: model_name
                    + random_name_component,
                    self._wml_client.deployments.ConfigurationMetaNames.ONLINE: {},
                }

            self._deployment_details = self._wml_client.deployments.create(
                artifact_uid=model_uid, meta_props=deployment_props, asynchronous=False
            )
            LOGGER.info("Deployment details: %s", self._deployment_details)
            # LOGGER.info(
            #    "Deployment UID: %s",
            #   self._wml_client.deployments.get_uid(self._deployment_details),
            # )
            return self._model_details, self._deployment_details
        except Exception as ex:
            LOGGER.exception(ex)
            return None, None

    def delete_deployments(self, regex_pattern: str, use_simple_wildcards: bool = True):
        """delete deployments matching a regular expression
        Arguments:
            regex_pattern {str} -- a valid regular expression pattern (e.g., 'mymodel.*')
            use_simple_wildcards {bool} -- if True (the default) behavior will similar to posix filesystem
             wildcard matching and will not adhere strictly to regular expression matching rules.
        Returns:
           {int} -- the number of items deleted
        """
        return WMLScorer._delete_stuff(
            self._wml_client.deployments.get_details(),
            self._wml_client.deployments.delete,
            pattern=regex_pattern,
            use_simple_wildcards=use_simple_wildcards,
        )

    def delete_models(
        self, regexp_pattern, use_simple_wildcards: bool = True, limit=100
    ):
        """delete models matching a regular expression
        Arguments:
            regex_pattern {str} -- a valid regular expression pattern (e.g., 'mymodel.*')
            use_simple_wildcards {bool} -- if True (the default) behavior will similar to posix filesystem
             wildcard matching and will not adhere strictly to regular expression matching rules.
        Returns:
           {int} -- the number of items deleted
        """
        return WMLScorer._delete_stuff(
            self._wml_client.repository.get_model_details(),
            self._wml_client.repository.delete,
            pattern=regexp_pattern,
            use_simple_wildcards=use_simple_wildcards,
        )

    def score(self, deployment_details: dict, payload: dict) -> dict:
        """
        Scores on deployed model.
        Args:
            deployment_details (dict, required): the meta data associated with the deployed endpoint (as returned by the call 'deploy')
            payload (dict, required): Data for scoring
        """

        scoring_payload = {
            self._wml_client.deployments.ScoringMetaNames.INPUT_DATA: [payload]
        }
        predictions = self._wml_client.deployments.score(
            deployment_details["metadata"]["id"], scoring_payload
        )

        return predictions

    # ###################### PRIVATE METHODS #############################

    # pylint: disable=not-callable
    @classmethod
    def _delete_stuff(cls, details, deletefn, pattern: str, use_simple_wildcards):

        if not use_simple_wildcards:
            thepattern = pattern  # strict regexp
        else:
            # if someone asked for wildcard, maintain honor it
            if pattern.find(".*") >= 0 or pattern.find("*") >= 0:
                thepattern = pattern
            else:
                thepattern = f"\\b{pattern}\\b"

        repattern = re.compile(thepattern)
        runtime_details = details
        answer = 0
        try:
            for adict in runtime_details["resources"]:
                metadata = adict["metadata"]
                name = metadata["name"]
                if repattern.search(name):
                    deletefn(metadata["id"])
                    print("deleted:", name)
                    answer += 1
        except KeyError as e:
            LOGGER.exception(e)
            print(details)
        return answer

    @classmethod
    def _guid_from_space_name(cls, client, space_name):
        space = client.spaces.get_details()
        return next(
            item for item in space["resources"] if item["entity"]["name"] == space_name
        )["metadata"]["id"]

    @classmethod
    def _nonalphafixer(cls, astring: str) -> str:
        answer = astring
        nonalpha = re.compile("[^0-9a-zA-Z]+")
        if nonalpha.search(astring):
            print("Warn: fixing name with non-alphanumeric characters")
            answer = nonalpha.sub("_", astring)
            # see https://github.ibm.com/NGP-TWC/ml-planning/issues/14998#issuecomment-20075254
            answer += "_"  # don't ask
            print("Warn: name is now {}".format(answer))
        return answer
