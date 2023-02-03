import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def split_columns(data):
    """
    """
    cat_cols = []
    num_cols = []
    for col in data.columns:
        if data[col].dtype == "object":
            cat_cols.append(col)
        if (data[col].dtype == "int64") and (data[col].value_counts().count() <= 2):  # Binary
            cat_cols.append(col)
        if (data[col].dtype == "int64") and (data[col].value_counts().count() > 2):  # Non-Binary
            num_cols.append(col)
        if data[col].dtype == "float":
            num_cols.append(col)

    return data[num_cols], data[cat_cols]
