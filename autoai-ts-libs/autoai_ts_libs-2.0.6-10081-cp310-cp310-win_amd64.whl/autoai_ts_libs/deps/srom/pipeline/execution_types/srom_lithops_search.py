# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import logging

import lithops
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import ParameterSampler

from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid
from autoai_ts_libs.deps.srom.pipeline.utils.lithops_helper import replace_lithops_classes
from autoai_ts_libs.deps.srom.utils.pipeline_utils import gen_pipeline_and_grid
from autoai_ts_libs.deps.srom.utils.srom_exceptions import IncorrectValueException
from autoai_ts_libs.deps.srom.utils.pipeline_utils import verbosity_to_verbose_mapping
from sklearn.pipeline import Pipeline

LOGGER = logging.getLogger(__file__)
COS_CREDS = {}
LITHOPS_CONFIG = {}
TUNING_PARAM = {"activations_limit": 50}

# the following module will be removed from model_param
# this is what it bring the significant scale-out
modules = [
    "srom",
    "jupyter_client",
    "bleach",
    "nose",
    "distributed",
    "tblib",
    "cycler.py",
    "minisom.py",
    "nbconvert",
    "xgboost",
    "openml",
    "joblib",
    "typing_extensions.py",
    "kombu",
    "notebook",
    "tsfresh",
    "nbclient",
    "prompt_toolkit",
    "pygments",
    "func_timeout",
    "knnimpute",
    "IPython",
    "pyspark",
    "decorator.py",
    "_multiprocess",
    "cython.py",
    "billiard",
    "fsspec",
    "tqdm",
    "packaging",
    "async_generator",
    "cloudpickle",
    "xlrd",
    "pyDOE",
    "keras",
    "lifelines",
    "imageio",
    "ipython_genutils",
    "mlxtend",
    "arff.py",
    "parso",
    "pyximport",
    "qtconsole",
    "ipykernel",
    "ptyprocess",
    "send2trash",
    "ecos",
    "mock",
    "tabulate.py",
    "jupyterlab_pygments",
    "dill",
    "qtpy",
    "fancyimpute",
    "lomond",
    "networkx",
    "partd",
    "terminado",
    "pyparsing.py",
    "scs",
    "watson_machine_learning_client",
    "pwlf",
    "retrying.py",
    "evolutionary_search",
    "pexpect",
    "skopt",
    "jsonschema",
    "backcall",
    "patsy",
    "locket",
    "graphviz",
    "plotly",
    "dqlearn",
    "prometheus_client",
    "defusedxml",
    "smote_variants",
    "multiprocess",
    "jupyter_core",
    "_plotly_utils",
    "imblearn",
    "ipywidgets",
    "pyomo",
    "nest_asyncio.py",
    "async_timeout",
    "yaml",
    "webencodings",
    "threadpoolctl.py",
    "ply",
    "seaborn",
    "amqp",
    "outliers",
    "vine",
    "wcwidth",
    "py4j",
    "idna_ssl.py",
    "traitlets",
    "_plotly_future_",
    "sortedcontainers",
    "xmltodict.py",
    "pmlb",
    "test",
    "rbfopt",
    "cvxpy",
    "nbformat",
    "pickleshare.py",
    "toolz",
    "entrypoints.py",
    "pykalman",
    "pandocfilters.py",
    "appdirs.py",
    "mistune.py",
    "missingpy",
    "dask",
    "celery",
    "testpath",
    "paramiko",
    "jedi",
]


