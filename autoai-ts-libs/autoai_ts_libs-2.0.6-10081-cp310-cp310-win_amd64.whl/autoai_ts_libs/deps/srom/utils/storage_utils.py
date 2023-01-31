# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


import os
import pickle
import shutil
import tempfile
import zipfile

from sklearn.pipeline import Pipeline
from tensorflow.keras.models import load_model
from pathlib import Path
from autoai_ts_libs.deps.srom.utils.copy_utils import deeper_copy


def sklearn_pipeline_save(
    sk_pipeline, save_dir=None, artifact_name=None, artifact_id=0
):
    """
    Pickles or stores a sklearn pipeline object in the local disc and returns the storage
    meta data.

    Args:
        sk_pipeline ():
        artifact_name ():
        artifact_id ():

    Returns:
        pipeline_save_path ():
    """

    # store in the zip
    if save_dir is None:
        save_dir = os.getcwd()

    pickle_name = "sklearn_pipeline"

    if artifact_name is not None:
        pickle_name = artifact_name + "_" + pickle_name
    pickle_name = pickle_name + "_" + str(artifact_id) + ".pkl"
    pickle_path = str(Path(save_dir) / pickle_name)

    model_pathlist = []
    steps_copy = []

    for j, step in enumerate(sk_pipeline.steps):
        model = step[1]
        model_path = "keras_model_p" + str(artifact_id) + "s" + str(j) + ".h5"
        model_save_path = str(Path(save_dir) / model_path)
        if "keras.wrappers" in str(type(model)) and hasattr(model, "model"):
            model.model.save(model_save_path)
            steps_copy.append((step[0], None))
            model_pathlist.append(model_save_path)
        elif "keras.models" in str(type(model)):
            model.save(model_save_path)
            steps_copy.append((step[0], None))
            model_pathlist.append(model_save_path)
        else:
            model_pathlist.append(0)
            steps_copy.append(step)

    try:
        sk_pipeline_copy = deeper_copy(Pipeline(steps_copy))
        with open(pickle_path, "wb") as output_file:
            pickle.dump(sk_pipeline_copy, output_file)
    except:
        raise Exception("Model cannot be pickled!")

    pipeline_save_path = {}
    pipeline_save_path["pipeline_save_path"] = pickle_path
    pipeline_save_path["model_pathlist"] = model_pathlist
    return pipeline_save_path


def save_pipeline(pipeline, save_path):
    """
    Saves the srom pipeline to the local disc to the specified path.

    Args:
        pipeline:
        save_path:
    """
    from autoai_ts_libs.deps.srom.pipeline.srom_pipeline import SROMPipeline

    if not isinstance(pipeline, SROMPipeline):
        raise Exception("Pipeline is not an SROM Pipeline")

    meta_data = {}

    tmp_path = tempfile.mkdtemp()

    try:
        meta_data["mode"] = "pipeline"
        main_pipeline_path = str(Path(tmp_path) / "srom_pipeline.pkl")
        pickle.dump(pipeline, open(main_pipeline_path, "wb"))
    except:
        meta_data["mode"] = "path"

        # store best estimators
        if pipeline.best_estimator is not None:
            pipeline_save_path = sklearn_pipeline_save(
                pipeline.best_estimator, save_dir=tmp_path, artifact_id="best_est"
            )
            meta_data["best_estimator"] = pipeline_save_path

        if pipeline.best_estimators is not None:
            meta_data["best_estimators"] = []
            for i, estimator in enumerate(pipeline.best_estimators):
                pipeline_save_path = sklearn_pipeline_save(
                    estimator, save_dir=tmp_path, artifact_id=i
                )
                meta_data["best_estimators"].append(pipeline_save_path)

        tmp_best_estimators = pipeline.best_estimators
        tmp_best_estimator = pipeline.best_estimator

        pipeline.best_estimators = None
        pipeline.best_estimator = None
        main_pipeline_path = str(Path(tmp_path) / "srom_pipeline.pkl")
        pickle.dump(pipeline, open(main_pipeline_path, "wb"))
        pipeline.best_estimators = tmp_best_estimators
        pipeline.best_estimator = tmp_best_estimator

    archive = zipfile.ZipFile(save_path, "w")

    # put all the .zip file
    if "best_estimator" in meta_data.keys():
        path = meta_data["best_estimator"]["pipeline_save_path"]
        path_info = meta_data["best_estimator"]["model_pathlist"]
        archive.write(
            path, compress_type=zipfile.ZIP_DEFLATED, arcname=os.path.basename(path)
        )
        meta_data["best_estimator"]["pipeline_save_path"] = os.path.basename(path)
        for i, path_info_item in enumerate(path_info):
            if path_info_item != 0:
                archive.write(
                    path_info_item,
                    compress_type=zipfile.ZIP_DEFLATED,
                    arcname=os.path.basename(path_info_item),
                )
                meta_data["best_estimator"]["model_pathlist"][i] = os.path.basename(
                    path_info_item
                )

    if "best_estimators" in meta_data.keys():
        for i, pipeline_path in enumerate(meta_data["best_estimators"]):
            path = pipeline_path["pipeline_save_path"]
            path_info = pipeline_path["model_pathlist"]
            archive.write(
                path, compress_type=zipfile.ZIP_DEFLATED, arcname=os.path.basename(path)
            )
            meta_data["best_estimators"][i]["pipeline_save_path"] = os.path.basename(
                path
            )
            for j, path_info_item in enumerate(path_info):
                if path_info_item != 0:
                    archive.write(
                        path_info_item,
                        compress_type=zipfile.ZIP_DEFLATED,
                        arcname=os.path.basename(path_info_item),
                    )
                    meta_data["best_estimators"][i]["model_pathlist"][
                        j
                    ] = os.path.basename(path_info_item)

    # store the meta data
    meta_data_path = str(Path(tmp_path) / "metadata.pkl")
    pickle.dump(meta_data, open(meta_data_path, "wb"))

    archive.write(
        meta_data_path,
        compress_type=zipfile.ZIP_DEFLATED,
        arcname=os.path.basename(meta_data_path),
    )
    archive.write(
        main_pipeline_path,
        compress_type=zipfile.ZIP_DEFLATED,
        arcname=os.path.basename(main_pipeline_path),
    )

    archive.close()
    shutil.rmtree(tmp_path)
    return


