from dataclasses import dataclass

@dataclass
class Book:
    id: int
    isbn: int
    isbn13: int
    title: str
    image: str
    link: str
    pages: int
    publish_year: int
    rating: float
    num_ratings: int
    desc: str
    authors: list[int]

@dataclass
class Author:
    id: int
    name: str
    link: str
    image: str
    works: int
    hometown: str
    in_goodreads: bool
    books: list[int]