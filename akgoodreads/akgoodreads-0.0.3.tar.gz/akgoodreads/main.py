import requests
import time
from akgoodreads.gr_parser import GoodreadsParser
from akgoodreads.log import AKLog
from akgoodreads.credentials import getpwd
from akgoodreads.definitions import Book, Author

class Goodreads:
    def __init__(self, email:str, sec_bet_req:float=1, debug:bool = False) -> None:
        self.key = getpwd('goodreads', email)
        self.sec_bet_req = sec_bet_req

        self.log = AKLog()
        if debug:
            self.log.set_debug()
        s = requests.Session()

        self._update_last_request()
        s.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        self.s = s

        self.parser = GoodreadsParser(self.log)

    def __repr__(self) -> str:
        apikey = self.key
        sec_bet_req = self.sec_bet_req
        return f"Goodreads({apikey=}, {sec_bet_req=})"
    
    @property
    def nxt_req(self):
        return self.last_request + self.sec_bet_req
    
    def _update_last_request(self):
        self.last_request = time.time()
        self.log.debug(f'{self.last_request=}')

    def request(self, path:str, params: dict={}):
        if not 'key' in params.keys():
            params['key'] = self.key
        result = gr_req(self.log, f"https://www.goodreads.com/{path}", params, self.s, self.nxt_req)
        self._update_last_request()
        return result

    def author(self, name: str) -> Author:
        #https://www.goodreads.com/api/index#search.authors
        result = self.request(f"api/author_url/{name}")
        author_id = self.parser.author_id(result)
        return self._author_from_id(author_id)

    def _author_from_id(self, id:int) -> Author:
        log = self.log
        log.debug(f"Requsting Author with goodreads ID: {id}")
        result = self.request(f"author/show/{id}")
        return self.parser.author(result)

    def _book_from_id(self, id:int) -> Book:
        log = self.log
        log.debug(f"Requsting Book with goodreads ID: {id}")
        result = self.request(f"book/show/{id}")
        return self.parser.book(result)

    def book(self, name: str, limit:int=None) -> list[Book]:
        """Returns book info from the specified query term. `limit` limits the # of match returned, max 20
        """
        result = self.request('search/index.xml', params={'q':name})
        book_ids = self.parser.book_ids_from_query(result)
        if not limit:
            limit = len(book_ids)-1
        return [self._book_from_id(id) for id in book_ids[:limit]]


def gr_req(log, url: str, params:dict ={}, session = None, next_request: float = None):
    log.debug(f"{next_request=}, {time.time()=}")
    if next_request:
        while next_request - time.time() > 0:
            time.sleep(0.1)
    if session:
        log.debug(f"Sending Sessions request to url:{url} with parameters: {params}")
        req = session.get(url, params=params)
    else:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        log.debug(f"Sending standalone request to url:{url} with parameters: {params}")
        req = requests.get(url, params=params, headers=headers)
    req.raise_for_status()
    return req