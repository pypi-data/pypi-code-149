# *****************************************************************#
# (C) Copyright IBM Corporation 2022.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#

from autoai_ts_libs.deps.watson_core.toolkit import alog
from ...toolkit.errors import error_handler
from . import model


log = alog.use_channel("CFGGBSWFL")
error = error_handler.get(log)


class WorkflowCatalog(model.ModelCatalog):
    """WorkflowCatalog is identical to model catalog in methods, filters. All modules are located
    under /workflows instead of /blocks.
    """

    def get_workflows(self, username=None, password=None):
        """Get a dict of all known models supported in this library version. Queries Artifactory,
        requires credentials, and may take a bit to run depending on connection speed. Also,
        retrieves aliased models.

        Note:
            Alias rule/logic: `<block_type>_<block_shortname>-workflow_<language>_<description>`
            And aliases always map to full-length model name paths.

        Args:
            username:  str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password:  str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY

        Returns:
            WorkflowCatalog
                New instance of WorkflowCatalog with all download-able models.
        """
        all_workflow_models = self._get_all_artifacts("workflows", username, password)
        # models in artifactory are always stored as full model names, and many times there are
        #     broken & invalid models up there, so we need to create aliases from the full names
        #     and filter out those invalid models before returning to users a model catalog
        all_models = self.alias_filter_models(all_workflow_models)
        return WorkflowCatalog(all_models, self.library_version, self.artifact_path)

    def get_alias_models(self, username=None, password=None):
        """Get a dict of all aliased workflows supported in this library version. Queries Artifactory,
        requires credentials, and may take a bit to run depending on connection speed.

        Note:
            Alias rule/logic: `<block_type>_<block_shortname>-workflow_<language>_<description>`
            And aliases always map to full-length model name paths.

        Args:
            username:  str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password:  str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY

        Returns:
            WorkflowCatalog
                New instance of WorkflowCatalog with all latest download-able workflows.
        """
        return self.get_workflows(username, password).filter_non_aliased()

    def filter_non_aliased(self):
        """Filter model catalog to only return aliased models.

        Returns:
            WorkflowCatalog
                New instance of WorkflowCatalog with models in accordance with the filter.
        """
        # model name being separated by three underscores means it's a short name
        models = {
            model_name: model_path
            for model_name, model_path in self.items()
            if len(model_name.split("_")) == 4
        }
        return WorkflowCatalog(models, self.library_version, self.artifact_path)

    def filter_non_latest(self):
        """Filter model catalog to only return latest, full-name models.

        Returns:
            WorkflowCatalog
                New instance of WorkflowCatalog with models in accordance with the filter.
        """
        return WorkflowCatalog(
            self._filter_non_latest(self.filter_non_aliased()),
            self.library_version,
            self.artifact_path,
        )

    def get_latest_models(self, username=None, password=None):
        """Get a dict of all latest workflows supported in this library version. Queries Artifactory,
        requires credentials, and may take a bit to run depending on connection speed. Does NOT
        return alias, returns full length model name paths.

        Args:
            username:  str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password:  str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY

        Returns:
            WorkflowCatalog
                New instance of WorkflowCatalog with all latest download-able workflows.
        """
        return self.get_workflows(username, password).filter_non_latest()
