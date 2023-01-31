# IBM Confidential Materials
# Licensed Materials - Property of IBM
# IBM Smarter Resources and Operation Management
# (C) Copyright IBM Corp. 2021 All Rights Reserved.
# US Government Users Restricted Rights
#  - Use, duplication or disclosure restricted by
#    GSA ADP Schedule Contract with IBM Corp.


"""
Maintains utility functions for exporting best found pipeline code
"""

import inspect
import codecs


def export_pipeline(
    exported_pipeline, code_file_path, random_state=None, data_file_path=""
):

    pipeline_text = ""
    pipeline_code, import_packages = _generate_pipeline_source_code(
        exported_pipeline.steps
    )
    pipeline_text = _generate_import_code(import_packages)
    pipeline_text = pipeline_text + _pipeline_code_wrapper(
        pipeline_code, random_state, data_file_path
    )
    code_file_path = _persist_pipeline(pipeline_text, code_file_path)
    return code_file_path


def _generate_pipeline_source_code(exported_pipeline):
    pipeline_code = ""
    import_packages = []
    if type(exported_pipeline) == list:
        for estimator in exported_pipeline:
            est_obj = None
            if type(estimator) == tuple:
                est_obj = estimator[1]
            else:
                est_obj = estimator
            object_members = inspect.getmembers(est_obj)
            for member in object_members:
                if member[0] == "__class__":
                    klass = member[1]
                    klass_name = klass.__name__
                    module_name = klass.__module__
                    import_packages.append(
                        "from " + module_name + " import " + klass_name
                    )
        pipeline_code = str(exported_pipeline)
    else:
        raise Exception("exported srom pipeline is not in list format")

    return pipeline_code, import_packages


def _generate_import_code(import_packages):
    import_text = ""
    packages = [
        "import numpy as np",
        "import pandas as pd",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.pipeline import Pipeline",
    ]
    packages = packages + import_packages
    for package in packages:
        import_text += package + "\n"
    return import_text


def _pipeline_code_wrapper(pipeline_code, random_state, data_file_path):

    if data_file_path == "":
        data_file_path = "PATH/TO/DATA/FILE"

    return """

# Replace COLUMN_SEPARATOR with column separator of your data file.
# Replace string 'PATH/TO/DATA/FILE' with  your data file path if any.
data = pd.read_csv('{}', sep='COLUMN_SEPARATOR')

# Replace target with target column name.
features = data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = train_test_split(features, data['target'].values, random_state={})
exported_pipeline = Pipeline({})
exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
score = exported_pipeline.score(testing_features, testing_target)
print(score)
""".format(
        data_file_path, random_state, pipeline_code
    )


def _persist_pipeline(content, file_name):
    file = codecs.open(file_name, "w", "utf-8")
    file.write(content)
    file.close()
    return file_name
