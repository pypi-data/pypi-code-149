
import warnings
from typing import Callable, Union, Tuple, List, Iterator, Optional

import pandas as pd

from ...log import get_module_logger, TimeInspector
from ...utils import init_instance_by_config
from ...utils.serial import Serializable
from .utils import fetch_df_by_col
from .loader import DataLoader

from . import processor as processor_module
from . import loader as data_loader_module


class DataHandler(Serializable):
    def __init__(
        self,
        data_loader: Union[dict, str, DataLoader] = None,
        init_data=True,
        fetch_orig=True,
    ):
        # Setup data loader
        assert data_loader is not None  # to make start_time end_time could have None default value

        self.data_loader = init_instance_by_config(
            data_loader,
            None if (isinstance(data_loader, dict) and "module_path" in data_loader) else data_loader_module,
            accept_types=DataLoader,
        )


        self.fetch_orig = fetch_orig
        if init_data:
            with TimeInspector.logt("Init data"):
                self.setup_data()

        super().__init__()


    def config(self, **kwargs):
        super().config(**kwargs)

    def setup_data(self, enable_cache: bool = False):
        with TimeInspector.logt("Loading data"):
            # make sure the fetch method is based on an index-sorted pd.DataFrame
            self._data = self.data_loader.load()
        # TODO: cache


    CS_ALL = "__all"  # return all columns with single-level index column
    CS_RAW = "__raw"  # return raw data with multi-level index column

    def fetch(
        self,
        split: str,
        col_set: Union[str, List[str]] = CS_ALL,
        squeeze: bool = False,
        proc_func: Callable = None,
    ) -> pd.DataFrame:
        return self._fetch_data(
            data_storage=self._data[split],
            col_set=col_set,
            squeeze=squeeze,
            proc_func=proc_func,
        )

    def _fetch_data(
        self,
        data_storage: pd.DataFrame,
        col_set: Union[str, List[str]] = CS_ALL,
        squeeze: bool = False,
        proc_func: Callable = None,
    ):
        data_df = data_storage
        data_df = fetch_df_by_col(data_df, col_set)

        if squeeze:
            # squeeze columns
            data_df = data_df.squeeze()
            # squeeze index
            if isinstance(selector, (str, pd.Timestamp)):
                data_df = data_df.reset_index(level=level, drop=True)
        return data_df


    def get_cols(self, col_set=CS_ALL) -> list:
        df = self._data.head()
        df = fetch_df_by_col(df, col_set)
        return df.columns.to_list()


