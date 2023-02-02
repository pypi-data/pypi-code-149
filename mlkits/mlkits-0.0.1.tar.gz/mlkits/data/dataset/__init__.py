
from ...utils.serial import Serializable
from ...utils import init_instance_by_config
from .handler import DataHandler, DataHandlerLP
from typing import Callable, Union, List, Tuple, Dict, Text, Optional
from copy import copy, deepcopy
import pandas as pd
import numpy as np
import bisect


class Dataset(Serializable):
    """
    Preparing data for model training and inferencing.
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.label_column = kwargs['label_column']
        self.feature_columns = kwargs['feature_columns']

    def config(self, **kwargs):
        """
        config is designed to configure and parameters that cannot be learned from the data
        """
        super().config(**kwargs)


    def prepare(self, **kwargs) -> object:
        """
        The type of dataset depends on the model. (It could be pd.DataFrame, pytorch.DataLoader, etc.)
        The parameters should specify the scope for the prepared data
        The method should:
        - process the data

        - return the processed data

        Returns
        -------
        object:
            return the object
        """



class DatasetH(Dataset):
    """
    Dataset with Data(H)andler

    User should try to put the data preprocessing functions into handler.
    Only following data processing functions should be placed in Dataset:
    """

    def __init__(
        self,
        handler: Union[Dict, DataHandler],
        fetch_kwargs: Dict = {},
        **kwargs,
    ):
        """
        Setup the underlying data.

        Parameters
        ----------
        handler : Union[dict, DataHandler]
            handler could be:

            - instance of `DataHandler`

            - config of `DataHandler`.  Please refer to `DataHandler`
        """
        self.handler: DataHandler = init_instance_by_config(handler, accept_types=DataHandler)
        self.fetch_kwargs = copy(fetch_kwargs)
        super().__init__(**kwargs)

    def prepare(
        self,
        split,
        col_set=DataHandler.CS_ALL,
        **kwargs,
    ) -> Union[List[pd.DataFrame], pd.DataFrame]:
        seg_kwargs = {"col_set": col_set}
        seg_kwargs.update(kwargs)
        if hasattr(self, "fetch_kwargs"):
            return self.handler.fetch(split, **seg_kwargs, **self.fetch_kwargs)
        else:
            return self.handler.fetch(split, **seg_kwargs)