def load_pipeline(load_path):
    """
    Function to load srom pipeline from the local disc.

    Args:
        load_path:

    Returns:
        pipeline ():
    """
    unzip_path = tempfile.mkdtemp()

    srom_pipeline_archive = zipfile.ZipFile(load_path, "r")
    srom_pipeline_archive.extractall(unzip_path)
    srom_pipeline_archive.close()

    meta_data_path = str(Path(unzip_path) / "metadata.pkl")
    meta_data = {}
    with open(meta_data_path, "rb") as input_file:
        meta_data = pickle.load(input_file)

    pipeline_path = str(Path(unzip_path) / "srom_pipeline.pkl")
    pipeline = None
    with open(pipeline_path, "rb") as input_file:
        pipeline = pickle.load(input_file)

    if meta_data["mode"] == "path":

        if "best_estimator" in meta_data.keys():
            path = meta_data["best_estimator"]["pipeline_save_path"]
            path_info = meta_data["best_estimator"]["model_pathlist"]

            pipeline.best_estimator = pickle.load(
                open(str(Path(unzip_path) / path), "rb")
            )
            for i, path_info_item in enumerate(path_info):
                if path_info_item != 0:
                    if "keras" in path_info_item:
                        tmp_model = load_model(str(Path(unzip_path) / path_info_item))
                        pipeline.best_estimator.steps[i] = (
                            pipeline.best_estimator.steps[i][0],
                            tmp_model,
                        )

        if "best_estimators" in meta_data.keys():
            pipeline.best_estimators = []
            for path_dict in meta_data["best_estimators"]:
                path = path_dict["pipeline_save_path"]
                path_info = path_dict["model_pathlist"]
                pipeline_obj = pickle.load(open(str(Path(unzip_path) / path), "rb"))
                for i, path_info_item in enumerate(path_info):
                    if path_info_item != 0:
                        if "keras" in path_info_item:
                            tmp_model = load_model(
                                str(Path(unzip_path) / path_info_item)
                            )
                            pipeline_obj.steps[i] = (
                                pipeline_obj.steps[i][0],
                                tmp_model,
                            )
                pipeline.best_estimators.append(pipeline_obj)

    shutil.rmtree(unzip_path)

    return pipeline


def load_pipeline_from_cos(cos_client, bucket_name, filename):
    """
    Function to load pipeline in python from a cloud object storage bucket.

    Args:
        cos_client ()
        bucket_name ()
        filename ()

    Returns:
        pipeline ()
    """
    download_path = tempfile.mkdtemp()
    cos_download_path = str(Path(download_path) / "tmp_pipeline_cos_download.zip")

    obj = cos_client.get_object(Bucket=bucket_name, Key=filename)
    with open(cos_download_path, "wb") as output:
        output.write(obj.get("Body").read())

    pipeline = load_pipeline(cos_download_path)

    os.remove(cos_download_path)
    os.rmdir(download_path)

    return pipeline
