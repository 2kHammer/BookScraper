from enum import Enum

class Shelf(Enum):
    READ = "read"
    WANT_TO_READ = "to-read"
    CURRENTLY_READING = "currently-reading"
    UNDEFINED = ""


    def get_shelf(shelf_description):
        if shelf_description == "read":
            return Shelf.READ
        elif shelf_description == "to-read":
            return Shelf.WANT_TO_READ
        elif shelf_description == "currently-reading":
            return Shelf.CURRENTLY_READING

class Book:
    def __init__(self, title,id, description, num_pages, isbn, avg_rating, year_published, author_name):
        self.title = title
        self.id = id
        self.description = description
        self.num_pages = num_pages
        self.isbn = isbn
        self.avg_rating = avg_rating
        self.year_published = year_published
        self.author_name = author_name
