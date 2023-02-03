"""
实现 Requests 基类封装
"""
from multidict import CIMultiDict
from yarl import URL


__all__ = ["BaseSesssion"]


# User-Agnet
UA_ANDROID  = "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"
UA_WINDOWNS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
UA_MAC      = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
UA_IPHONE   = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
UA_IPAD     = "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
UA_SYMBIAN  = "Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba"
UA_APAD     = "Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"

UA_ALL = CIMultiDict({
    "android" : UA_ANDROID,
    "windows" : UA_WINDOWNS,
    "mac"     : UA_MAC,
    "iphone"  : UA_IPHONE,
    "ipad"    : UA_IPAD,
    "symbian" : UA_SYMBIAN,
    "apad"    : UA_APAD
})


def get_user_agent(user_agent, overwrite=False):
    """
    获取 UserAgent
    """
    if not isinstance(user_agent, str):
        raise ValueError(
            f"\033[31minvalid user_agent: '{user_agent}', "
            f"type: '{type(user_agent).__name__}'\033[0m")
    return user_agent if overwrite is True else UA_ALL.getone(user_agent, UA_ANDROID)


def default_headers():
    """
    默认 Headers
    """
    headers = (
        ("User-Agent", get_user_agent("android")),
    )
    return CIMultiDict(headers)



class BaseSesssion:
    """
    pip install requests
    对 requests 封装基类
    """

    # 默认超时时间
    DEFAULT_TIMEOUT = 7

    def __init__(
        self,
        base_url: str or URL=None,
        headers: dict or CIMultiDict=None,
        timeout: int or float=None,
        verify: bool=True,
    ):
        self._base_url = base_url
        self._headers  = headers
        self._timeout  = timeout
        self._verify   = bool(verify)
        self.__initialization_attr()


    def __initialization_attr(self):
        self.__init_base_url()
        self.__init_headers()
        self.__init_timeout()


    def __init_base_url(self):
        base_url = getattr(self, "_base_url", None)
        if not base_url:
            setattr(self, "_base_url", None)
            return

        # base_url 格式错误
        if not isinstance(base_url, (str, URL)):
            raise TypeError(
                "\033[31m'base_url' type must be a 'str' or 'URL', "
                f"not '{type(base_url).__name__}'\033[0m")

        # 只有绝对路径 url 才能是base_url
        base_url = URL(str(base_url))
        if base_url.is_absolute():
            setattr(self, "_base_url", base_url)
        else:
            setattr(self, "_base_url", None)


    def __init_headers(self, overwrite=False):
        raw_headers = CIMultiDict() if overwrite is True else default_headers()
        headers = getattr(self, "_headers", None)
        if headers:
            headers = CIMultiDict(headers)
        else:
            headers = CIMultiDict()
        raw_headers.update(headers)
        setattr(self, "_headers", raw_headers)


    def __init_timeout(self):
        timeout = getattr(self, "_timeout", self.DEFAULT_TIMEOUT)
        if (
            not isinstance(timeout, (int, float))
            or timeout <= 0
        ):
            timeout = self.DEFAULT_TIMEOUT
        setattr(self, "_timeout", timeout)


    def build_url(
        self, url: str or URL, raw: bool=False
    ) -> str or URL:
        """
        构建完整 url, base_url=None 将抛出错误
        raw=True 返回字符串
        """
        if isinstance(url, str):
            url = URL(url)

        elif not isinstance(url, URL):
            raise TypeError(
                "\033[31m'url' type must be a 'str' or 'URL', "
                f"not '{type(url).__name__}'\033[0m"
            )

        if not url.is_absolute():
            if self.base_url is None:
                raise ValueError(f"\033[31murl '{url}' not absolute\033[0m")
            url = self._base_url.join(url)
        # 原生数据
        if raw:
            url = str(url)
        return url


    @property
    def base_url(self):
        if not hasattr(self, "_base_url"):
            setattr(self, "_base_url", None)
        base_url = getattr(self, "_base_url")
        if base_url:
            base_url = str(base_url)
        return base_url

    @base_url.setter
    def base_url(self, value):
        setattr(self, "_base_url", value)
        self.__init_base_url()

    @property
    def headers(self):
        if not hasattr(self, "_headers"):
            setattr(self, "_headers", CIMultiDict())
        return getattr(self, "_headers")

    @headers.setter
    def headers(self, value):
        setattr(self, "_headers", value)
        self.__init_headers(overwrite=True)

    @property
    def timeout(self):
        if not hasattr(self, "_timeout"):
            setattr(self, "_timeout", self.DEFAULT_TIMEOUT)
        return getattr(self, "_timeout")

    @timeout.setter
    def timeout(self, value):
        setattr(self, "_timeout", value)
        self.__init_timeout()
