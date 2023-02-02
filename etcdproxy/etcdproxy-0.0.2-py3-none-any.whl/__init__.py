
from pyproxypattern import Proxy
from typing import Optional, Any
from .url_parser import etcdurl_parser, EtcdConnParams


class EtcdProxy(Proxy):
    """etcd的代理类."""
    __slots__ = ('instance', "_callbacks", "_instance_check", "aio")

    def __init__(self, *, conn_params: Optional[EtcdConnParams] = None, aio: bool = False, url: Optional[str] = None) -> None:
        """初始化一个etcd代理.

        Args:
            url (Optional[str], optional): etcd的url路径,注意schema为`etcd`或`etcd+async`. Defaults to None.
        """

        if url:
            instance = self.new_instance_from_url(url)
            super().__init__(instance)
        elif conn_params:
            instance = self.new_instance(conn_params, aio=aio)
            super().__init__(instance)
        else:
            super().__init__()

    def new_instance(self, conn_params: EtcdConnParams, *, aio: bool = False) -> Any:
        if aio:
            self.aio = True
            import aetcd
            return aetcd.Client(**conn_params)
        else:
            self.aio = False
            import etcd3
            return etcd3.client(**conn_params)

    def initialize_from_params(self, conn_params: EtcdConnParams, *, aio: bool = False) -> None:
        """使用参数初始化etcd连接实例

        Args:
            conn_params (EtcdConnParams): 连接参数
            aio (bool, optional): 是否使用异步接口. Defaults to False.
        """
        instance = self.new_instance(conn_params, aio=aio)
        self.initialize(instance)

    def new_instance_from_url(self, url: str) -> Any:
        urlinfo = etcdurl_parser(url)
        return self.new_instance(urlinfo["conn_params"], aio=urlinfo["aio"])

    def initialize_from_url(self, url: str) -> None:
        """从url初始化."""
        instance = self.new_instance_from_url(url)
        self.initialize(instance)
