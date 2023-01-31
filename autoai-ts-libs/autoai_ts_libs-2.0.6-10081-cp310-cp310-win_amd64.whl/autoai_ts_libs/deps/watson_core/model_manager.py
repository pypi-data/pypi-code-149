# *****************************************************************#
# (C) Copyright IBM Corporation 2021.                             #
#                                                                 #
# The source code for this program is not published or otherwise  #
# divested of its trade secrets, irrespective of what has been    #
# deposited with the U.S. Copyright Office.                       #
# *****************************************************************#
"""Most logic interacting with remotely uploaded models.  Can load, upload, download, etc.
"""

from io import BytesIO
import os
import tempfile
import zipfile
from typing import Union

import autoai_ts_libs.deps.watson_core
from autoai_ts_libs.deps.watson_core.toolkit import alog, web
from .toolkit.errors import error_handler

from . import module, ModuleBase

log = alog.use_channel("MDLMNG")
error = error_handler.get(log)

# restrict functions that are imported so we don't pollute the base module namespce
__all__ = [
    "BLOCK_REGISTRY",
    "WORKFLOW_REGISTRY",
    "RESOURCE_REGISTRY",
    "MODULE_REGISTRY",
    "get_valid_module_ids",
    "ModelManager",
]

# Define the various registries used by the model manager
BLOCK_REGISTRY = {}  # Block ID -> class registry
WORKFLOW_REGISTRY = {}  # Workflow ID -> class registry
RESOURCE_REGISTRY = {}  # Resource Type ID -> class registry
MODULE_REGISTRY = {}  # Module (block/workflow) ID -> class registry


def get_valid_module_ids():
    """Get a dictionary mapping all module (block and workflow) IDs to the
    string names of the implementing classes.
    """
    return {
        module_id: model_class.__name__
        for module_id, model_class in MODULE_REGISTRY.items()
    }


