from akgoodreads.main import *
import pytest

class TestGoodreads:
    client = Goodreads('rpakishore@gmail.com')

    def test__author_from_id(self):
        response = self.client._author_from_id(18541)
        assert response.id == 18541
        assert response.name != "NA"
        assert response.link != "NA"
        assert response.image != "NA"
        assert response.works >= 70
        assert response.hometown == "Cork"
        assert type(response.in_goodreads) == bool
        assert 2581204 in response.books

    def test_author(self):
        response = self.client.author('James A. Michener')
        assert response.id == 7995

    def test_book(self):
        response = self.client.book("Ender's Game", limit=2)
        assert len(response) == 2
        book = response[0]
        assert type(book.id) == int
        assert book.link != "NA"
        assert book.image != "NA"
        assert "Ender’s Game" in book.title

        book = response[1]
        assert type(book.id) == int
        assert book.title != "NA"
        assert book.link != "NA"
        assert book.image != "NA"

    def test__book_from_id(self):
        response = self.client._book_from_id(50)
        assert response.id == 50
        assert response.isbn == 689840926
        assert response.isbn13 == 9780689840920
        assert response.title == "Hatchet (Brian's Saga, #1)"
        assert len(response.image) > 15
        assert response.link == 'https://www.goodreads.com/book/show/50.Hatchet'
        assert response.pages == 208
        assert response.publish_year == 2000
        assert response.rating == 3.76
        assert response.num_ratings == 343233
        assert len(response.desc) > 50
        assert response.authors == [18]
        
