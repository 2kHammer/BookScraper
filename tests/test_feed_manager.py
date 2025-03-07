import unittest
import time
import random
from book_scraper.models.book import Shelf, Book
from book_scraper.feed_manager.feed_fetcher import fetch_goodreads
from book_scraper.feed_manager.feed_parser import parse_goodreads
from book_scraper.models.reader import Reader, ReaderBook


class TestFeedFetcher(unittest.TestCase):
    def test_fetching(self):
        test_ids = [u for u in range(1, 6)]
        for id in test_ids:
            try:
                link, books_parsed = fetch_goodreads(1, Shelf.READ)
                time.sleep(2)
                print(str(id) + " passed")
            except Exception as e:
                print(str(id) + " failed")
                self.fail(e)

    def test_invaliduserid(self, invalid_id=220):
        try:
            links, books_parsed = fetch_goodreads(invalid_id, Shelf.READ)
            self.assertEqual(books_parsed, None)
        except Exception as e:
            self.fail(e)


def fetch_parse(id):
    link, books_parsed = fetch_goodreads(id, Shelf.WANT_TO_READ)
    reader = None
    books = None
    if books_parsed != None:
        reader, books = parse_goodreads(id, books_parsed, link)
    return reader, books


class TestFeedParser(unittest.TestCase):
    def test_normalfeed(self, id=596):
        link, books_parsed = fetch_goodreads(id, Shelf.READ)
        reader, books = parse_goodreads(id, books_parsed, link)
        self.assertIsInstance(reader, Reader)
        for rb in reader.books:
            self.assertIsInstance(rb.id, int)
            self.assertIsInstance(rb, ReaderBook)
        for b in books:
            self.assertIsInstance(b, Book)

    def test_random_ids(self):
        rand_ids = [random.randint(1, 1000) for i in range(0, 5)]
        for id in rand_ids:
            time.sleep(2)
            print("Test for id: " + str(id))
            reader, books = fetch_parse(id)
            if reader != None:
                self.assertIsInstance(reader, Reader)
                for rb in reader.books:
                    self.assertIsInstance(rb.id, int)
                    self.assertIsInstance(rb, ReaderBook)
                for b in books:
                    self.assertIsInstance(b, Book)
