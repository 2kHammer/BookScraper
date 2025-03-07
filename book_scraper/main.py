from models.book import Book, Shelf
from feed_manager.feed_fetcher import fetch_goodreads
from feed_manager.feed_parser import parse_goodreads

reader_id = 8
current_link, rated_books_parsed_xml = fetch_goodreads(reader_id, Shelf.READ)
reader, books = parse_goodreads(reader_id,rated_books_parsed_xml,current_link)
print(reader.name)