class DataHandlerLP(DataHandler):

    # data key
    DK_R = "raw"
    DK_I = "infer"
    DK_L = "learn"
    ATTR_MAP = {DK_R: "_data", DK_I: "_infer", DK_L: "_learn"}

    # process type
    PTYPE_I = "independent"
    # - self._infer will be processed by shared_processors + infer_processors
    # - self._learn will be processed by shared_processors + learn_processors

    # NOTE:
    PTYPE_A = "append"

    # - self._infer will be processed by shared_processors + infer_processors
    # - self._learn will be processed by shared_processors + infer_processors + learn_processors
    #   - (e.g. self._infer processed by learn_processors )

    def __init__(
        self,
        data_loader: Union[dict, str, DataLoader] = None,
        infer_processors: List = [],
        learn_processors: List = [],
        shared_processors: List = [],
        process_type=PTYPE_A,
        drop_raw=False,
        **kwargs,
    ):
        # Setup preprocessor
        self.infer_processors = []  # for lint
        self.learn_processors = []  # for lint
        self.shared_processors = []  # for lint
        for pname in "infer_processors", "learn_processors", "shared_processors":
            for proc in locals()[pname]:
                getattr(self, pname).append(
                    init_instance_by_config(
                        proc,
                        None if (isinstance(proc, dict) and "module_path" in proc) else processor_module,
                        accept_types=processor_module.Processor,
                    )
                )

        self.process_type = process_type
        self.drop_raw = drop_raw
        super().__init__(data_loader, **kwargs)

    
    def get_all_processors(self):
        return self.shared_processors + self.infer_processors + self.learn_processors

    def fit(self):
        for proc in self.get_all_processors():
            with TimeInspector.logt(f"{proc.__class__.__name__}"):
                proc.fit(self._data)

    def fit_process_data(self):
        self.process_data(with_fit=True)

    @staticmethod
    def _run_proc_l(
        df: pd.DataFrame, proc_l: List[processor_module.Processor], with_fit: bool, check_for_infer: bool
    ) -> pd.DataFrame:
        for proc in proc_l:
            if check_for_infer and not proc.is_for_infer():
                raise TypeError("Only processors usable for inference can be used in `infer_processors` ")
            with TimeInspector.logt(f"{proc.__class__.__name__}"):
                if with_fit:
                    proc.fit(df)
                df = proc(df)
        return df

    @staticmethod
    def _is_proc_readonly(proc_l: List[processor_module.Processor]):
        """
        NOTE: it will return True if `len(proc_l) == 0`
        """
        for p in proc_l:
            if not p.readonly():
                return False
        return True

    def process_data(self, with_fit: bool = False):
        # shared data processors
        # 1) assign
        _shared_df = self._data
        if not self._is_proc_readonly(self.shared_processors):  # avoid modifying the original data
            _shared_df = _shared_df.copy()
        # 2) process
        _shared_df = self._run_proc_l(_shared_df, self.shared_processors, with_fit=with_fit, check_for_infer=True)

        # data for inference
        # 1) assign
        _infer_df = _shared_df
        if not self._is_proc_readonly(self.infer_processors):  # avoid modifying the original data
            _infer_df = _infer_df.copy()
        # 2) process
        _infer_df = self._run_proc_l(_infer_df, self.infer_processors, with_fit=with_fit, check_for_infer=True)

        self._infer = _infer_df

        # data for learning
        # 1) assign
        if self.process_type == DataHandlerLP.PTYPE_I:
            _learn_df = _shared_df
        elif self.process_type == DataHandlerLP.PTYPE_A:
            # based on `infer_df` and append the processor
            _learn_df = _infer_df
        else:
            raise NotImplementedError(f"This type of input is not supported")
        if not self._is_proc_readonly(self.learn_processors):  # avoid modifying the original  data
            _learn_df = _learn_df.copy()
        # 2) process
        _learn_df = self._run_proc_l(_learn_df, self.learn_processors, with_fit=with_fit, check_for_infer=False)

        self._learn = _learn_df

        if self.drop_raw:
            del self._data


    def config(self, processor_kwargs: dict = None, **kwargs):
        """
        configuration of data.
        # what data to be loaded from data source

        This method will be used when loading pickled handler from dataset.
        The data will be initialized with different time range.

        """
        super().config(**kwargs)
        if processor_kwargs is not None:
            for processor in self.get_all_processors():
                processor.config(**processor_kwargs)

    # init type
    IT_FIT_SEQ = "fit_seq"  # the input of `fit` will be the output of the previous processor
    IT_FIT_IND = "fit_ind"  # the input of `fit` will be the original df
    IT_LS = "load_state"  # The state of the object has been load by pickle

    def setup_data(self, init_type: str = IT_FIT_SEQ, **kwargs):
        """
        Set up the data in case of running initialization for multiple time

        Parameters
        ----------
        init_type : str
            The type `IT_*` listed above.
        enable_cache : bool
            default value is false:

            - if `enable_cache` == True:

                the processed data will be saved on disk, and handler will load the cached data from the disk directly
                when we call `init` next time
        """
        # init raw data
        super().setup_data(**kwargs)

        with TimeInspector.logt("fit & process data"):
            if init_type == DataHandlerLP.IT_FIT_IND:
                self.fit()
                self.process_data()
            elif init_type == DataHandlerLP.IT_LS:
                self.process_data()
            elif init_type == DataHandlerLP.IT_FIT_SEQ:
                self.fit_process_data()
            else:
                raise NotImplementedError(f"This type of input is not supported")

        # TODO: Be able to cache handler data. Save the memory for data processing

    @classmethod
    def cast(cls, handler: "DataHandlerLP") -> "DataHandlerLP":
        new_hd: DataHandlerLP = object.__new__(DataHandlerLP)
        new_hd.from_cast = True  # add a mark for the cast instance

        for key in list(DataHandlerLP.ATTR_MAP.values()) + [
            "fetch_orig",
            "drop_raw",
        ]:
            setattr(new_hd, key, getattr(handler, key, None))
        return new_hd


