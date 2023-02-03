import time
import functools


def ttl_lru_cache(ttl, maxsize=128, typed=False):
    """
    增加过期时间的lru缓存装饰器
    """

    def _decorator(fn):
        start = time.time()

        def get_salt():
            delta = time.time() - start
            return int(delta / ttl)

        @functools.lru_cache(maxsize=maxsize, typed=typed)
        def _new(*args, __time_salt, **kwargs):
            return fn(*args, **kwargs)

        @functools.wraps(fn)
        def _wrapped(*args, **kwargs):
            return _new(*args, **kwargs, __time_salt=get_salt())

        return _wrapped

    return _decorator
