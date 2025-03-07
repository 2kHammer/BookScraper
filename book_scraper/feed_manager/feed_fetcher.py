import requests
import xml.etree.ElementTree as ET

base_link = "https://www.goodreads.com/review/list_rss/"
shelf_link = "?shelf="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_goodreads(reader_id, shelf):
    link_to_fetch = base_link+ str(reader_id)+ shelf_link + shelf.value
    rated_books_request = requests.get(link_to_fetch, headers=headers)
    if rated_books_request.status_code == 200:
        #print(rated_books_request.text)
        rated_books_parsed_xml = ET.fromstring(rated_books_request.text)
    else:
        rated_books_parsed_xml = None
    return link_to_fetch, rated_books_parsed_xml
