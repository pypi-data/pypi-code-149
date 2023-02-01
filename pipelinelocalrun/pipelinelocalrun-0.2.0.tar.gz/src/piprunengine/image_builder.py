from genericpath import exists
import hashlib
import logging
from typing import Dict, Union
from pathlib import Path

import docker
from docker import DockerClient
from docker.errors import ImageNotFound, APIError
from azure.core.exceptions import AzureError

from azure.ai.ml import MLClient
# from azure.ai.ml.constants._common import AzureMLResourceType
# from azure.ai.ml.operations._environment_operations import EnvironmentOperations
from azure.ai.ml.entities import CommandComponent, Environment
from azure.ai.ml.entities._builders import BaseNode

from .environment_resolver import EnvironmentResolver
from .dockerfile_resolver import DockerfileResolver
from .constants import ENV_CURATED_IMAGE_PREFIX, MCR_CURATED_IMAGE_PREFIX, CONDA_FILE_NAME
from .logger import get_logger

AZURE_ENV_PATH="/azureml-envs/inf-conda-env"

class LocalImageBuildError(Exception):
    def __init__(self, error: Union[str, Exception]):
        err = f"Building the local image failed with error: {str(error)}"
        super().__init__(err)

class LocalImageBuilder(object):
    """
    """
    def __init__(self, ml_client: MLClient, log_path: str) -> None:
        self._environment_resolver = EnvironmentResolver()
        self._ml_client = ml_client
        self._docker_client: DockerClient = docker.from_env()
        self._logger = get_logger("image-builder", log_path=log_path, std_out=True)

    def _get_build_directory(self, pipeline_name: str, job_name: str) -> Path:
        return Path(Path.home(), ".azureml", "pipeline", pipeline_name, job_name)
    
    def build_container_image(self, pipeline_name: str, job: BaseNode):
        """build job docker container image based on environment info in job component.
        
        :return local docker container image name
        """
        if not isinstance(job._component, CommandComponent):
            raise AzureError(message="local job image build only support command component.")
        environment=job._component.environment
        if self._environment_resolver._environment_contains_cloud_artifacts(environment):
            name, version = self._environment_resolver._parse_environment_name_version(job._component.environment)
            if not name.lower().startswith(ENV_CURATED_IMAGE_PREFIX):
                raise AzureError(message="Only azureml curated environments (https://learn.microsoft.com/en-us/azure/machine-learning/resource-curated-environments) are supported in local run mode!")
            image_name = self._pull_curated_image_from_mcr(name, version)
            return image_name, None
        # if only image is provided in environment, return directly
        if isinstance(environment, Environment) and environment.image is not None and environment.conda_file is None:
            return environment.image, None

        # image is related to environment, so use environment_name:environment_version as the local image name
        image_name = self.get_image_name(environment=environment)
        
        try:
            self._docker_client.images.get(image_name)
            self._logger.info(f"image with name {image_name} already exist, skip image building...")
            return image_name, None
        except ImageNotFound:
            pass
        except APIError as e:
            self._logger.error(f"get image with name {image_name} err:{e}")
            raise LocalImageBuildError(e)
        
        download_dir = self._get_build_directory(pipeline_name, job.name)
        download_dir.mkdir(parents=True, exist_ok=True)
        # env_operation: EnvironmentOperations = None
        # if self._ml_client is not None:
        #     env_operation = self._ml_client._operation_container.all_operations.get(AzureMLResourceType.ENVIRONMENT)
        download_path = str(download_dir.resolve())
        (
            yaml_base_image_name,
            yaml_env_conda_file_path,
            yaml_env_conda_file_contents,
            downloaded_build_context,
            yaml_dockerfile,
        ) = self._environment_resolver.get_environment_artifacts(job)
        # code_directory_path = Path(job._component.base_path, job._component.code)

        if yaml_env_conda_file_contents:
            self._write_conda_file(
                conda_contents=yaml_env_conda_file_contents,
                directory_path=download_path,
                conda_file_name=CONDA_FILE_NAME,
            )
            dockerfile = DockerfileResolver(
                dockerfile=yaml_dockerfile,
                docker_base_image=yaml_base_image_name,
                docker_azureml_env_path=AZURE_ENV_PATH,
                docker_conda_file_name=CONDA_FILE_NAME,
            )
        else:
            dockerfile = DockerfileResolver(
                dockerfile=yaml_dockerfile,
                docker_base_image=yaml_base_image_name,
                docker_azureml_env_path=AZURE_ENV_PATH,
                docker_conda_file_name=None,
            )
        build_directory = downloaded_build_context if downloaded_build_context else download_path
        dockerfile.write_file(directory_path=build_directory)
        # user_environment_variables = job._component.environment_variables
        self._logger.debug(f"Start building local image: [{image_name}]")
        self._logger.debug(f"Build directory: {build_directory}")
        self._logger.debug(f"Dockerfile path: {dockerfile.local_path}")
        # docker client build container
        self._build_image(build_directory=build_directory, image_name=image_name, dockerfile_path=dockerfile.local_path)
        return image_name, str(dockerfile)
    
    def _build_image(
        self,
        build_directory: str,
        image_name: str,
        dockerfile_path: str,
    ) -> None:
        try:
            self._logger.info(f"Start building docker image {image_name} from Dockerfile: {dockerfile_path}")
            self._logger.info(f"----------------------------------------[{image_name} build start]----------------------------------------")
            for status in self._docker_client.api.build(
                path=build_directory, tag=image_name, dockerfile=dockerfile_path, pull=True, decode=True, quiet=False, buildargs={"ENV": "local"}
            ):
                if "stream" in status:
                    if "An unexpected error has occurred. Conda has prepared the above report." in status["stream"]:
                        raise LocalImageBuildError(f"Issue creating conda environment:\n{status['stream']}")
                    content:str = status["stream"]
                    f = content.strip('\n\r')
                    if len(f) > 0:
                        self._logger.info(f)
                if "error" in status:
                    self._logger.info(status["error"])
                    raise Exception(status["error"])
            self._logger.info(f"----------------------------------------[{image_name} build finish]----------------------------------------")
        except APIError as e:
            raise LocalImageBuildError(e)
        except Exception as e:
            if isinstance(e, LocalImageBuildError):
                raise
            raise LocalImageBuildError(e)

    def _pull_curated_image_from_mcr(self, name: str, version: str):
        if name.lower().startswith(ENV_CURATED_IMAGE_PREFIX):
            name = name[len(ENV_CURATED_IMAGE_PREFIX):]
        if version is None:
            version = "latest"
        image_name = MCR_CURATED_IMAGE_PREFIX + name
        image_with_exact_version = image_name + ":" + version
        # check image exist or not
        exist = self._is_image_exist(image_with_exact_version)
        if exist:
            return image_with_exact_version

        # using exact tag to pull image
        try:
            self._docker_client.images.pull(image_name, tag=version)
            return image_with_exact_version
        except APIError as e:
            self._logger.info(f"image with name {image_name} and tag {version} not found!")
            if version != "latest":
                self._logger.info(f"fall back to using latest tag for image {image_name}!")
                pass
            else:
                raise e

        # try using latest tag to pull image
        try:
            self._docker_client.images.pull(image_name)
            return f"{image_name}:latest"
        except APIError as e:
            self._logger.error(f"pull image with name {image_name} failed! err:{e}")
            raise e

    def _write_conda_file(self, conda_contents: str, directory_path: str, conda_file_name: str):
        """Writes out conda file to provided directory

        :param conda_contents: contents of conda yaml file provided by user
        :type conda_contents: str
        :param directory_path: directory on user's local system to write conda file
        :type directory_path: str
        """
        conda_file_path = f"{directory_path}/{conda_file_name}"
        p = Path(conda_file_path)
        p.write_text(conda_contents)

    def get_image_name(self, environment: Union[str, Environment]):
        # TODO: using md5 from environment content should be better to avoid conflict
        if isinstance(environment, Environment):
            return f"{environment.name.lower()}:{environment.version}"
        # for string format environment, should we respect the verstion tag?
        return get_md5_string(environment)

    def _is_image_exist(self, image_name:str) -> bool:
        try:
            self._docker_client.images.get(image_name)
            self._logger.info(f"image with name {image_name} already exist, skip image building...")
            return True
        except ImageNotFound:
            pass
        except APIError as e:
            self._logger.error(f"get image with name {image_name} err:{e}")
        return False

def get_md5_string(text):
    try:
        return hashlib.md5(text.encode("utf8")).hexdigest()
    except Exception as ex:
        raise ex
