import abc
import pickle
from pathlib import Path
import warnings
from typing import Tuple, Union, List
import numpy as np
import pandas as pd
from ...utils.serial import Serializable


class DataLoader(abc.ABC):
    """
    DataLoader is designed for loading raw data from original data source.
    """
    @abc.abstractmethod
    def load(self) -> pd.DataFrame:
        pass


class StaticDataLoader(DataLoader, Serializable):
    """
    DataLoader that supports loading data from file or as provided.
    """

    include_attr = ["_config"]

    def __init__(self, config: dict, join="outer"):
        """
        Parameters
        ----------
        config : dict
            {fields_group: <path or object>}
        join : str
            How to align different dataframes
        """
        self._config = config  # using "_" to avoid confliction with the method `config` of Serializable
        self.join = join
        self._data = {}
        self._weight = None

    def __getstate__(self) -> dict:
        # avoid pickling `self._data`
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def load(self) -> pd.DataFrame:
        self._maybe_load_raw_data()
        return self._data

    @abc.abstractmethod
    def _load_file(self, path: str) -> pd.DataFrame:
        pass

    def _maybe_load_raw_data(self):
        if len(self._data) > 0:
            return
        
        splits = self._config['splits']
        for k, v in splits.items():
            self._data[k] = self._load_file(v['path'])

        if 'weight' in self._config:
            self._weight = self._config['weight']
        

class PickleDataLoader(StaticDataLoader, Serializable):
    def __init__(self, config: dict, join="outer"):
        super().__init__(config, join)

    def _load_file(self, path: str) -> pd.DataFrame:
        return pd.read_pickle(path)


class CSVDataLoader(StaticDataLoader, Serializable):
    def __init__(self, config: dict, join="outer"):
        super().__init__(config, join)

    def _load_file(self, path: str) -> pd.DataFrame:
        return pd.read_csv(path)