# this is FIFO Batch Executors
# it needs a lots of tuning
class BatchExecutor:
    """
    Helper class to run the cloud function
    in Batch
    """

    def run(self, map_func, pipelines, activations):
        """
        map_func : to run
        pipelines : list of pipelines to execute
        activations : integer
        """

        # this was a booster for us to reduce the pickle size
        # during activations
        import types

        # I reduced the code to reduce the srom dependency
        new_boto3client = types.FunctionType(boto3client.__code__, {})
        new_csv_to_pandasdf = types.FunctionType(
            csv_to_pandasdf.__code__, {"boto3client": new_boto3client}
        )
        new_map_func = types.FunctionType(
            map_func.__code__, {"csv_to_pandasdf": new_csv_to_pandasdf}
        )

        # the limit set by user
        activations_limit = TUNING_PARAM["activations_limit"]

        # an object that was being stored
        ret_result = []

        if len(pipelines) == 0:
            return ret_result

        if activations_limit >= len(pipelines):
            activations_limit = len(pipelines)

        # submit job in Batch, wait for a batch to finish the job
        for start_index in range(0, len(pipelines), activations_limit):

            # number of requests
            num_req = activations_limit
            if start_index + activations_limit > len(pipelines):
                num_req = len(pipelines) - start_index

            activations.append(num_req)

            # step 0 - setup remote executors
            remote_executor = lithops.FunctionExecutor(config=LITHOPS_CONFIG)

            # apply map operations
            futures = remote_executor.map(
                new_map_func,
                pipelines[start_index: start_index + num_req],
                exclude_modules=modules,
            )
            # collect results
            # throw exception allow you to get rid of error
            LOGGER.info("Start to run %d pipelines on serverless." % num_req)
            ans = remote_executor.get_result(throw_except=False)
            # add execution time for each pipeline to the ans
            LOGGER.info("Results of %d pipelines received." % len(ans))
            LOGGER.debug("Results of the pipelines: {}".format(str(ans)))

            for i, future in enumerate(list(futures)):
                if ans[i] is not None:
                    ans[i] += (
                        future.stats["worker_exec_time"] / 60.0,
                    )  # worker_func_exec_time or worker_exec_time?
            ret_result.extend(ans)

        return ret_result


def boto3client(
        credentials, resiliency="cross-region", region="us", public=True, location="us-geo"
):
    """returns an ibm boto3 client"""
    # Request detailed endpoint list
    import requests
    import ibm_boto3
    from ibm_botocore.client import Config

    endpoints = requests.get(credentials.get("endpoints")).json()
    # Obtain iam and cos host from the the detailed endpoints

    iam_host = endpoints["identity-endpoints"]["iam-token"]
    cos_host = ""

    pub_string = "public" if public is True else "private"
    cos_host = endpoints["service-endpoints"][resiliency][region][pub_string][location]
    api_key = credentials.get("apikey")
    service_instance_id = credentials.get("resource_instance_id")
    endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host

    # Get bucket list
    cos = ibm_boto3.client(
        "s3",
        ibm_api_key_id=api_key,
        ibm_service_instance_id=service_instance_id,
        ibm_auth_endpoint=endpoint,
        config=Config(signature_version="oauth"),
        region_name=location,
        endpoint_url=service_endpoint,
    )

    return cos


def csv_to_pandasdf(
        credentials,
        object_name,
        resiliency="cross-region",
        region="us",
        public=False,
        location="us-geo",
        compression=None,
        **kwargs
):
    """
    Method to fetch data from cos and convert it to dataframe.
    Returns:
        Pandas dataframe
    """
    from ibm_botocore.exceptions import ClientError
    import pandas as pd

    if "BUCKET" in credentials and "bucket" not in credentials:
        credentials["bucket"] = credentials.pop("BUCKET")

    if not "bucket" in credentials:
        raise Exception("credentials must have bucket key")

    total_try = 5
    for _ in range(total_try):
        try:
            botoc = boto3client(credentials, resiliency, region, public, location)
            obj = botoc.get_object(Bucket=credentials["bucket"], Key=object_name)[
                "Body"
            ]
            if compression:
                return pd.read_csv(obj, compression=compression, **kwargs)
            else:
                return pd.read_csv(obj, **kwargs)
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "NoSuchKey":
                raise Exception(
                    "Please provide correct location and object key"
                ) from None
            else:
                raise Exception("Error in boto3 client") from None
        except KeyError as ex:
            raise Exception("Please provide correct location and object key") from None
        except:
            import time

            time.sleep(2)
        finally:
            botoc = None


