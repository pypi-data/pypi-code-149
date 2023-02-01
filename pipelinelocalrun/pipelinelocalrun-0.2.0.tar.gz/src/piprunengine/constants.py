
# deperated
CURATED_ENVS_SUPPORTED = ["azureml-sklearn-0.24-ubuntu18.04-py37-cpu"]
ENV_CURATED_IMAGE_PREFIX = "azureml-"
MCR_CURATED_IMAGE_PREFIX = "mcr.microsoft.com/azureml/curated/"

CONDA_FILE_NAME = "conda.yml"
CONDA_ENV_NAME = "inf-conda-env"

BLOB_WASBS_REGEX = "wasbs://(.*?)@(.*?).blob.core.windows.net/(.+)"
BLOB_HTTPS_PATTERN = "https://{}.blob.core.windows.net/{}/{}"

class LocalRunMode(object):
    # so far only support COMPUTE_LOCAL_METRICS_LOCAL
    COMPUTE_LOCAL_METRICS_LOCAL = "COMPUTE_LOCAL_METRICS_LOCAL"
    COMPUTE_LOCAL_METRICS_REMOTE = "COMPUTE_LOCAL_METRICS_REMOTE"
    COMPUTE_REMOTE_METRICS_REMOTE = "COMPUTE_REMOTE_METRICS_REMOTE"

class CuratedEnvironmentDefaultRunMode(object):
    NATIVE = "NATIVE"
    CONTAINER = "CONTAINER"

class JobRunningStatus(object):
    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    FAIL = "Failed"
    SUCCESS = "Completed"
    Canceled = "Canceled"

class JobLocalRunMode(object):
    # run as native process
    NATIVE = "native"
    # directly use provided container image to run
    DOCKER = "docker"