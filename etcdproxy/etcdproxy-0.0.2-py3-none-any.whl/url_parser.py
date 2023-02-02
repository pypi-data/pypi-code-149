from urllib.parse import urlparse, parse_qsl
from typing import Dict, Union, ItemsView, TypedDict, Optional, Sequence, Literal


class EtcdConnParams(TypedDict, total=False):
    host: str
    port: int
    user: str
    password: str
    timeout: int
    ca_cert: str
    cert_key: str
    cert_cert: str
    grpc_options: ItemsView[str, Union[str, int]]
    options: Dict[str, Union[str, int]]


class ParserResult(TypedDict, total=False):
    aio: bool
    conn_params: EtcdConnParams
    key: str
    is_prefix: bool


def etcdurl_parser(url: str) -> ParserResult:
    """解析etcd路径.

    schema为`etcd`返回的`aio`字段为False,为`etcd+async`返回的`aio`字段为True,其他都为非法.
    url中host,port,user,password部分对应etcd中对应内容
    url中的path会被作为返回的`key`字段,如果其首字符为`/`则会被去掉,
    当返回中有key时如果在url的参数部分设置is_prefix=true则返回的`is_prefix`会被置为True,否则置为False,
    `ca_cert`, `cert_key`, `cert_cert`和`timeout`也在url的参数部分设置,其他的参数则会作为grpc参数传入
    其他的连接参数可以在url的参数部分设置

    Args:
        url (str): etcd的地址,注意请以`etcd://`或者`etcd+async://`开头

    Raises:
        AttributeError: schema 必须为etcd

    Returns:
        Dict[bool,str,bool, Union[str, int, Dict[str, str]]]: 初始化etcd客户端的参数数据,分别为是否为
    """
    conn_str_params = ("ca_cert", "cert_key", "cert_cert")
    conn_int_params = ("timeout",)
    aio: bool = False
    key: Optional[str] = None
    is_prefix: Optional[bool] = None

    conn_params: EtcdConnParams = {
        "host": '127.0.0.1',
        "port": 2379,
    }
    parse_result = urlparse(url)
    schema = parse_result.scheme.lower()
    if schema not in ("etcd", "etcd+async"):
        raise AttributeError("schema 必须为etcd")
    if schema == "etcd+async":
        aio = True
    if parse_result.username:
        conn_params.update({"user": parse_result.username})
    if parse_result.password:
        conn_params.update({"password": parse_result.password})
    if parse_result.port:
        conn_params.update({"port": parse_result.port})
    if parse_result.hostname:
        conn_params.update({"host": parse_result.hostname})
    if parse_result.path:
        if parse_result.path not in ("", "/"):
            if parse_result.path.startswith("/"):
                key = parse_result.path[1:]
            else:
                key = parse_result.path
    if parse_result.query:
        sql_result = dict(parse_qsl(parse_result.query))
        _grpc_options: Dict[str, Union[str, int]] = {}
        if key is not None:
            is_prefix = False
        for k, v in sql_result.items():
            if k == "is_prefix" and key is not None:
                print("444")
                print(v)
                if v.lower() == "false" or v == "0":
                    is_prefix = False
                else:
                    is_prefix = True
            elif k in conn_str_params:
                conn_params[k] = v  # type: ignore
            elif k in conn_int_params:
                conn_params.update({k: int(v)})  # type: ignore
            else:
                if v.isdigit():
                    _grpc_options.update({k: int(v)})
                else:
                    _grpc_options.update({k: v})
        if _grpc_options:
            if aio:
                conn_params.update({"options": _grpc_options})
            else:
                grpc_options = _grpc_options.items()
                conn_params.update({"grpc_options": grpc_options})
    result: ParserResult = {
        "aio": aio,
        "conn_params": conn_params
    }
    if key is not None:
        result.update({
            "key": key
        })
    if is_prefix is not None:
        result.update({
            "is_prefix": is_prefix
        })
    return result