def upload_X_y(X, y, bucket_name, suffix=""):
    from ibm_botocore.exceptions import ClientError

    try:
        credentials = COS_CREDS
        region = "us-south"
        resiliency = "regional"
        location = "us-south"
        public = True
        X_filename = "X_" + str(suffix)
        y_filename = "y_" + str(suffix)

        pd.DataFrame(X).to_csv(
            X_filename + ".csv.gz", index=False, header=False, compression="gzip"
        )

        if y is not None:
            pd.DataFrame(y).to_csv(
                y_filename + ".csv.gz", index=False, header=False, compression="gzip"
            )
        cos = boto3client(credentials, resiliency, region, public, location)
        with open(X_filename + ".csv.gz", "rb") as data:
            cos.upload_fileobj(data, bucket_name, X_filename)
            LOGGER.info("X is uploaded to bucket %s." % bucket_name)

        if y is not None:
            with open(y_filename + ".csv.gz", "rb") as data:
                cos.upload_fileobj(data, bucket_name, y_filename)
                LOGGER.info("y is uploaded to bucket %s." % bucket_name)

    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to create text file: {0}".format(e))


def delete_X_y(y_is_none_flag):
    """[summary]

    Args:
        X_name ([type]): [description]
        y_name ([type]): [description]
        bucket_name ([type]): [description]
    """
    from ibm_botocore.exceptions import ClientError

    # clean the buckets
    bucket_name = COS_CREDS["bucket"]
    suffix = ""
    if "suffix" in COS_CREDS.keys():
        suffix = COS_CREDS['suffix']

    credentials = COS_CREDS
    region = "us-south"
    resiliency = "regional"
    location = "us-south"
    public = True
    X_filename = "X_" + str(suffix)
    y_filename = "y_" + str(suffix)

    try:
        cos = boto3client(credentials, resiliency, region, public, location)
        cos.delete_object(Bucket=bucket_name, Key=X_filename)
        LOGGER.info("X is deleted from bucket %s." % bucket_name)

        if y_is_none_flag == 0:
            cos.delete_object(Bucket=bucket_name, Key=y_filename)
            LOGGER.info("y is deleted from bucket %s." % bucket_name)

    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to delete text file: {0}".format(e))


def create_lithops_pipeline_list(
        pipelines,
        param_grids,
        mode,
        num_option_per_pipeline,
        path_ids,
        rounds,
        scorer,
        cv,
        random_state=None,
        optimize_utilization=False,
        y_is_none_flag=0,
):
    """
    pipelines:
    param_grids:
    mode:
    num_option_per_pipeline:
    path_ids:
    rounds:
    scorer:
    random_state:
    optimize_utilization:
    """

    # we generate a sample configurations for each pipelines (based on number of options)
    lithops_pipeline_list = []
    for pipeline_index in range(len(pipelines)):
        try:
            param_list = []
            grid_combo = ParameterGrid(param_grids[pipeline_index])
            is_total_space_smaller = (
                    mode == "random" and len(grid_combo) < num_option_per_pipeline
            )
            if mode == "exhaustive" or is_total_space_smaller:
                if is_total_space_smaller:
                    LOGGER.debug(
                        """The total space of parameters is smaller than
                                    provided num_option_per_pipeline."""
                    )
                param_list = list(grid_combo)
            else:
                num_option_for_this_pipeline = num_option_per_pipeline

                if rounds == 1 and optimize_utilization:
                    ideal_pipelines_count = (
                                                    len(pipelines)
                                                    * num_option_per_pipeline
                                                    // TUNING_PARAM["activations_limit"]
                                                    + 1
                                            ) * TUNING_PARAM["activations_limit"]
                    num_option_for_this_pipeline = (
                                                           ideal_pipelines_count - len(lithops_pipeline_list)
                                                   ) / (len(pipelines) - pipeline_index)

                param_list = list(
                    ParameterSampler(
                        param_grids[pipeline_index],
                        n_iter=num_option_for_this_pipeline,
                        random_state=random_state,
                    )
                )

            for _, parameters in enumerate(param_list):
                local_pipeline = clone(pipelines[pipeline_index])
                local_pipeline.set_params(**parameters)
                current_size = len(lithops_pipeline_list)
                if isinstance(cv, int):
                    lithops_pipeline_list.append(
                        [
                            local_pipeline,
                            path_ids[pipeline_index],
                            current_size,
                            rounds,
                            COS_CREDS,
                            scorer,
                            y_is_none_flag,
                        ]  # pipeline, path_id, path_param_id, rounds
                    )
                else:
                    lithops_pipeline_list.append(
                        [
                            local_pipeline,
                            path_ids[pipeline_index],
                            current_size,
                            rounds,
                            COS_CREDS,
                            scorer,
                            cv,
                            y_is_none_flag,
                        ]  # pipeline, path_id, path_param_id, rounds
                    )
        except ValueError as value_error:
            LOGGER.debug(str(value_error))
        except Exception as exception:
            LOGGER.info(str(exception))
            raise exception
    return lithops_pipeline_list


