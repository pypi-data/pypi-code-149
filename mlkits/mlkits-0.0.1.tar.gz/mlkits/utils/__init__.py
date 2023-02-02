import sys
import importlib
import pandas as pd
from typing import List, Dict, Union, Tuple, Any, Optional, Callable
from types import ModuleType
from pathlib import Path

__all__ = ["Literal", "TypedDict", "final"]

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict, final  # type: ignore  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal, TypedDict, final


class InstDictConf(TypedDict):
    """
    InstDictConf  is a Dict-based config to describe an instance

        case 1)
        {
            'class': 'ClassName',
            'kwargs': dict, #  It is optional. {} will be used if not given
            'model_path': path, # It is optional if module is given in the class
        }
        case 2)
        {
            'class': <The class it self>,
            'kwargs': dict, #  It is optional. {} will be used if not given
        }
    """

    # class: str  # because class is a keyword of Python. We have to comment it
    kwargs: dict  # It is optional. {} will be used if not given
    module_path: str  # It is optional if module is given in the class


InstConf = Union[InstDictConf, str, object, Path]


def get_module_by_module_path(module_path: Union[str, ModuleType]):
    """Load module path

    :param module_path:
    :return:
    :raises: ModuleNotFoundError
    """
    if module_path is None:
        raise ModuleNotFoundError("None is passed in as parameters as module_path")

    if isinstance(module_path, ModuleType):
        module = module_path
    else:
        if module_path.endswith(".py"):
            module_name = re.sub("^[^a-zA-Z_]+", "", re.sub("[^0-9a-zA-Z_]", "", module_path[:-3].replace("/", "_")))
            module_spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(module_spec)
            sys.modules[module_name] = module
            module_spec.loader.exec_module(module)
        else:
            module = importlib.import_module(module_path)
    return module


def split_module_path(module_path: str) -> Tuple[str, str]:
    """

    Parameters
    ----------
    module_path : str
        e.g. "a.b.c.ClassName"

    Returns
    -------
    Tuple[str, str]
        e.g. ("a.b.c", "ClassName")
    """
    *m_path, cls = module_path.split(".")
    m_path = ".".join(m_path)
    return m_path, cls


def get_callable_kwargs(config: InstConf, default_module: Union[str, ModuleType] = None) -> (type, dict):
    """
    extract class/func and kwargs from config info

    Parameters
    ----------
    config : [dict, str]
        similar to config
        please refer to the doc of init_instance_by_config

    default_module : Python module or str
        It should be a python module to load the class type
        This function will load class from the config['module_path'] first.
        If config['module_path'] doesn't exists, it will load the class from default_module.

    Returns
    -------
    (type, dict):
        the class/func object and it's arguments.

    Raises
    ------
        ModuleNotFoundError
    """
    if isinstance(config, dict):
        key = "class" if "class" in config else "func"
        if isinstance(config[key], str):
            # 1) get module and class
            # - case 1): "a.b.c.ClassName"
            # - case 2): {"class": "ClassName", "module_path": "a.b.c"}
            m_path, cls = split_module_path(config[key])
            if m_path == "":
                m_path = config.get("module_path", default_module)
            module = get_module_by_module_path(m_path)

            # 2) get callable
            _callable = getattr(module, cls)  # may raise AttributeError
        else:
            _callable = config[key]  # the class type itself is passed in
        kwargs = config.get("kwargs", {})
    elif isinstance(config, str):
        # a.b.c.ClassName
        m_path, cls = split_module_path(config)
        module = get_module_by_module_path(default_module if m_path == "" else m_path)

        _callable = getattr(module, cls)
        kwargs = {}
    else:
        raise NotImplementedError(f"This type of input is not supported")
    return _callable, kwargs


