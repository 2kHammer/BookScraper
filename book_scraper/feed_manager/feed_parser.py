import re
from book_scraper.models.book import *
from book_scraper.models.reader import Reader
from book_scraper.utils.type_converter import convert_to_int


def parse_goodreads(reader_id, rated_books_parsed_xml, current_link):
    books=[]
    current_reader = None
    reader_name = ""
    current_shelf = Shelf.UNDEFINED
    name_shelf_pattern = r"(.*)'s bookshelf: (read|currently-reading|to-read)"

    #get title and name of the reader
    title = rated_books_parsed_xml.find(".//title").text
    match = re.match(name_shelf_pattern, title)
    if match:
        reader_name, current_shelf = match.groups()
    current_reader = Reader(reader_id,reader_name)
    current_reader.add_url(current_link)

    # get books
    items_bookshelf = rated_books_parsed_xml.findall(".//item")
    for index, book in enumerate(items_bookshelf):
        title = book.find(".//title").text
        id = int(book.find(".//book_id").text)
        description = book.find(".//book_description").text
        num_pages = convert_to_int(book.find(".//num_pages").text)
        isbn = book.find(".//isbn").text
        avg_rating = float(book.find(".//average_rating").text)
        published = convert_to_int(book.find(".//book_published").text)
        author_name = book.find(".//author_name").text
        books.append(Book(title,id,description,num_pages,isbn,avg_rating,published,author_name))
        rating = float(book.find(".//user_rating").text)
        current_reader.add_book(id, title, rating, Shelf.get_shelf(current_shelf))

    return current_reader, books