def test_train_cf(pipeline_param_grid_tuple):
    """
    Performs cross validation.
    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
    	Shared resource for multiprocessing.
    """

    (
        local_pipeline,
        path_ids,
        pipeline_index,
        rounds,
        tmp_cos_creds,
        scorer,
        y_is_none_flag,
    ) = pipeline_param_grid_tuple

    if "suffix" in tmp_cos_creds:
        X_filename = "X_" + tmp_cos_creds["suffix"]
        y_filename = "y_" + tmp_cos_creds["suffix"]
    else:
        X_filename = "X_"
        y_filename = "y_"

    if "localhost" in tmp_cos_creds:
        import pandas as pd

        X = pd.read_csv(X_filename)
        y = pd.read_csv(y_filename)

    else:
        X = csv_to_pandasdf(
            credentials=tmp_cos_creds,
            object_name=X_filename,
            region="us-south",
            public=True,
            resiliency="regional",
            location="us-south",
            compression="gzip",
        )

        y = csv_to_pandasdf(
            credentials=tmp_cos_creds,
            object_name=y_filename,
            region="us-south",
            public=True,
            resiliency="regional",
            location="us-south",
            compression="gzip",
        )

    X = X.values
    y = y.values

    from sklearn.model_selection import train_test_split

    stratify = None
    try:
        from sklearn.base import is_classifier

        if is_classifier(local_pipeline):
            stratify = y
    except:
        pass

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=33, test_size=0.1, stratify=stratify
    )
    try:
        local_pipeline.fit(X_train, y_train)
        if scorer is None:
            score_res = local_pipeline.score(X_test, y_test)
        else:
            from sklearn.metrics import get_scorer

            score_res = get_scorer(scorer)(local_pipeline, X_test, y_test)
        return (path_ids, pipeline_index, rounds, score_res)
    except Exception as ex:
        import numpy as np

        return (path_ids, pipeline_index, rounds, np.nan)


