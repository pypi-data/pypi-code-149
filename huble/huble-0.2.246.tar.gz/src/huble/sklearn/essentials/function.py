from sklearn.model_selection import train_test_split as sklearn_tts  # type: ignore
import pandas as pd
from ...error.decorators import function_error_handling
from connector import Dataset
from sklearn.externals import joblib

# @function_error_handling("train_test_split")
def train_test_split(**params):
    data = params["data"]
    train_dataset, test_dataset = sklearn_tts(
        data, test_size=params["parameters"]["test_size"], random_state=42
    )
    return train_dataset, test_dataset


# @function_error_handling("train_model")
def train_model(**params):
    data = params["data"]
    y = data[params["column"]]
    X = data.drop(params["column"], axis=1)
    data_dict  = Dataset.get_dataframe_types(X)
    model = params["model"]
    Model = model.fit(X, y)
    filename = 'model.joblib'
    joblib.dump(model, filename)
    return Model, data_dict, filename
