# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
.. module:: pipeline_skeleton
   :synopsis: This module runs on the wml execution environment \
        if user submits a srom pipeline training to wml \
        execution environment.

.. moduleauthor:: SROM Team
"""
import argparse
import gzip
import json
import logging
import multiprocessing
import os
import time
import pandas as pd
import numpy as np

# from autoai_ts_libs.deps.srom.pipeline.time_series_prediction import TimeSeriesPredictionPipeline

import dill

from autoai_ts_libs.deps.srom.utils.file_utils import possibly_unsafe_join
from autoai_ts_libs.deps.srom.utils.srom_tabulate import tabulate

LOGGER = logging.getLogger(__name__)

print("We have numpy {} and pandas {}".format(np.__version__, pd.__version__))


def parse_execution_cmd(parser):
    """
    Method to parse execution command.

    Parameters:
        parser (ArgumentParser, required): Parses arguments.

    Returns:
        parser: Returns the parser containing all the arguments to \
            the execution command.
    """
    parser.add_argument(
        "--train_x", type=str, required=True, help="Data name (X) for training"
    )
    parser.add_argument(
        "--train_y", type=str, required=True, help="Output name (y) for training"
    )
    parser.add_argument(
        "--path_id", type=str, required=False, default="-1", help="Path ID to execute"
    )
    parser.add_argument(
        "--exectype",
        type=str,
        required=False,
        default="single_node_random_search",
        help="Complete Search or Random Search",
    )
    parser.add_argument(
        "--execgranularity",
        type=str,
        required=False,
        default="fine",
        help="Use single training run or multiples",
    )
    parser.add_argument(
        "--num_option_per_pipeline",
        type=str,
        required=False,
        default="10",
        help="A parameter for random Search",
    )
    parser.add_argument("--verbosity", type=str, required=False, default="low")
    parser.add_argument(
        "--label",
        type=str,
        required=False,
        default="label",
        help="label for pre-failure data",
    )
    parser.add_argument(
        "--n_jobs",
        type=str,
        required=False,
        default="None",
        help="n_jobs for pipeline execution",
    )
    parser.add_argument(
        "--pre_dispatch",
        type=str,
        required=False,
        default="2*n_jobs",
        help="pre_dispatch for pipeline execution",
    )
    return parser


def pipeline_skeleton(kwargs=None):
    start_time = time.time()
    if kwargs is not None:
        args = kwargs
    else:
        args = parse_args()
    train_X = args.train_x
    train_y = args.train_y
    path_id = int(args.path_id)
    exectype = args.exectype
    # exectype = "single_node_random_search"
    execgranularity = args.execgranularity
    num_option_per_pipeline = int(args.num_option_per_pipeline)
    verbosity = args.verbosity
    label = args.label
    is_hpo = False
    n_jobs = args.n_jobs
    pre_dispatch = args.pre_dispatch

    print("Input arguments are:")
    print(args)
    LOGGER.debug("Input arguments are: %s", str(args))

    # handle n_jobs
    cpu_count = multiprocessing.cpu_count()
    if n_jobs == "None":
        n_jobs = cpu_count
    else:
        n_jobs = min(int(n_jobs), cpu_count)
    # loading pipeline from pickle file
    LOGGER.debug("loading pipeline from pickle file.")
    pipeline = dill.load(open("tmp_pipeline.pkl", "rb"))
    LOGGER.debug(
        "loading pipeline from pickle file completed successfully %s ", str(pipeline)
    )

    # creating path for data in buckets
    LOGGER.debug("creating path for data in buckets.")
    if os.environ.get("DATA_DIR") is not None:
        data_folder = os.environ["DATA_DIR"]
        path_x = possibly_unsafe_join(data_folder, train_X)
        path_y = possibly_unsafe_join(data_folder, train_y)
    else:
        raise Exception("DATA_DIR not found.")

    # reading X and y data from bucket
    LOGGER.debug("reading X and y data from bucket.")

    df_X = pd.read_csv(gzip.GzipFile(path_x, "rb"))
    df_y = pd.read_csv(gzip.GzipFile(path_y, "rb"))
    LOGGER.debug("reading X and y data from bucket completed successfully.")

    estimator_path, estimator_score = pipeline.execute(
        df_X,
        df_y,
        exectype=exectype,
        verbosity=verbosity,
        param_grid=pipeline.param_grid,
        num_option_per_pipeline=num_option_per_pipeline,
        n_jobs=n_jobs,
        pre_dispatch=pre_dispatch,
    )

    if pipeline.best_estimator:
        pipeline.fit(df_X, df_y)
    else:
        LOGGER.error("Best estimator not found.")
        raise Exception("Best estimator not found.")

    total_execution = time.time() - start_time

    result = []
    result.append(["estimator path", estimator_path])
    result.append(["estimator score", estimator_score])
    result.append(["total execution time", str(total_execution) + " sec"])

    print("-" * 80)
    print(
        tabulate(result, tablefmt="grid", stralign=None, headers=["headers", "results"])
    )
    print("-" * 80)

    # saving the results to IBM Cloud bucket
    if os.environ.get("RESULT_DIR") is not None:
        output_dir = possibly_unsafe_join(os.environ["RESULT_DIR"], "results")
        os.makedirs(output_dir, exist_ok=True)
        LOGGER.debug("Output directory is %s", output_dir)

        with open(
                possibly_unsafe_join(output_dir, "pipeline_output.pkl"), "wb"
        ) as output_file:
            dill.dump(
                [
                    total_execution,
                    int(path_id),
                    estimator_score,
                    pipeline.best_estimator,
                ],
                output_file,
            )
        with open(
                possibly_unsafe_join(output_dir, "trained_pipeline.pkl"), "wb"
        ) as output_file:
            dill.dump(pipeline, output_file)

        # In case of 'hpo_search' exectype, we need to store results in val_dict_list.json
        if is_hpo:
            with open(
                    possibly_unsafe_join(os.environ["RESULT_DIR"], "val_dict_list.json"),
                    "w",
            ) as vdl:
                json.dump(
                    [
                        {
                            "steps": int(os.environ["SUBID"]),
                            "best_score": float(estimator_score),
                        }
                    ],
                    vdl,
                )
    else:
        LOGGER.error("Result Bucket not provided.")
        raise Exception("Result Bucket not provided.")


def parse_args():
    """
    Contains code to be executed on WML.
    """
    # Do not remove below print statement. Used to display trimmed logs.
    print("\n--- WML EXECUTION ---\n")

    from autoai_ts_libs.deps.srom.pipeline.srom_param_grid import SROMParamGrid

    # from autoai_ts_libs.deps.srom.pipeline.anomaly_pipeline import AnomalyPipeline

    # getting the arguments from execution command
    LOGGER.debug("parsing the arguments from execution command.")
    parser = argparse.ArgumentParser(description="SROM pipeline execution on WML")
    parser = parse_execution_cmd(parser)
    args = parser.parse_args()
    LOGGER.debug("arguments parsing from execution command completed successfully.")
    # taking arguments
    return args


if __name__ == "__main__":
    pipeline_skeleton()