def init_instance_by_config(
    config: InstConf,
    default_module=None,
    accept_types: Union[type, Tuple[type]] = (),
    try_kwargs: Dict = {},
    **kwargs,
) -> Any:
    """
    get initialized instance with config

    Parameters
    ----------
    config : InstConf

    default_module : Python module
        Optional. It should be a python module.
        NOTE: the "module_path" will be override by `module` arguments

        This function will load class from the config['module_path'] first.
        If config['module_path'] doesn't exists, it will load the class from default_module.

    accept_types: Union[type, Tuple[type]]
        Optional. If the config is a instance of specific type, return the config directly.
        This will be passed into the second parameter of isinstance.

    try_kwargs: Dict
        Try to pass in kwargs in `try_kwargs` when initialized the instance
        If error occurred, it will fail back to initialization without try_kwargs.

    Returns
    -------
    object:
        An initialized object based on the config info
    """
    if isinstance(config, accept_types):
        return config

    if isinstance(config, (str, Path)):
        if isinstance(config, str):
            # path like 'file:///<path to pickle file>/obj.pkl'
            pr = urlparse(config)
            if pr.scheme == "file":
                with open(os.path.join(pr.netloc, pr.path), "rb") as f:
                    return pickle.load(f)
        else:
            with config.open("rb") as f:
                return pickle.load(f)

    klass, cls_kwargs = get_callable_kwargs(config, default_module=default_module)

    try:
        return klass(**cls_kwargs, **try_kwargs, **kwargs)
    except (TypeError,):
        # TypeError for handling errors like
        # 1: `XXX() got multiple values for keyword argument 'YYY'`
        # 2: `XXX() got an unexpected keyword argument 'YYY'
        return klass(**cls_kwargs, **kwargs)


def lazy_sort_index(df: pd.DataFrame, axis=0) -> pd.DataFrame:
    """
    make the df index sorted

    df.sort_index() will take a lot of time even when `df.is_lexsorted() == True`
    This function could avoid such case

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame:
        sorted dataframe
    """
    idx = df.index if axis == 0 else df.columns
    if (
        not idx.is_monotonic_increasing
        or not is_deprecated_lexsorted_pandas
        and isinstance(idx, pd.MultiIndex)
        and not idx.is_lexsorted()
    ):  # this case is for the old version
        return df.sort_index(axis=axis)
    else:
        return df


def fill_placeholder(config: dict, config_extend: dict):
    """
    Detect placeholder in config and fill them with config_extend.
    The item of dict must be single item(int, str, etc), dict and list. Tuples are not supported.
    There are two type of variables:
    - user-defined variables :
        e.g. when config_extend is `{"<MODEL>": model, "<DATASET>": dataset}`, "<MODEL>" and "<DATASET>" in `config` will be replaced with `model` `dataset`
    - variables extracted from `config` :
        e.g. the variables like "<dataset.kwargs.segments.train.0>" will be replaced with the values from `config`

    Parameters
    ----------
    config : dict
        the parameter dict will be filled
    config_extend : dict
        the value of all placeholders

    Returns
    -------
    dict
        the parameter dict
    """
    # check the format of config_extend
    for placeholder in config_extend.keys():
        assert re.match(r"<[^<>]+>", placeholder)

    # bfs
    top = 0
    tail = 1
    item_queue = [config]
    while top < tail:
        now_item = item_queue[top]
        top += 1
        if isinstance(now_item, list):
            item_keys = range(len(now_item))
        elif isinstance(now_item, dict):
            item_keys = now_item.keys()
        for key in item_keys:
            if isinstance(now_item[key], (list, dict)):
                item_queue.append(now_item[key])
                tail += 1
            elif isinstance(now_item[key], str):
                if now_item[key] in config_extend.keys():
                    now_item[key] = config_extend[now_item[key]]
                else:
                    m = re.match(r"<(?P<name_path>[^<>]+)>", now_item[key])
                    if m is not None:
                        now_item[key] = get_item_from_obj(config, m.groupdict()["name_path"])
    return config


def auto_filter_kwargs(func: Callable, warning=True) -> Callable:
    """
    this will work like a decoration function

    The decrated function will ignore and give warning when the parameter is not acceptable

    For example, if you have a function `f` which may optionally consume the keywards `bar`.
    then you can call it by `auto_filter_kwargs(f)(bar=3)`, which will automatically filter out
    `bar` when f does not need bar

    Parameters
    ----------
    func : Callable
        The original function

    Returns
    -------
    Callable:
        the new callable function
    """

    def _func(*args, **kwargs):
        spec = inspect.getfullargspec(func)
        new_kwargs = {}
        for k, v in kwargs.items():
            # if `func` don't accept variable keyword arguments like `**kwargs` and have not according named arguments
            if spec.varkw is None and k not in spec.args:
                if warning:
                    log.warning(f"The parameter `{k}` with value `{v}` is ignored.")
            else:
                new_kwargs[k] = v
        return func(*args, **new_kwargs)

    return _func