class ModelManager:
    """Manage the models or resources for library."""

    def __init__(
        self, artifact_path, model_catalog, resource_catalog, workflow_catalog
    ):
        """Initialize ModelManager.

        Args:
            artifact_path:  str
                Path to artifactory where models live (typically from config.yml)
            model_catalog:  ModelCatalog
                Library's instance of catalog for blocks.
            resource_catalog:  ResourceCatalog
                Library's instance of catalog for resources.
            workflow_catalog:  WorkflowCatalog
                Library's instance of catalog for workflows.
        """
        self.artifact_path = artifact_path
        self.model_catalog = model_catalog
        self.resource_catalog = resource_catalog
        self.workflow_catalog = workflow_catalog

        # Map to store module caches, to be used for singleton model lookups
        self.singleton_module_cache = {}

    # make load function available from top-level of library
    def load(self, module_path, load_singleton=False, *args, **kwargs):
        """Load a model and return an instantiated object on which we can run inference.

        Args:
            module_path: str | BytesIO | bytes
                A module path to one of the following.
                    1. A module path to a directory containing a yaml config file in the top level.
                    2. A module path to a zip archive containing either a yaml config file in the
                       top level when extracted, or a directory containing a yaml config file in
                       the top level.
                    3. A BytesIO object corresponding to a zip archive containing either a yaml
                       config file in the top level when extracted, or a directory containing a
                       yaml config file in the top level.
                    4. A bytes object corresponding to a zip archive containing either a yaml
                       config file in the top level when extracted, or a directory containing a
                       yaml config file in the top level.
            load_singleton: bool (Defaults to False)
                Indicates whether this model should be loaded as a singleton.

        Returns:
            subclass of blocks.base.BlockBase
                Model object that is loaded, configured, and ready for prediction.
        """
        # This is mainly done for the Watson Studio integration so that the models are loadable from
        # a volume mount such as `/opt/ibm/nlpmodels`. Note if the path exists we assume the
        # customer is trying to load their own model (e.g,. a standard models saved to disk, or
        # a custom model downloaded from Studio data assets. In that case we keep module_path intact.
        load_path = watson_core.lib_config.load_path
        if load_path is not None and isinstance(module_path, str):
            if not os.path.exists(module_path):
                module_path = os.path.join(load_path, module_path)

        # Ensure that we have a loadable directory.
        error.type_check("<COR98255419E>", str, BytesIO, bytes, module_path=module_path)
        if isinstance(module_path, str):
            # Ensure this path is operating system correct if it isn't already.
            module_path = os.path.normpath(module_path)
        # If we have bytes, convert to a buffer, since we already handle in memory binary streams.
        elif isinstance(module_path, bytes):
            module_path = BytesIO(module_path)
        # Now that we have a file like object | str we can try to load as an archive.
        if zipfile.is_zipfile(module_path):
            return self._load_from_zipfile(module_path, load_singleton, *args, **kwargs)
        try:
            return self._load_from_dir(module_path, load_singleton, *args, **kwargs)
        except FileNotFoundError:
            error(
                "<COR80419785E>",
                FileNotFoundError(
                    "Module load path `{}` does not contain a `config.yml` file.".format(
                        module_path
                    )
                ),
            )

    def _load_from_dir(self, module_path, load_singleton, *args, **kwargs):
        """Load a model from a directory.

        Args:
            module_path:  str
                Path to directory. At the top level of directory is `config.yml` which holds info
                about the model.
            load_singleton: bool
                Indicates whether this model should be loaded as a singleton.

        Returns:
            subclass of blocks.base.BlockBase
                Model object that is loaded, configured, and ready for prediction.
        """
        module_config = module.ModuleConfig.load(module_path)

        # Check if the model is being loaded in singleton fashion. If so,
        # then fetch they hash for the module from config and use it as key.
        key = module_config.unique_hash
        if load_singleton and key is not None and key in self.singleton_module_cache:
            # return model back from singleton cache
            return self.singleton_module_cache[key]

        # retrive and validate the module class to initialize based on the
        # module_id retrieved from the configuration (which is dynamically set
        # based on either a block_id or workflow_id in the config.yml), looking up
        # the corresponding MODULE_ID (BLOCK_ID/WORKFLOW_ID) of the module class
        # in the ModuleBase class registry
        module_id = module_config["module_id"]
        module_class = MODULE_REGISTRY.get(module_id)

        if module_class is None:
            error(
                "<COR50207494E>",
                ValueError(
                    "could not find class with MODULE_ID of `{}`".format(module_id)
                ),
            )

        if not issubclass(module_class, module.ModuleBase):
            error(
                "<COR18830919E>",
                TypeError(
                    "class `{}` is not a valid module for module load".format(
                        module_class.__name__
                    )
                ),
            )

        # instantiate object and return to user
        loaded_artifact = module_class.load(module_path, *args, **kwargs)

        # if singleton loading is enabled, and module unique hash is available,
        # save the module in singleton map
        if load_singleton and key is not None:
            self.singleton_module_cache[key] = loaded_artifact

        return loaded_artifact

    def _load_from_zipfile(self, module_path, load_singleton, *args, **kwargs):
        """Load a model from a zip archive.

        Args:
            module_path:  str
                Path to directory. At the top level of directory is `config.yml` which holds info
                about the model.
            load_singleton: bool
                Indicates whether this model should be loaded as a singleton.

        Returns:
            subclass of blocks.base.BlockBase
                Model object that is loaded, configured, and ready for prediction.
        """
        with tempfile.TemporaryDirectory() as extract_path:
            with zipfile.ZipFile(module_path, "r") as zip_f:
                zip_f.extractall(extract_path)
            # Depending on the way the zip archive is packaged, out temp directory may unpack
            # to files directly, or it may unpack to a (single) directory containing the files.
            # We expect the former, but fall back to the second if we can't find the config.
            try:
                model = self._load_from_dir(
                    extract_path, load_singleton, *args, **kwargs
                )
            # NOTE: Error handling is a little gross here, the main reason being that we
            # only want to log to error() if something is fatal, and there are a good amount
            # of things that can go wrong in this process.
            except FileNotFoundError:
                get_full_path = lambda f: os.path.join(extract_path, f)
                # Get the contained directories. Omit anything starting with __ to avoid
                # accidentally traversing compression artifacts, e.g., __MACOSX.
                nested_dirs = [
                    get_full_path(f)
                    for f in os.listdir(extract_path)
                    if os.path.isdir(get_full_path(f)) and not f.startswith("__")
                ]
                # If we have multiple dirs, something is probably wrong - this doesn't look
                # like a simple level of nesting as a result of creating the zip.
                if len(nested_dirs) != 1:
                    error(
                        "<COR06761097E>",
                        FileNotFoundError(
                            "Unable to locate archive config due to nested dirs"
                        ),
                    )
                # Otherwise, try again. If we fail again stop, because the zip creation should only
                # create one potential extra layer of nesting around the model directory.
                try:
                    model = self._load_from_dir(
                        nested_dirs[0], load_singleton, *args, **kwargs
                    )
                except FileNotFoundError:
                    error(
                        "<COR84410081E>",
                        FileNotFoundError(
                            "Unable to locate archive config within top two levels".format(
                                module_path
                            )
                        ),
                    )
        return model

    def fetch(
        self,
        module_name,
        username=None,
        password=None,
        parent_dir=None,
        show_progress_bar=False,
    ):
        """Method to download a given model archive if present. Does NOT unzip it.

        Args:
            module_name:  str
                Name of artifact (case-sensitive) to download. Could be a valid model/resource
            username: str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password: str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY
            parent_dir: str
                Parent directory where the model archive is downloaded as "<model_name>.zip".
                Defaults to current working directory.
            show_progress_bar: bool
                Whether we want to show a tqdm progress bar for the download

        Returns:
            str
                Output path where the model archive is downloaded.
        """
        if not username:
            username = os.environ.get("ARTIFACTORY_USERNAME")

        if not password:
            password = os.environ.get("ARTIFACTORY_API_KEY")

        if username is None or password is None:
            error(
                "<COR30723302E>",
                ValueError(
                    "Please either pass in username/password as arguments or set the "
                    "environment variables: `ARTIFACTORY_USERNAME` and `ARTIFACTORY_API_KEY` "
                    "to download models."
                ),
            )

        parent_dir = os.path.abspath(parent_dir or os.getcwd())
        module_path = os.path.join(parent_dir, module_name)

        extension = "zip"
        module_zip_path = ".".join([module_path, extension])

        full_url_path = None

        # Search module in model catalog
        models = self.model_catalog.get_models(username, password)
        if module_name in models:
            full_url_path = models.get(module_name)

        # Search module in resource catalog if not found in models
        workflows = self.workflow_catalog.get_workflows(username, password)
        if module_name in workflows:
            full_url_path = workflows.get(module_name)

        # Search module in resource catalog if not found in models
        resources = self.resource_catalog.get_resources(username, password)
        if module_name in resources:
            full_url_path = resources.get(module_name)

        if full_url_path is None:
            error(
                "<COR22599008E>",
                ValueError("Invalid module name: `{}`".format(module_name)),
            )

        return web.WebClient.request_chunks(
            full_url_path,
            username,
            password,
            module_zip_path,
            show_progress_bar=show_progress_bar,
        )

    def extract(self, zip_path, model_path, force_overwrite=False):
        """Method to extract a downloaded archive to a specified directory.

        Args:
            zip_path: str
                Location of .zip file to extract.
            model_path: str
                Model directory where the archive should be unzipped unzipped.
            force_overwrite: bool (Defaults to false)
                Force an overwrite to model_path, even if the folder exists
        Returns:
            str
                Output path where the model archive is unzipped.
        """
        model_path = os.path.abspath(model_path)

        # skip if force_overwrite disabled and path already exists
        if not force_overwrite and os.path.exists(model_path):
            log.info(
                "INFO: Skipped extraction. Archive already extracted in directory: %s",
                model_path,
            )
            return model_path

        with zipfile.ZipFile(zip_path, "r") as zip_f:
            zip_f.extractall(model_path)

        # path to model
        return model_path

    def download(
        self,
        model_name,
        username=None,
        password=None,
        parent_dir=None,
        force_overwrite=False,
        show_progress_bar=False,
    ):
        """Method to download a given model archive if present and unzip it to an output directory.

        Args:
            model_name: str
                Name of model (case-sensitive) to download.
            username: str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password: str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY
            parent_dir: str
                Parent directory where the model archive is unzipped under model_name. Defaults to
                current working directory.
            force_overwrite: bool (Defaults to false)
                Default download behavior is to check whether model directory exists in
                parent_dir, and to skip the download if it does. `force_overwrite` overwrites
                that directory to force a download.
            show_progress_bar: bool
                Whether we want to show a tqdm progress bar for the download

        Returns:
            str
                Output path where the model archive is unzipped.
        """
        if not username:
            username = os.environ.get("ARTIFACTORY_USERNAME")
        if not password:
            password = os.environ.get("ARTIFACTORY_API_KEY")

        # download and extract .zip file
        parent_dir = (
            os.path.abspath(parent_dir) if parent_dir else os.path.abspath(os.getcwd())
        )
        model_path = os.path.abspath(os.path.join(parent_dir, model_name))

        # make sure parent_dir exists before downloading
        if not os.path.exists(parent_dir):
            error(
                "<COR17079245E>",
                FileNotFoundError("Directory '{}' does not exist.".format(parent_dir)),
            )

        # skip if `force_overwrite` disabled and path already exists
        if not force_overwrite and os.path.exists(model_path):
            log.info(
                "INFO: Skipped download. Model already downloaded in directory: %s",
                parent_dir,
            )
            return model_path

        download_path = self.fetch(
            model_name,
            username,
            password,
            parent_dir,
            show_progress_bar=show_progress_bar,
        )
        model_path = self.extract(download_path, model_path, force_overwrite)
        # don't need the .zip file anymore
        os.remove(download_path)

        return model_path

    def download_and_load(
        self,
        model_name,
        username=None,
        password=None,
        parent_dir=None,
        force_overwrite=False,
        show_progress_bar=False,
        *args,
        **kwargs
    ):
        """Method to download a given model archive if present, unzip it to an output directory and
        return a loaded instance of the model. Combines .download and .load as one piped operation.

        Args:
            model_name: str
                Name of model (case-sensitive) to download.
            username: str
                Applicable username to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_USERNAME
            password: str
                Applicable password to download the artifact. If None, looks for credentials from
                environment variable: ARTIFACTORY_API_KEY
            parent_dir: str
                Parent directory where the model archive is unzipped under model_name. Defaults to
                current working directory.
            force_overwrite: bool (Defaults to false)
                Default download behavior is to check whether model directory exists in
                parent_dir, and to skip the download if it does. `force_overwrite` overwrites
                that directory to force a download.
            show_progress_bar: bool
                Whether we want to show a tqdm progress bar for the download
            *args, **kwargs:
                Additional arguments of any type to be passed to the function.
        Returns:
            subclass of blocks.base.BlockBase
                Model object that is loaded, configured, and ready for prediction.
        """
        return self.load(
            self.download(
                model_name,
                username,
                password,
                parent_dir,
                force_overwrite,
                show_progress_bar=show_progress_bar,
            ),
            *args,
            **kwargs
        )

    def resolve_and_load(
        self, path_or_name_or_model_reference: Union[str, ModuleBase], **kwargs
    ):
        """Try our best to load a model, given a path or a name. Simply returns any loaded model
        passed in. This exists to ease the burden on workflow developers who need to accept
        individual blocks in their API, where users may have references to custom models or may only
        have the ability to give the name of a stock model.

        Args:
            path_or_name_or_model_reference (str, ModuleBase): Either a
                - Path to a model on disk
                - Name of a model that the catalog knows about
                - Loaded module (e.g. block or workflow)
            **kwargs: Any keyword arguments to pass along to ModelManager.load()
                      or ModelManager.download()
                e.g. parent_dir

        Returns:
            A loaded module

        Examples:
            >>> stock_syntax_model = manager.resolve_and_load('syntax_izumo_en_stock')
            >>> local_categories_model = manager.resolve_and_load('path/to/categories/model')
            >>> some_custom_model = manager.resolve_and_load(some_custom_model)
        """
        error.type_check(
            "<COR50266694E>",
            str,
            ModuleBase,
            path_or_name_or_model_reference=path_or_name_or_model_reference,
        )

        # If this is already a module, we're good to go
        if isinstance(path_or_name_or_model_reference, ModuleBase):
            log.debug("Returning model %s directly", path_or_name_or_model_reference)
            return path_or_name_or_model_reference

        # Otherwise, this could either be a path on disk or some name of a model that our catalog
        # can resolve and fetch
        if os.path.isdir(path_or_name_or_model_reference):
            # Try to load from path
            log.debug(
                "Attempting to load model from path %s", path_or_name_or_model_reference
            )
            return self.load(path_or_name_or_model_reference, **kwargs)
        else:
            # Hope that this is a model name
            log.debug(
                "Attempting to find model with name %s", path_or_name_or_model_reference
            )
            return self.download_and_load(path_or_name_or_model_reference, **kwargs)

    def get_singleton_model_cache_info(self):
        """Returns information about the singleton cache in {hash: module type} format

        Returns:
            Dict[str, type]
                A dictionary of model hashes to model types
        """
        return {k: type(v) for k, v in self.singleton_module_cache.items()}

    def clear_singleton_cache(self):
        """Clears the cache of singleton models. Useful to release references of models, as long as
        you know that they are no longer held elsewhere and you won't be loading them again.

        Returns:
            None
        """
        self.singleton_module_cache = {}
