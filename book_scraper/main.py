import os
import random
from dotenv import load_dotenv

from book_scraper.db.connection import close_db
from book_scraper.db.insert import insert_reader, insert_books, check_reader_in_db
from db.connection import get_db
from models.book import Book, Shelf
from feed_manager.feed_fetcher import fetch_goodreads
from feed_manager.feed_parser import parse_goodreads
from utils.logger import Logger

def fetch_full_reader(reader_id):
    links = {}
    xml_parsed = {}
    books = {}
    reader = {}
    databooks = []

    for shelf in Shelf:
        if shelf != shelf.UNDEFINED:
            links[shelf.value], xml_parsed[shelf.value] = fetch_goodreads(reader_id, shelf)

            if xml_parsed[shelf.value] is not None:
                reader[shelf.value], books[shelf.value] = parse_goodreads(reader_id, xml_parsed[shelf.value],links[shelf.value])
                databooks.extend(reader[shelf.value].books)

    if (len(databooks) > 0):
        reader[Shelf.READ.value].books = databooks
        reader[Shelf.READ.value].urls = list(links.values())
        books = sum(books.values(), [])
        return reader[Shelf.READ.value], books
    else:
        logger.debug("Fetching the reader " + str(reader_id) + " is not possible")
        return None, None


#Load the .env file
load_dotenv()
logger = Logger.init_logger(os.getenv("LOG_DIR"))
logger.info("Application started")

#database
db, client = get_db()

while True:
    try:
        id = random.randint(1,100000000)
        reader, books = fetch_full_reader(id)
        if reader:
            insert_reader(reader, db)
            if (len(books) > 0):
                amount_inserted, amount_already_in_db = insert_books(books, db)
                logger.info("Reader " + str(id) + " inserted: "+ str(amount_inserted) + " books were inserted, " + str(amount_already_in_db) + " were already in db")
    except Exception as e:
        logger.error("Fatal error:" + str(e))

close_db(client)



