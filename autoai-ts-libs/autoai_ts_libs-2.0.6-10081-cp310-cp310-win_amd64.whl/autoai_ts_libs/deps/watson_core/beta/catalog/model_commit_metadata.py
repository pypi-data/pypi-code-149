# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

"""Metadata about a module.
"""
import os
import sys
from dataclasses import dataclass
from typing import List
from uuid import uuid4, UUID

from autoai_ts_libs.deps.watson_core import ModuleBase
from autoai_ts_libs.deps.watson_core.toolkit import alog, error_handler

log = alog.use_channel("MODEL_COMMIT")
error = error_handler.get(log)


# frozen=True because committed models should be immutable
@dataclass(frozen=True)
class ImmutableModelCommit:
    """
    Represents a model that has been saved into a repository.
    repo_path:
        Path to the model archive, relative to the repo root
    name:
        Human readable name of the model. E.g. syntax_izumo_en_stock
    kind:
        "Type" of watson_core module, as in a block, a workflow, or a resource
    feature:
        The ML Feature that this model enables, e.g. syntax, categories, entities, sentiment...
    algorithm:
        The specific ML algorithm used, e.g. BiLSTM, ESA, CNN...
    module_id:
        The unique ID of the watson_core module, used to identify the class that should load the
        archive
    languages:
        The languages supported by the model, for NLP models. (This should probably be more generic)
    library_version:
        The version of the library that the model code lives in, at the time the model was committed.
        This is not the version of watson_core, for NLP models this would be the version of
        watson_nlp.
    uuid:
        The ID for this commit, sort of like a git hash.
    parent_uuid:
        If the model has a parent, this is the ID to the parent model's commit
    """

    repo_path: str
    name: str
    kind: str
    feature: str
    algorithm: str
    module_id: str
    languages: List[str]
    library_version: str
    uuid: UUID
    # Default of None required on optional UUIDs to avoid deserialization barf
    parent_uuid: UUID = None


class ModelCommitMetadata(ImmutableModelCommit):
    """Interface with ImmutableModelCommit"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._deleted = False

    def set_deleted(self, deleted: bool):
        """Sets the deleted flag for this commit"""
        self._deleted = deleted

    @property
    def deleted(self) -> bool:
        """Whether or not this commit has been deleted"""
        return self._deleted

    @classmethod
    def from_loaded_module(
        cls,
        model: ModuleBase,
        name: str,
        parent_uuid: UUID = None,
        languages_supported: List[str] = None,
    ) -> "ModelCommitMetadata":
        """
        NOTE: The return type annotation here uses a forward reference for 3.6
            compatibility.
            CITE: https://www.python.org/dev/peps/pep-0484/#forward-references
        """
        (
            kind,
            feature,
            algorithm,
            repo_path_bit,
            library_version,
        ) = cls._extract_module_data(model)
        new_uuid = uuid4()

        repo_path = os.path.join(repo_path_bit, name + "_@" + str(new_uuid) + ".zip")

        return ModelCommitMetadata(
            name=name,
            repo_path=repo_path,
            module_id=model.MODULE_ID,
            kind=kind,
            feature=feature,
            algorithm=algorithm,
            languages=languages_supported,
            parent_uuid=parent_uuid,
            library_version=library_version,
            uuid=new_uuid,
        )

    @staticmethod
    def _extract_module_data(loaded_model: ModuleBase):
        module_path = loaded_model.__module__
        module_path_list = module_path.split(".")
        if "blocks" in module_path_list:
            kind = _BLOCK_KIND
            kind_idx = module_path_list.index("blocks")
        elif "workflows" in module_path_list:
            kind = _WORKFLOW_KIND
            kind_idx = module_path_list.index("workflows")
        elif "resources" in module_path_list:
            kind = _RESOURCE_KIND
            kind_idx = module_path_list.index("resources")
        else:
            raise ValueError("Not a block, workflow, or resource")

        feature = module_path_list[kind_idx + 1]
        algorithm = module_path_list[kind_idx + 2]
        repo_path_bit = os.path.join(*module_path_list[kind_idx : kind_idx + 3])

        # Get the current version of the python module that supports this model
        base_module = sys.modules.get(module_path.split(".")[0])
        assert base_module is not None, "Failed to find the base module!"
        base_module_version = base_module.lib_config.library_version

        return kind, feature, algorithm, repo_path_bit, base_module_version


_BLOCK_KIND = "block"
_WORKFLOW_KIND = "workflow"
_RESOURCE_KIND = "resource"