def cv_cf(pipeline_param_grid_tuple):
    """
    Performs cross validation.
    Parameters:
        tup (tuple): Tuple containing parameters and pipeline_index.

    output:
    	Shared resource for multiprocessing.
    """

    (
        local_pipeline,
        path_ids,
        pipeline_index,
        rounds,
        tmp_cos_creds,
        scorer,
        cv,
        y_is_none_flag,
    ) = pipeline_param_grid_tuple

    if "suffix" in tmp_cos_creds:
        X_filename = "X_" + tmp_cos_creds["suffix"]
        y_filename = "y_" + tmp_cos_creds["suffix"]
    else:
        X_filename = "X_"
        y_filename = "y_"

    if "localhost" in tmp_cos_creds:
        import pandas as pd
        X = pd.read_csv(X_filename)
        if y_is_none_flag == 0:
            y = pd.read_csv(y_filename)
        else:
            y = None

    else:
        X = csv_to_pandasdf(
            credentials=tmp_cos_creds,
            object_name=X_filename,
            region="us-south",
            public=True,
            resiliency="regional",
            location="us-south",
            compression="gzip",
        )

        if y_is_none_flag == 0:
            y = csv_to_pandasdf(
                credentials=tmp_cos_creds,
                object_name=y_filename,
                region="us-south",
                public=True,
                resiliency="regional",
                location="us-south",
                compression="gzip",
            )
        else:
            y = None

    X = X.values
    if y is not None:
        y = y.values
    import numpy as np

    try:
        from sklearn.model_selection import cross_validate
        scores = cross_validate(
            local_pipeline,
            X,
            y,
            cv=cv,
            scoring=scorer,
            return_train_score=False,
        )
        return (path_ids, pipeline_index, rounds, np.mean(scores["test_score"]))
    except Exception as ex:
        return (path_ids, pipeline_index, rounds, np.nan)


def srom_lithops_search_async(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        max_eval_time_minute,
        num_option_per_pipeline=10,
        mode="exhaustive",
        groups=None,
        cross_val_score=None,
        evn_config=None,
        upload_data=False,
        random_state=None,
        lithops_mode="serverless",
        pipeline_type=Pipeline,
        pipeline_init_param={},
        verbosity="low",
        result_queue=None
):
    srom_lithops_search(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        max_eval_time_minute,
        num_option_per_pipeline,
        mode,
        groups,
        cross_val_score,
        evn_config,
        upload_data,
        random_state,
        lithops_mode,
        pipeline_type,
        pipeline_init_param,
        verbosity,
        result_queue
    )
    return


