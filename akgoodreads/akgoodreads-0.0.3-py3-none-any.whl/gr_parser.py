import xmltodict
from requests.models import Response
from akgoodreads.definitions import Book, Author

class GoodreadsParser:
    def __init__(self, log):
        self.log = log

    def author_id(self, response: Response) -> int:
        """Returns a the goodreads author id from the passed response object
        """
        res = parse_response(response)
        return int(res.get('@id', 0))
    
    def author(self, response: Response) -> Author:
        """Get goodreads author details from author_id response
        """
        res = parse_response(response)
        return _parse_author_info(res)

    def book_ids_from_query(self, response) -> list[int]:
        """Returns a list of book_ids from the xml response of a query
        """
        res = parse_response(response)
        works = res['results']['work']
        return [int(work['best_book']['id']['#text']) for work in works]
    
    def book(self, response) -> Book:
        """Returns the `Book` dataclass parsed from the xml response
        """
        res = parse_response(response)
        return _parse_book_info(res)

    def __repr__(self) -> str:
        return f"GoodreadsParser()"



def parse_response(response: Response):
    res = xmltodict.parse(response.text)['GoodreadsResponse']
    request_status = res.pop('Request')
    assert request_status['authentication'] == 'true'
    assert len(res.keys()) == 1
    return list(res.values())[0]

def _parse_author_info(author: dict) -> Author:
    books = author.get('books').get('book')
    if type(books) == list:
        book_ids = [int(book['id']['#text']) for book in books]
    else:
        book_ids = [int(books['id'])]
    return Author(
            id=int(author.get('id', 0)),
            name=author.get('name', 'NA'),
            link=author.get('link', 'NA'),
            image=author.get('large_image_url',author.get('image_url',author.get('small_image_url','NA'))),
            works=int(author.get('works_count', 0)),
            hometown=author.get('hometown', 'NA'),
            in_goodreads=author.get('goodreads_author') == 'true',
            books=book_ids
        )

def _parse_book_info(book:dict) -> Book:
    authors = book.get('authors').get('author')
 
    if type(authors) == list:
        author_ids = [int(author['id']) for author in authors]
    else:        
        author_ids = [int(authors['id'])]

    return Book(
        id=int_of(book.get('id',0)),
        isbn=int_of(book.get('isbn', 0)),
        isbn13=int_of(book.get('isbn13', 0)),
        title=book.get('title', 'NA'),
        image=book.get('large_image_url',book.get('image_url',book.get('small_image_url','NA'))),
        link=book.get('link', 'NA'),
        pages=int_of(book.get('num_pages',0)),
        publish_year=int_of(book.get('publication_year', 0)),
        rating=float(book.get('average_rating', 0)),
        num_ratings=int_of(book.get('ratings_count', 0)),
        desc=book.get('description', 'NA'),
        authors=author_ids
    )


def int_of(string: str) -> int:
    try:
        return int(string)
    except:
        return 0