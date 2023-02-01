import os
from pathlib import Path
from typing import Dict, Union, Iterable, Tuple, Optional

from azure.ai.ml.entities._assets.environment import BuildContext, Environment
from azure.ai.ml.entities._builders import BaseNode
from azure.ai.ml._utils._arm_id_utils import parse_prefixed_name_version

from azure.core.exceptions import AzureError

from ._utils import dump_yaml

class EnvironmentResolver:
    def get_environment_artifacts(
        self,
        job: BaseNode,
        # environment_operations: EnvironmentOperations,
        # download_path: str,
    ) -> Iterable[str]:
        """Validates and returns artifacts from environment specification.

        :param job: job to validate
        :type job: BaseNode entity
        :return: (base_image, conda_file_path, conda_file_contents, build_directory, dockerfile_contents) - Either base_image or build_directory should be None.
        :type return: Iterable[str]
        """
        # remote environment is not supported(besides curated environment)
        # if self._environment_contains_cloud_artifacts(environment=job._component.environment): 
        #     name, version = self._parse_environment_name_version(job._component.environment)
        #     environment_asset = environment_operations.get(name=name, version=version)
        #     if self._is_microsoft_curated_environment(environment_asset):
        #         raise AzureError(message=f"Currently can't support building curated environment images in pipeline local run. Environment: {environment_asset}")
        #     if not self._cloud_environment_is_valid(environment=environment_asset):
        #         raise AzureError(
        #             message="Cloud environment must have environment.image "
        #             + "or the environment.build.path set to work for local endpoints.",
        #         )
        #     return self._get_cloud_environment_artifacts(
        #         environment_operations=environment_operations,
        #         environment_asset=environment_asset,
        #         download_path=download_path,
        #     )
        if not self._local_environment_is_valid(environment=job._component.environment):
            raise AzureError(message=f"Local job run only support local artifacts. Job {job.name} did not contain required local artifact environment.image or environment.build.path.")
        return self._get_local_environment_artifacts(job._component.base_path, job._component.environment)

    # def _get_cloud_environment_artifacts(
    #     self,
    #     environment_operations: EnvironmentOperations,
    #     environment_asset: Environment,
    #     download_path: str,
    # ) -> Tuple[str, str, str, str]:
    #     """
    #     :return: (base_image, conda_file_path, conda_file_contents, build_directory, dockerfile_contents) - Either base_image or build_directory should be None.
    #     :type return: Iterable[str]
    #     """
    #     if environment_asset.build and environment_asset.build.path and is_url(environment_asset.build.path):
    #         environment_build_directory = download_artifact_from_storage_url(
    #             blob_url=environment_asset.build.path,
    #             destination=download_path,
    #             datastore_operation=environment_operations._datastore_operation,
    #             datastore_name=None,
    #         )
    #         dockerfile_path = Path(environment_build_directory, environment_asset.build.dockerfile_path)
    #         dockerfile_contents = dockerfile_path.read_text()
    #         return (None, None, None, environment_build_directory, dockerfile_contents)
    #     conda_file_contents = (
    #         dump_yaml(environment_asset.conda_file) if environment_asset.conda_file else None
    #     )
    #     return (environment_asset.image, environment_asset.id, conda_file_contents, None, None)

    def _get_local_environment_artifacts(self, base_path: str, environment: Environment):
        """
        :return: (base_image, conda_file_path, conda_file_contents, build_directory, dockerfile_contents) - Either base_image or build_directory should be None.
        :type return: Iterable[str]
        """
        if environment.image:
            conda_file_contents = dump_yaml(environment.conda_file)
            return (environment.image, environment._conda_file_path, conda_file_contents, None, None)

        dockerfile_contents = None
        if environment.build:
            if base_path is None:
                base_path = os.getcwd()
            absolute_build_directory = Path(base_path, environment.build.path).resolve()
            docker_file=environment.build.dockerfile_path
            if docker_file is None:
                # default docker file name
                docker_file = "Dockerfile"
            absolute_dockerfile_path = Path(absolute_build_directory, docker_file).resolve()
            dockerfile_contents = absolute_dockerfile_path.read_text()
            return (None, None, None, str(absolute_build_directory), dockerfile_contents)

    def _environment_contains_cloud_artifacts(self, environment: Union[str, Environment]) -> bool:
        return isinstance(environment, str)
    
    def _is_microsoft_curated_environment(self, environment: Environment) -> bool:
        created_info = environment.creation_context
        return created_info.created_by == "Microsoft"
    
    def _local_environment_is_valid(self, environment: Union[str, Environment]) -> bool:
        return isinstance(environment, Environment) and (
            environment.image
            or (
                environment.build is not None
                and isinstance(environment.build, BuildContext)
                and self._local_build_context_is_valid(environment.build)
            )
        )

    def _local_build_context_is_valid(self, build_context: BuildContext):
        return build_context.path is not None

    def _cloud_environment_is_valid(self, environment: Environment):
        return isinstance(environment, Environment) and (
            environment.image or (environment.build and environment.build.path)
        )
    
    def _parse_environment_name_version(self, environment: str) -> Tuple[str, Optional[str]]:
        name, version = parse_prefixed_name_version(environment)
        if version is None and "@" in name:
            at_splits = name.rsplit("@", 1)
            name=at_splits[0]
            version = at_splits[1]
        return name, version

