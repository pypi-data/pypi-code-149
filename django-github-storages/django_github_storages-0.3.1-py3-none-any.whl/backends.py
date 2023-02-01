import base64
import posixpath
import random

import requests
import simplejson as json

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import Storage

from .utils import get_url


class GitHubStorage(Storage):
    """
    A storage backend that utilizes GitHub for storing files.
    """

    def __init__(self):
        """
        Get all the credentials from the settings.py file and initialize them to global variables.
        """
        self.username = settings.GITHUB_USERNAME
        self.token = settings.GITHUB_ACCESS_TOKEN
        self.target_repo = settings.GITHUB_TARGET_REPO

        try:
            self.media_root = settings.GITHUB_MEDIA_ROOT
        except ImproperlyConfigured:
            self.media_root = None

    def url(self, name):
        return name

    def save(self, name, content, max_length=None):
        """
        Saves the file uploaded from the user side to GitHub.
        """
        path_with_file_name = posixpath.basename(str(name)).split("\\")
        name = path_with_file_name.pop()
        path = path_with_file_name

        return self._save(name, path, content)

    def _save(self, name, path, content):
        """
        Checks for the available file name in the specified GitHub repository.
        If found then calls the upload_file_to_git function.

        Arguments:
            - name -- name of the file
            - path -- path leading to the file
            - content -- content of the file

        Returns:
            Download url of the file from GitHub
        """
        while True:
            if self.exists(name, path):
                name = self.get_available_name(name)
            else:
                break

        response = self.upload_file_to_git(name, path, content)

        return response["content"]["download_url"]

    def exists(self, name, path):
        """
        Checks if the file exists in the specified GitHub repository.

        Arguments:
            - name -- name of the file
            - path -- path leading to the file

        Returns:
            True if file exists.
            False if file doesn't exist.
        """
        fetch_url = get_url(name, path, self.media_root)
        response = requests.get(fetch_url)

        return response.status_code == 200

    def get_available_name(self, name, max_length=None):
        random_hash = random.random() * 1000
        name = str(int(random_hash)) + name
        return name

    def upload_file_to_git(self, name, path, content):
        """
        Uploads the file to the specified GitHub repository.

        Arguments:
            - name -- name of the file
            - path -- path leading to the file
            - content -- content of the file

        Raises:
            IOError: If the GitHub API sends a 404 status code. This might happen if the required settings are not configured properly or the GitHub API might not be working properly.

        Returns:
            The content of the file that has been successfully uploaded to GitHub.
        """
        upload_url = get_url(name, path, self.media_root)
        headers = {"Authorization": f"token {self.token}"}
        payload = {
            "message": f"chore: add {name} as media file",
            "committer": {},
        }
        payload["committer"]["name"] = "Monalisa Octocat"
        payload["committer"]["email"] = "octocat@github.com"
        payload["content"] = self.convert_to_base64(content)

        response = requests.put(
            url=upload_url, data=json.dumps(payload), headers=headers
        )

        if response.status_code == 404:
            raise IOError(response.content)
        return json.loads(response.content)

    def convert_to_base64(self, content):
        """
        Encrypts the content of the file before uploading to the specified GitHub repository.

        Arguments:
            content -- the content of the file that will be encrypted.

        Returns:
            The encrypted version of the file.
        """
        return base64.b64encode(content.read())

    def delete(self, name):
        """
        Deletes the file from the specified GitHub repository.

        Arguments:
            name -- name of the file

        Raises:
            IOError: If the GitHub API sends a 404 status code i.e the file couldn't be found. This might happen if the required settings are not configured properly or the GitHub API might not be working properly.

        Returns:
            True upon proper deletion of the file.
        """

        image_path = str(self.url(name)).split("/master/")[-1]

        path_with_file_name = image_path.split("/")
        name = path_with_file_name.pop()

        if path_with_file_name[0] == self.media_root:
            del path_with_file_name[0]

        path = path_with_file_name

        delete_url = get_url(name, path, self.media_root)
        headers = {"Authorization": f"token {self.token}"}

        fetch_url = get_url(name, path, self.media_root)
        response = requests.get(fetch_url)

        try:
            json_data = json.loads(response.content)
            sha = json_data["sha"]
        except IOError as error:
            raise IOError(response.content) from error

        delete_url = get_url(name, path, self.media_root)
        headers = {"Authorization": f"token {self.token}"}

        payload = {
            "message": f"chore: remove {name} as media file",
            "committer": {},
        }
        payload["committer"]["name"] = "Monalisa Octocat"
        payload["committer"]["email"] = "octocat@github.com"
        payload["sha"] = sha

        response = requests.delete(
            url=delete_url, data=json.dumps(payload), headers=headers
        )

        if response.status_code == 404:
            raise IOError(response.content)

        return 1

    def size(self, name):
        name = str(name)

        image_path = str(self.url(name)).split("/master/")[-1]
        path_with_file_name = image_path.split("/")
        name = path_with_file_name.pop()

        if path_with_file_name[0] == self.media_root:
            del path_with_file_name[0]

        path = path_with_file_name
        get_size_url = get_url(name, path, self.media_root)
        headers = {"Authorization": f"token {self.token}"}
        response = requests.get(get_size_url, headers)

        if response.status_code == 404:
            raise IOError(response.content)
        json_data = json.loads(response.content)

        return json_data["size"]
