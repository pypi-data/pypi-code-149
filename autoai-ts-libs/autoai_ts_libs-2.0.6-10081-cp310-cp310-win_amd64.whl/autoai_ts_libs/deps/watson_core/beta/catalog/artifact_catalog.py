# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

"""Model ArtifactCatalog of the FUUUUTURE.
"""
import os
import tempfile
import zipfile
from typing import Dict, List, Tuple, Set
from uuid import UUID
from anytree import Node, RenderTree, findall
from autoai_ts_libs.deps.watson_core import ModuleBase
from autoai_ts_libs.deps.watson_core.beta.catalog import ModelCommitMetadata
from autoai_ts_libs.deps.watson_core.beta.catalog import Repository
from autoai_ts_libs.deps.watson_core.toolkit import alog, error_handler
import autoai_ts_libs.deps.watson_core

log = alog.use_channel("CATALOG")
error = error_handler.get(log)


class ArtifactCatalog:
    """ArtifactCatalog of all available saved models"""

    def __init__(self, repositories: List[Repository]):
        self._repositories = repositories
        if len([r for r in self._repositories if r.default_repository]) != 1:
            raise ValueError("No default repo")

    # Properties #####################################################################################
    @property
    def repositories(self) -> List[Repository]:
        """Returns the underlying repositories, which expose a lower-level API"""
        return self._repositories

    # API ############################################################################################
    def load(self, model: (str, UUID)) -> ModuleBase:
        """Retrieves a specific model by UUID or searches for the latest version of the model by name.
            Will always fetch commits from remote repositories to check for the latest model.
            Pulls the model archive from a remote repository if needed, extracts to disk, and loads.

        Args:
            model: str or UUID
                Either the model name to search for, or UUID to look up
        Returns:
             ModuleBase:
                The loaded and ready to run model, if one was found.
        """
        if not self.exists(model):
            raise ValueError("Model does not exist")

        if isinstance(model, str):
            model_history, repo = self._find_by_name(model)
            # Could do semantic version checks here too...
            model_metadata = model_history[-1]
        else:
            model_metadata, repo = self._find_by_uuid(model)

        # Make sure model is cached
        self.cache(model)

        # unzip it all
        zip_path = os.path.join(repo.root, model_metadata.repo_path)
        with tempfile.TemporaryDirectory() as tempdir:
            with zipfile.ZipFile(zip_path, "r") as zip_f:
                zip_f.extractall(tempdir)

            loaded_model = watson_core.load(tempdir)

        return loaded_model

    def save(
        self,
        model: ModuleBase,
        languages_supported: List[str],
        parent: ModelCommitMetadata = None,
        model_name: str = None,
    ) -> ModelCommitMetadata:
        """Catalog a new model.

        Will commit the model to a repository, archiving it into a .zip file and readying it to be
        synced to a remote repo if required.

        This is slightly intelligent and will search for a parent for the model by name. Cataloging a
        model with the same name as an existing model will append it to the history for that model.

        Saves the model into the default repository, unless the parent exists on a different one.

        A model name is required, but if one is not given then the same name as the parent is assumed.

        Args:
            model: ModuleBase
                The loaded model to catalog
            languages_supported: List(str)
                The languages supported by this model
            parent: ModelCommitMetadata
                (Optional) the exact model to use as a parent
            model_name: str
                (Optional) The name of the model for the catalog. default=parent.name
        """
        # TODO: repo override for saving in a non-default repo?

        if not parent and not model_name:
            raise ValueError(
                "Either model name or parent is required to catalog a model"
            )

        repo = self._default_repo()
        # Make sure we're up to date with _all repos_
        _ = [r.fetch() for r in self.repositories]

        # Deduce both name and parent from each other
        if not model_name:
            model_name = parent.name
        if not parent:
            parent_history, parent_repo = self._find_by_name(model_name)
            if len(parent_history) > 0:
                # Add this model to the end of the list
                parent = parent_history[-1]
                # Parent could be in a different repo. /shrug just save it there? TODO: think
                repo = parent_repo

        new_model = repo.commit(
            loaded_model=model,
            languages_supported=languages_supported,
            model_name=model_name,
            parent=parent,
        )

        return new_model

    def models(
        self,
        kind: str = None,
        feature: str = None,
        algorithm: str = None,
        language: str = None,
        latest_only: bool = False,
        show_deleted: bool = False,
    ) -> Dict[str, List[ModelCommitMetadata]]:
        """Returns all cataloged models that meet the optional filtering criteria.
        The dictionary is indexed by model name, and each entry is a list of the entire history of
        the model that is currently cataloged.
        """
        models: Dict[str, List[ModelCommitMetadata]] = {}
        # First update all repos to check for any new models
        self._update_all_repos()
        for repo in self.repositories:
            model_uuid_map = repo.commits
            # TODO: this would completely clobber models of the same name in different repos
            # definitely some options to consider here...
            models.update(ArtifactCatalog._build_model_histories(model_uuid_map))

        models = ArtifactCatalog._filter_models(
            models, kind, feature, algorithm, language, show_deleted
        )
        models = {k: v for k, v in models.items() if len(v) > 0}
        return models

    def cached(self, model: (str, UUID)) -> bool:
        """Check if a model is cached locally"""
        if isinstance(model, str):
            model_history, repo = self._find_by_name(model)
            # Check if the latest one is cached
            return os.path.exists(os.path.join(repo.root, model_history[0].repo_path))
        else:
            model, repo = self._find_by_uuid(model)
            return os.path.exists(os.path.join(repo.root, model.repo_path))

    def cache(self, model: (str, UUID)) -> None:
        """Download a model from a remote and cache it locally"""
        if isinstance(model, str):
            model_history, repo = self._find_by_name(model)
            # Could do other things here too..
            # But just cache the "most recent" one by name
            repo.pull(model_history[-1])
        else:
            model, repo = self._find_by_uuid(model)
            repo.pull(model)

    def delete(self, model: (str, UUID)) -> None:
        """Delete a model, referenced by name, commit, or UUID"""
        # TODO: Allow deletion by commit
        if isinstance(model, UUID):
            commit, repo = self._find_by_uuid(model)
            repo.delete(commit)
        elif isinstance(model, str):
            model_history, repo = self._find_by_name(model)
            _ = [repo.delete(commit) for commit in model_history]

    def exists(self, model: (str, UUID)) -> bool:
        """Check for the existence of a model, either by name or ID"""
        if isinstance(model, str):
            model_history, _ = self._find_by_name(model)
            return len([m for m in model_history if not m.deleted]) > 0
        else:
            commit, _ = self._find_by_uuid(model)
            return commit is not None and not commit.deleted

    def print_tree(self) -> None:
        """Print out the tree of cataloged models"""
        catalog_node = Node(name="ArtifactCatalog", model=None)
        for repo in self.repositories:
            # Save the ugliness for the bottom of this file...
            self._add_repository_tree(catalog_node, repo)

        print(RenderTree(catalog_node).by_attr("name"))

    # Private implementations ########################################################################
    def _update_all_repos(self):
        for repo in self.repositories:
            repo.fetch()

    @staticmethod
    def _build_model_histories(
        model_uuid_map: Dict[UUID, ModelCommitMetadata]
    ) -> Dict[str, List[ModelCommitMetadata]]:
        ordered_model_histories_map: Dict[str, List[ModelCommitMetadata]] = {}

        all_names = set(m.name for m in model_uuid_map.values())

        for name in all_names:
            model_history = [m for m in model_uuid_map.values() if m.name == name]
            if len(model_history) == 1:
                ordered_model_histories_map[name] = model_history
            else:
                # Order the list by lineage
                parent_uuids = set(m.parent_uuid for m in model_history)
                reverse_ordered_model_history = []
                while len(model_history) > 0:
                    last_model = [
                        m for m in model_history if m.uuid not in parent_uuids
                    ]
                    assert len(last_model) == 1
                    last_model = last_model[0]
                    reverse_ordered_model_history.append(last_model)
                    model_history.remove(last_model)
                    parent_uuids.remove(last_model.parent_uuid)

                ordered_model_histories_map[name] = list(
                    reversed(reverse_ordered_model_history)
                )

        return ordered_model_histories_map

    @staticmethod
    def _filter_models(
        models: Dict[str, List[ModelCommitMetadata]],
        kind: str = None,
        feature: str = None,
        algorithm: str = None,
        language: str = None,
        show_deleted: bool = False,
    ) -> Dict[str, List[ModelCommitMetadata]]:
        if kind:
            models = {k: v for k, v in models.items() if v[0].kind == kind}
        if feature:
            models = {k: v for k, v in models.items() if v[0].feature == feature}
        if algorithm:
            models = {k: v for k, v in models.items() if v[0].algorithm == algorithm}
        if language:
            models = {k: v for k, v in models.items() if language in v[0].languages}
        if not show_deleted:
            models = {
                k: [commit for commit in v if not commit.deleted]
                for k, v in models.items()
            }
        return models

    def _find_by_name(self, name: str) -> Tuple[List[ModelCommitMetadata], Repository]:
        # Include all deleted commits in here as well, so we can reason about full histories.
        # Then we'll filter later based on what the caller wants.
        all_models_by_name = self.models(show_deleted=True)
        if name in all_models_by_name:
            # heh...
            repo = [
                r
                for r in self.repositories
                if all_models_by_name[name][0].uuid in r.commits
            ][0]
            return all_models_by_name[name], repo
        else:
            return [], None

    def _find_by_uuid(self, uuid: UUID) -> Tuple[ModelCommitMetadata, Repository]:
        # no fetch in private interface, do it once at public call
        # self._update_all_repos()
        for repo in self.repositories:
            if uuid in repo.commits:
                return repo.commits[uuid], repo
        return None, None

    def _default_repo(self) -> Repository:
        return [r for r in self.repositories if r.default_repository][0]

    def _add_repository_tree(self, catalog_node: Node, repo: Repository):
        """ðŸŒ¶ï¸ðŸŒ¶ï¸ðŸŒ¶ï¸"""
        repo_node = Node(
            name=repo.name + "(" + repo.nickname + ")", model=None, parent=catalog_node
        )
        repo_models = repo.commits
        for kind in {m.kind for m in repo_models.values()}:
            kind_models = {uuid: m for uuid, m in repo_models.items() if m.kind == kind}
            kind_node = Node(name=kind, parent=repo_node, model=None)
            for feature in {m.feature for m in kind_models.values()}:
                feature_models = {
                    uuid: m for uuid, m in kind_models.items() if m.feature == feature
                }
                feature_node = Node(name=feature, parent=kind_node, model=None)
                for algo in {m.algorithm for m in feature_models.values()}:
                    algo_models = {
                        uuid: m
                        for uuid, m in feature_models.items()
                        if m.algorithm == algo
                    }
                    algo_node = Node(name=algo, parent=feature_node, model=None)

                    # Now to the actual models...
                    # There should be >0 models with no parents here
                    # So make some nodes for these and set their parents to the algorithm node
                    for model in algo_models.values():
                        model: ModelCommitMetadata
                        if model.parent_uuid is None:
                            self._create_node(model, algo_node)

        # Now we at least have a tree with all the "root" models
        # So we can lazily add all the other models based on parent uuid
        uuids_in_tree = ArtifactCatalog._uuids_in_tree(repo_node)
        repo_models = {
            uuid: model
            for uuid, model in repo_models.items()
            if model.uuid not in uuids_in_tree
        }
        while len(repo_models) > 0:
            for model in repo_models.values():
                if model.parent_uuid in uuids_in_tree:
                    parent_node = findall(
                        repo_node,
                        filter_=lambda x: x.model is not None
                        and x.model.uuid == model.parent_uuid,
                    )[0]
                    self._create_node(model, parent_node)

            uuids_in_tree = ArtifactCatalog._uuids_in_tree(repo_node)
            repo_models = {
                uuid: m
                for uuid, m in repo_models.items()
                if m.uuid not in uuids_in_tree
            }

    @staticmethod
    def _uuids_in_tree(node: Node) -> Set[UUID]:
        # Node has a `model` attribute which is either None or a ModelCommitMetadata
        all_model_nodes = findall(node, filter_=lambda x: x.model is not None)
        return {n.model.uuid for n in all_model_nodes}

    def _create_node(self, commit: ModelCommitMetadata, parent: Node):
        # D-4 is a dirty hack for model version.
        version = parent.depth - 4
        cached = self.cached(commit.uuid)

        if cached:
            color_code = "\u001b[32m"
        else:
            color_code = "\u001b[31m"

        reset_code = "\u001b[0m"

        name_str = "{}{} (v{}){}".format(color_code, commit.name, version, reset_code)

        Node(name=name_str, parent=parent, model=commit)
