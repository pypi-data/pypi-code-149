import pandas as pd
import requests
from pydantic import BaseModel
#import woodwork as ww


class Dataset:
    def __init__(self, url) -> None:
        self.url = url
        self.dataframe = self.__load_dataset(url)

    def __load_dataset(self, url: str) -> pd.DataFrame:
        local_filename = url.split("/")[-1]
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return pd.read_csv(local_filename)

    def parse_dataset(self):
        data_dict = pd.io.json.build_table_schema(self.dataframe)   # type: ignore  
        for field in data_dict['fields']:
            if field['type']=='integer':
                field['type'] = 'number'
            if field['type']=='any':    
                field.pop('constraints')
                field.pop('ordered')
                field['type'] = 'categorical'
        return data_dict



        # self.dataframe.ww.init()
        # logical_types = self.dataframe.ww.logical_types
        # logical_types_dict = {}
        # for col in logical_types:
        #     logical_types_dict[col] = logical_types[col]
        # return logical_types_dict
