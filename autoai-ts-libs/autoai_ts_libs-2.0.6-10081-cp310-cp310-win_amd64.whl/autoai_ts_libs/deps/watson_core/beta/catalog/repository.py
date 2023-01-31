# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""This contains the Repository class that stores models locally and mirrors to remotes."""
import os
import tempfile
import zipfile
from typing import Dict, List
from uuid import UUID

import jsons

from autoai_ts_libs.deps.watson_core import ModuleBase
from autoai_ts_libs.deps.watson_core.beta.catalog import ImmutableModelCommit, ModelCommitMetadata
from autoai_ts_libs.deps.watson_core.beta.remotes import RemoteClient
from autoai_ts_libs.deps.watson_core.toolkit import alog, fileio

log = alog.use_channel("REPOSITORY")

# TODO: all the error handling


class Repository:
    """A git-like Repository for saving immutable records of model history.
    Attaches to a remote file system for github-like push/pull semantics. (If you squint hard enough)
    """

    _COMMITS = ".models"
    _DELETED = ".deleted"

    def __init__(
        self,
        local_repo_root: str,
        remote_client: RemoteClient,
        nickname: str = "",
        read_only: bool = False,
        default_repository: bool = False,
    ):
        """
        Args:
            local_repo_root: str
                Path to the directory containing this repo
            remote_client: RemoteClient
                The client for the remote
            nickname: str
                A friendly name for the repo
            read_only: bool
                Read only repos cannot be committed to
            default_repository: bool
                Whether a catalog should consider this the default place to commit models to
        """
        # Allow users to configure a repo root relative to ~
        if local_repo_root.startswith("~"):
            if not os.getenv("HOME"):
                raise ValueError(
                    "Unable to use ~ in configured repo root because $HOME is unset"
                )
            local_repo_root = local_repo_root.replace("~", os.getenv("HOME"))
        self._local_root = local_repo_root
        self._remote_client = remote_client
        self._nickname = nickname
        self._read_only = read_only
        self._default_repository = default_repository

        self._commits_folder = os.path.join(self._local_root, Repository._COMMITS)
        self._deletes_folder = os.path.join(self._local_root, Repository._DELETED)

        self._commits: Dict[UUID, ModelCommitMetadata] = {}

        # Name of repo is the name of the directory it lives in
        self._name: str = os.path.split(local_repo_root)[-1]

        # Make the dir structure if nothing exists locally
        self._init_if_bare()

        # Update commits in memory based on local files
        self._initialize_from_commits()

    # API ############################################################################################

    def fetch(self):
        """Fetch any new commits from the remote.
        Like `git fetch`, this does not download the model artifacts, so network overhead should be
        low."""
        remote_commits = self._list_commits_on_remote()
        for commit in remote_commits:
            if commit not in self.commits:
                self._remote_client.download(
                    os.path.join(self._COMMITS, str(commit)),
                    os.path.join(self._commits_folder, str(commit)),
                )

        # Also pull any commit delete records from the remote
        remote_deletes = self._list_deletes_on_remote()
        for commit in remote_deletes:
            # TODO: allow path functions to take UUIDs instead of just commits?
            self._remote_client.download(
                os.path.join(self._DELETED, str(commit)),
                os.path.join(self._deletes_folder, str(commit)),
            )

        # call the init code again to update self._commits
        self._initialize_from_commits()

    def pull(self, commit: ModelCommitMetadata):
        """Pull a model artifact off of the remote, if it does not already exist locally

        Args:
            commit: ModelCommitMetadata
                Downloads the model artifact associated with this commit
        """
        if not os.path.exists(self._absolute_model_path(commit)):
            os.makedirs(
                os.path.split(self._absolute_model_path(commit))[0], exist_ok=True
            )
            self._remote_client.download(
                commit.repo_path, self._absolute_model_path(commit)
            )

    def commit(
        self,
        loaded_model: ModuleBase,
        model_name: str,
        languages_supported: List[str],
        parent: ModelCommitMetadata = None,
    ) -> ModelCommitMetadata:
        """Commit a model to the repository. This creates and persists both a commit record (type
        ModelCommitMetadata) for the model as well as the packaged archive of the model. This does not
        push the commit or model archive to the remote.

        Args:
            loaded_model: ModuleBase
                The model to commit
            model_name: str
                The human-readable name of the model
            languages_supported: List[str]
                The languages supported by the model
            parent: ModelCommitMetadata
                This model's predecessor, if this model is intended to update a previous model

        Returns:
            ModelCommitMetadata
                A unique and immutable "commit record" for this model
        """
        # First do a bunch of checks to make sure we can commit this model
        if self.read_only:
            raise ValueError("Read only repo")

        if parent and parent.uuid not in self.commits:
            raise ValueError("Missing parent in repo")

        same_names = [m for m in self.commits.values() if m.name == model_name]
        if len(same_names) > 0:
            if not parent:
                raise ValueError("Model already exists")
            if parent and any(m.parent_uuid == parent.uuid for m in same_names):
                raise ValueError("Parent already has child with this name")

        if parent:
            parent_uuid = parent.uuid
        else:
            parent_uuid = None

        # Then build the new commit
        metadata = ModelCommitMetadata.from_loaded_module(
            model=loaded_model,
            name=model_name,
            parent_uuid=parent_uuid,
            languages_supported=languages_supported,
        )

        # Check real quick that the parent is the same sort of model as the child
        if parent and (
            parent.kind != metadata.kind
            or parent.feature != metadata.feature
            or parent.algorithm != metadata.algorithm
        ):
            raise ValueError("Cannot have parent of different model type")

        self.commits[metadata.uuid] = metadata
        self._persist_commit(metadata)
        self._zip_model(loaded_model, metadata)
        return metadata

    def push(self) -> None:
        """Pushes all commits and model artifacts that don't yet exist on the remote"""
        remote_commits = self._list_commits_on_remote()
        remote_deletes = self._list_deletes_on_remote()
        for commit in self.commits.values():
            self._push_one(commit, remote_commits, remote_deletes)

    def push_one(self, commit: ModelCommitMetadata) -> None:
        """Pushes one commit to the remote. This pushes both the commit record and the model
        artifact itself, if the commit does not yet exist on the remote.
        Pushing the commit record only is not supported.

        Args:
            commit: ModelCommitMetadata
                The commit to push to the remote
        """
        remote_commits = self._list_commits_on_remote()
        remote_deletes = self._list_deletes_on_remote()
        self._push_one(commit, remote_commits, remote_deletes)

    def clean(self):
        """Delete all locally cached models that exist on the remote"""
        raise NotImplementedError()

    def delete(self, commit: ModelCommitMetadata) -> ModelCommitMetadata:
        """Puts deleted ModelCommitMetadata into a deleted dir"""
        if self.read_only:
            raise ValueError("Read only repo")
        # Delete only in local until otherwise synced with a remote
        # Check if commit exists
        if commit.uuid not in self.commits:
            raise ValueError("Model does not exist!")
        # if it's deleted already, ignore
        if commit.deleted:
            log.info("Model is already deleted!")
        else:
            commit.set_deleted(deleted=True)
            self._persist_delete(commit)
        return commit

    @property
    def commits(self) -> Dict[UUID, ModelCommitMetadata]:
        """Returns all commits in a dictionary by UUID."""
        return self._commits

    @property
    def name(self) -> str:
        """Returns the name of the repository."""
        return self._name

    @property
    def root(self) -> str:
        """Returns the path to the root of the repository on local storage."""
        return self._local_root

    @property
    def nickname(self) -> str:
        """Returns the nickname of the repository."""
        return self._nickname

    @property
    def read_only(self):
        """Returns True if the repository is in read-only mode, otherwise False."""
        return self._read_only

    @property
    def default_repository(self):
        """Returns True if this repository is set as the default repo to write models to, otherwise
        False."""
        return self._default_repository

    # Private functionality ##########################################################################
    def _init_if_bare(self):
        os.makedirs(self._commits_folder, exist_ok=True)
        os.makedirs(self._deletes_folder, exist_ok=True)

    def _initialize_from_commits(self):
        for file in os.listdir(self._commits_folder):
            file_path = os.path.join(self._commits_folder, file)
            if os.path.isfile(file_path):
                commit = self._read_commit(file_path)
                self._commits[commit.uuid] = commit

        for file in os.listdir(self._deletes_folder):
            # Filenames are just the commit UUIDs
            self._commits[UUID(file)].set_deleted(True)

    def _read_commit(self, commit_path) -> ModelCommitMetadata:
        json_commit = fileio.load_txt(commit_path)
        model_metadata = jsons.loads(json_commit, cls=ImmutableModelCommit)
        # Note: we cannot just use **json.dump here since types like UUID would
        # be converted to string
        return ModelCommitMetadata(
            **{
                elem: getattr(model_metadata, elem)
                for elem in ImmutableModelCommit.__dataclass_fields__
            }
        )

    def _persist_commit(self, commit: ModelCommitMetadata) -> None:
        json_commit = jsons.dumps(commit, cls=ImmutableModelCommit, strict=True)
        fileio.save_txt(text=json_commit, filename=self._absolute_commit_path(commit))

    def _persist_delete(self, commit: ModelCommitMetadata) -> None:
        json_delete = jsons.dumps(commit, cls=ImmutableModelCommit, strict=True)
        fileio.save_txt(text=json_delete, filename=self._absolute_delete_path(commit))

    def _push_one(
        self,
        commit: ModelCommitMetadata,
        remote_commits: List[UUID],
        remote_deletes: List[UUID],
    ):
        if commit.uuid not in self.commits:
            raise ValueError("Model not committed to repo")

        if commit.uuid not in remote_commits:
            # TODO: Push/pull and reasoning about what exists on the remote needs to be made
            #  eventually consistent

            # Push the commit file
            self._remote_client.upload(
                self._absolute_commit_path(commit), self._relative_commit_path(commit)
            )
            # Push the model artifact
            self._remote_client.upload(
                self._absolute_model_path(commit), commit.repo_path
            )

        if commit.deleted and commit.uuid not in remote_deletes:
            self._remote_client.upload(
                self._absolute_delete_path(commit), self._relative_delete_path(commit)
            )

    def _absolute_commit_path(self, model: ModelCommitMetadata) -> str:
        return os.path.join(self._commits_folder, str(model.uuid))

    def _absolute_delete_path(self, model: ModelCommitMetadata):
        return os.path.join(self._deletes_folder, str(model.uuid))

    def _relative_commit_path(self, model: ModelCommitMetadata) -> str:
        return os.path.join(self._COMMITS, str(model.uuid))

    def _relative_delete_path(self, model: ModelCommitMetadata) -> str:
        return os.path.join(self._DELETED, str(model.uuid))

    def _absolute_model_path(self, model: ModelCommitMetadata) -> str:
        return os.path.join(self._local_root, model.repo_path)

    def _zip_model(self, model: ModuleBase, metadata: ModelCommitMetadata):
        # Ensure we have a place to save the zip
        path_to_zip = self._absolute_model_path(metadata)
        required_directory = os.path.split(path_to_zip)[0]
        os.makedirs(required_directory, exist_ok=True)

        # Save the model to a directory
        with tempfile.TemporaryDirectory() as tempdir:
            model.save(tempdir)

            # While the files still exist, zip those bad boys up
            with zipfile.ZipFile(
                self._absolute_model_path(metadata), "w", zipfile.ZIP_DEFLATED
            ) as zip_file:
                Repository._zipdir(tempdir, zip_file)

    # Zip up contents of a directory without the parent dir
    # (so there's no high level dir within the zip)
    @staticmethod
    def _zipdir(zip_path, zip_file):
        length = len(zip_path)

        for root, _, files in os.walk(zip_path):
            folder = root[length:]  # zip_path without parent dir
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.join(folder, file))

    def _list_commits_on_remote(self) -> List[UUID]:
        commit_files = self._remote_client.list(Repository._COMMITS)
        return [UUID(filename) for filename in commit_files]

    def _list_deletes_on_remote(self) -> List[UUID]:
        delete_records = self._remote_client.list(Repository._DELETED)
        return [UUID(filename) for filename in delete_records]
