import pandas as pd


def get_dataframe_types(self):
    data_dict = pd.io.json.build_table_schema(self.dataframe)  # type: ignore
    for field in data_dict["fields"]:
        if field["type"] == "integer":
            field["type"] = "number"
        if field["type"] == "any":
            field.pop("constraints")
            field.pop("ordered")
            field["type"] = "categorical"
    data_dict["columns"] = data_dict.pop("fields")
    data_dict.pop("primaryKey")
    data_dict.pop("pandas_version")
    return data_dict