def srom_lithops_search(
        X,
        y,
        param_grid,
        paths,
        cv,
        scorer,
        max_eval_time_minute,
        num_option_per_pipeline=10,
        mode="exhaustive",
        groups=None,
        cross_val_score=None,
        evn_config=None,
        upload_data=True,
        clean_data=True,
        random_state=None,
        pipeline_type=Pipeline,
        pipeline_init_param={},
        verbosity="low",
        result_queue=None
):
    """
        X (pandas dataframe or numpy array): The dataset to be used for model selection. \
            shape = [n_samples, n_features] \
            where n_samples is the number of samples and n_features is the number of features.
        y (pandas dataframe or numpy array): Target vector to be used. This is optional, \
            if target_column is added in the meta data, it is used from there. \
            shape = [n_samples] or [n_samples, n_output]
        param_grid (dict): Dictionary with parameter names(string) as keys and lists of parameter \
            settings to try as values, or a list of such dictionaries, in which case the grids \
            spanned by each dictionary in the list are explored.
        paths (list): Consists of estimator paths.
        cv (integer, cross-validation generator or an iterable): Determines the cross-validation \
            splitting strategy.
        scorer (string, callable, list/tuple, dict or None): A single string or a callable to evaluate \
            the predictions on the test set.
        max_eval_time_minute (integer) (minutes): Maximum timeout for execution of pipelines with unique \
            parameter grid combination.
        num_option_per_pipeline (integer): Default: 10. Number of parameter settings that are sampled. \
            This parameter is applicable if mode is 'random'.
        mode (String): Default: "exhaustive". Possible values: "random" or "exhaustive"
        groups :
        cross_val_score:
        evn_config:
        upload_data:
        random_state:
        lithops_mode:
    """
    # if int(max_eval_time_minute * 60) > 600:
    #    raise IncorrectValueException("Upper limit of timeout is 10 Minute.")

    if not evn_config:
        raise IncorrectValueException("Configuration is needed.")

    global COS_CREDS
    global LITHOPS_CONFIG
    if "COS_CREDS" not in evn_config.keys():
        raise Exception("provide COS_CREDS information")
    if "LITHOPS_CONFIG" not in evn_config.keys():
        raise Exception("provide LITHOPS_CONFIG information")

    # get the value
    COS_CREDS = evn_config["COS_CREDS"]
    LITHOPS_CONFIG = evn_config["LITHOPS_CONFIG"]

    if "suffix" not in COS_CREDS.keys():
        raise Exception("provide suffix key in COS_CREDS")

    if "bucket" not in COS_CREDS.keys():
        raise Exception("provide bucket key in COS_CREDS")

    if 'lithops' in LITHOPS_CONFIG and 'backend' in LITHOPS_CONFIG['lithops']:
        LOGGER.info('Using {} as backend.'.format(LITHOPS_CONFIG['lithops']['backend']))
    else:
        raise Exception("provide backend in LITHOPS_CONFIG['lithops'].")

    if "TUNING_PARAM" in evn_config.keys():
        global TUNING_PARAM
        TUNING_PARAM = evn_config["TUNING_PARAM"]

    # Validations
    if mode not in ["exhaustive", "random"]:
        raise IncorrectValueException(
            "Supported mode should be provided: 'exhaustive' or 'random'"
        )

    # setting the verbose parameter to be passed to the GridSearchCV
    verbose = verbosity_to_verbose_mapping(verbosity)

    if not paths:
        raise IncorrectValueException("Paths should be not be None or empty.")
    if (
            not num_option_per_pipeline
            or not isinstance(num_option_per_pipeline, int)
            or num_option_per_pipeline < 1
    ):
        raise IncorrectValueException(
            "Value of num_option_per_pipeline should be int and greater than 1."
        )
    if not param_grid:
        param_grid = SROMParamGrid(gridtype="empty")

    lithops_mode = "serverless"
    if LITHOPS_CONFIG['lithops']['backend'] == 'localhost':
        lithops_mode = 'localhost'

    if upload_data:
        if lithops_mode == "localhost":
            COS_CREDS["localhost"] = True
            pd.DataFrame(X).to_csv(
                "X_" + COS_CREDS["suffix"], index=False, header=False
            )
            if y is not None:
                pd.DataFrame(y).to_csv(
                    "y_" + COS_CREDS["suffix"], index=False, header=False
                )

        elif lithops_mode == "serverless":
            if "suffix" in COS_CREDS:
                upload_X_y(
                    X, y, bucket_name=COS_CREDS["bucket"], suffix=COS_CREDS["suffix"]
                )
            else:
                upload_X_y(X, y, bucket_name=COS_CREDS["bucket"])

    # Initialize return values
    best_estimators = []
    best_scores = []
    best_scores_std = []
    execution_time_for_best_estimators = []
    activations = []
    # each original path is given a unique id

    y_is_none_flag = 0
    if y is None:
        y_is_none_flag = 1

    global_path_ids = list(range(len(paths)))
    first_param_grid = SROMParamGrid(gridtype="empty")
    pipeline_paths, param_grids = gen_pipeline_and_grid(
        paths, first_param_grid, pipeline_type, pipeline_init_param
    )
    if len(pipeline_paths) != len(global_path_ids):
        raise Exception("There is an Error in gen_pipeline_and_grid function")

    # list of tuples
    lithops_pipeline_list_round0 = create_lithops_pipeline_list(
        pipeline_paths,
        param_grids,
        mode,
        num_option_per_pipeline,
        global_path_ids,
        rounds=0,
        scorer=scorer,
        random_state=random_state,
        cv=cv,
        y_is_none_flag=y_is_none_flag,
    )
    successful_pipeline_list = []
    round_two_pipeline_global_id = []
    exploration_results = []

    try:
        LOGGER.info("Running step 0: path exploration")
        exe_ind = BatchExecutor()
        if isinstance(cv, int):
            ret_results = exe_ind.run(
                test_train_cf, lithops_pipeline_list_round0, activations
            )
        else:
            ret_results = exe_ind.run(
                cv_cf, lithops_pipeline_list_round0, activations
            )
        for result in ret_results:
            if result is not None:
                if not np.isnan(result).any():
                    successful_pipeline_list.append(paths[result[0]])
                    round_two_pipeline_global_id.append(result[0])
                    exploration_results.append(result)
    except Exception as e:
        LOGGER.debug(e)

    number_of_combinations = len(lithops_pipeline_list_round0)

    # if no successful pipeline or if the parameter grid is empty
    if len(successful_pipeline_list) > 0 and len(param_grid.default_param_grid) > 0:
        pipeline_paths_1, param_grids_1 = gen_pipeline_and_grid(
            successful_pipeline_list, param_grid, pipeline_type, pipeline_init_param,
        )

        lithops_pipeline_list_round1 = create_lithops_pipeline_list(
            pipeline_paths_1,
            param_grids_1,
            mode,
            num_option_per_pipeline - 1,
            round_two_pipeline_global_id,
            rounds=1,
            scorer=scorer,
            random_state=random_state,
            cv=cv,
            y_is_none_flag=y_is_none_flag,
        )

        try:
            LOGGER.info("Running step 1: param grid fine tuning")
            exe_ind = BatchExecutor()
            if isinstance(cv, int):
                ret_results = exe_ind.run(
                    test_train_cf, lithops_pipeline_list_round1, activations
                )
            else:
                ret_results = exe_ind.run(
                    cv_cf, lithops_pipeline_list_round1, activations
                )

            for result in ret_results:
                if result is not None:
                    if not np.isnan(result).any():
                        exploration_results.append(result)
        except Exception as e:
            LOGGER.debug(e)

        # update the count
        number_of_combinations += len(lithops_pipeline_list_round1)
    else:
        lithops_pipeline_list_round1 = []

    if len(exploration_results) > 0:
        best_estimators = []
        best_scores = []
        best_scores_std = []
        execution_time_for_best_estimators = []

        eR = pd.DataFrame(exploration_results)
        eR.columns = ["path_ids", "pipeline_index", "rounds", "mae", "execution_time"]

        # group by by path_ids, get the maximum record for mae, a record with maximum record*
        # can be used to

        for p_id in global_path_ids:
            er1 = eR.loc[eR["path_ids"] == p_id]

            if er1.shape[0] > 0:
                # We have some path that fet executed
                final_rec = er1[er1.mae == er1.mae.max()].values
                final_rec = final_rec[0]
                if final_rec[2] == 0:  # round = 0
                    best_estimators.append(lithops_pipeline_list_round0[p_id][0])
                else:
                    best_estimators.append(
                        lithops_pipeline_list_round1[int(final_rec[1])][0]  # round = 1
                    )

                best_scores.append(final_rec[3])  # score
                best_scores_std.append(
                    np.nan
                )  # for train_test_score we set it tp np.nan
                execution_time_for_best_estimators.append(final_rec[4])
            else:
                # that path is never executed
                best_estimators.append(lithops_pipeline_list_round0[p_id][0])
                best_scores.append(np.nan)
                best_scores_std.append(np.nan)
                execution_time_for_best_estimators.append(np.nan)

            if result_queue is not None:
                result_queue.put([best_estimators,
                                  best_scores,
                                  number_of_combinations,
                                  best_scores_std,
                                  execution_time_for_best_estimators,
                                  activations
                                  ])

        best_estimators = replace_lithops_classes(best_estimators)

        if clean_data and lithops_mode == "serverless":
            delete_X_y(y_is_none_flag)

        return (
            best_estimators,
            best_scores,
            number_of_combinations,
            best_scores_std,
            execution_time_for_best_estimators,
            activations,
        )
    else:

        if clean_data and lithops_mode == "serverless":
            delete_X_y(y_is_none_flag)

        LOGGER.warning("No best estimators are found.")
        best_estimators = replace_lithops_classes(best_estimators)
        best_scores = [np.nan] * number_of_combinations
        return (
            best_estimators,
            best_scores,
            number_of_combinations,
            best_scores_std,
            execution_time_for_best_estimators,
            activations,
        )
