# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Client code for sending requests to artifactory"""
import os
import requests

from . import base
from requests import Response
from typing import List


class ArtifactoryRemote(base.RemoteClient):
    """An implementation of a RemoteClient for Artifactory"""

    def __init__(self, artifactory_url, artifactory_repo, username, password):
        """Initialize an Artifactory remote

        Args:
            artifacts_url:  str
                Base artifactory URL e.g. https://na.artifactory.swg-devops.com/
            artifactory_repo:  str
                Specific artifactory repo e.g. wcp-nlu-team-one-nlp-models-generic-local
            username:  str
                Username (ARTIFACTORY_USERNAME) used for authentication
            password:  str
                Password (ARTIFACTORY_API_KEY) used for authentication
        """
        self.api_base_url = os.path.join(
            artifactory_url, "artifactory", "api", "storage", artifactory_repo
        )
        self.file_io_base_url = os.path.join(
            artifactory_url, "artifactory", artifactory_repo
        )

        self.username = username
        self.password = password

    def list(self, directory) -> List[str]:
        """Return a list of files in directory.
        Ref: https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API#ArtifactoryRESTAPI-FileList

        Args:
            directory:  str
                Directory in Artifactory to list files for

        Returns:
            List[str]
                List of URIs for files in the directory
        """
        url = self.api_base_url + "/" + directory + "/?list"
        response: Response
        try:
            response = requests.get(url, auth=(self.username, self.password))
            if response.status_code == 404:
                # 404s are OK
                return []
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            print("Failed to list files in {}".format(directory))
            try:
                print(exception.read())
            except:
                pass
            raise exception

        files = response.json()["files"]
        return [each_file["uri"].lstrip("/") for each_file in files]

    def upload(self, source_file, destination_path) -> None:
        """Push a single file source file to a remote destination
        Ref: https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifact

        Args:
            source_file: str
                File to upload
            destination_path: str
                Path in the Artifactory repo to upload file to
                e.g. blocks/categories/test.zip
        """
        url = self.file_io_base_url + "/" + destination_path
        response: Response
        try:
            with open(source_file, mode="rb") as file:
                response = requests.put(
                    url, data=file, auth=(self.username, self.password)
                )
            response.raise_for_status()
        except requests.exceptions.HTTPError as exception:
            print("Failed to upload file {}".format(source_file))
            try:
                print(exception.read())
            except:
                pass
            raise exception

    def download(self, source_path, destination_path) -> None:
        """Pull a single file from a remote destination to a local path

        Args:
            source_path: str
                Path in the Artifactory repo to the file that will be downloaded
                e.g. blocks/categories/test.zip
            destination_path: str
                Path to download file to
        """
        url = self.file_io_base_url + "/" + source_path
        try:
            response = requests.get(
                url, auth=(self.username, self.password), stream=True
            )
            response.raise_for_status()
            file_path = ArtifactoryRemote._download_chunks(response, destination_path)
        except requests.exceptions.HTTPError as exception:
            print("Failed to download file {}".format(source_path))
            try:
                print(exception.read())
            except:
                pass
            raise exception

        assert file_path == destination_path

    @staticmethod
    def _download_chunks(response, destination_path, chunk_size=1000000):
        """Pull a single file from a remote destination to a local path

        Args:
            response: requests.Response
                Response object from an Artifactory call
            destination_path: str
                Path to download file to
        """
        # write to .zip file in chunks to then be extracted
        # we use chunks so that we don't run into broken pipe, memory limits, etc. errors when
        #     downloading very large models
        buffered_response = response.raw
        try:
            with open(destination_path, mode="wb") as fh:
                while True:
                    chunk = buffered_response.read(chunk_size)
                    if not chunk:
                        break
                    fh.write(chunk)
        finally:
            buffered_response.close()

        return destination_path
