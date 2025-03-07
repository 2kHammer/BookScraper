from dataclasses import dataclass
from book_scraper.models.book import Shelf

@dataclass
class ReaderBook:
    id: int
    title: str
    rating: float
    shelf: Shelf

class Reader:
    def __init__(self,id,name=""):
        self.id = id
        self.name = name
        self.books = []
        self.urls = []

    def add_book(self, id, title, rating, shelf):
        self.books.append(ReaderBook(id,title,rating,shelf))

    def add_url(self, url):
        self.urls.append(url)