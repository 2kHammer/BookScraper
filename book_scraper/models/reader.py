from dataclasses import dataclass
from book_scraper.models.book import Shelf

@dataclass
class ReaderBook:
    id: int
    title: str
    rating: float #only values 1-5, 0 means -> not rated
    shelf: Shelf

    def mongo_dict(self):
        return {"id": self.id, "title": self.title, "rating": self.rating, "shelf": self.shelf.value}


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