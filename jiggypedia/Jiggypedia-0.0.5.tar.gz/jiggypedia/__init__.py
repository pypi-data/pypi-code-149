

from .jiggy_session import ClientError, ServerError
from .query import  QueryRequest, EmbeddingModel

from .jiggy_session import JiggySession
from .query import  search as _search



def _wikipedia_search():
    jiggysession = JiggySession('jiggypedia-v0')
    def __search(*kargs, **kwargs):
        return _search(jiggysession, *kargs, **kwargs)
    return __search


wikipedia_search = _wikipedia_search()


def _deprecated_search():
    from loguru import logger
    jiggysession = JiggySession('jiggypedia-v0')
    def __search(*kargs, **kwargs):
        return _search(jiggysession, *kargs, **kwargs)
    return __search


search = _deprecated_search()



def _edgar_search():
    jiggysession = JiggySession('edgar-v0')
    def __search(*kargs, **kwargs):
        return _search(jiggysession, *kargs, **kwargs)
    return __search

    
edgar_search = _edgar_search()
