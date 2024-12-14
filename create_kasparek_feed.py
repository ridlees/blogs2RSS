#!/bin/python3

import requests as r
from bs4 import BeautifulSoup as bs
from feedgen.feed import FeedGenerator
import datetime


def get(url):
    page = r.get(url)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

class articleEntry:
    def __init__(self, title, ahref):
        self.title = title
        self.ahref = ahref

def parse_articles(page):
    fg = FeedGenerator()
    fg.id("003")
    fg.title("Unoficial Kašpárek RSS feed")
    fg.link(href='http://example.com', rel='alternate')
    fg.description("Unoficial RSS feed for michalkasparek.cz created by Martin K.")
    
    h2s = page.find_all('h2')
    h2s.reverse()
    
    for h2 in h2s:
        text = []
        for tag in h2.next_siblings:
            if tag.name == 'h2':
                fe = fg.add_entry()
                fe.id(h2.text)
                fe.title(h2.text)
                fe.content("\n".join(text))
                break
            elif tag.name == 'p' or tag.name == "blockquote":
                text.append(str(tag))
    atomfeed = fg.atom_str(pretty=True)
    rssfeed  = fg.rss_str(pretty=True)
    fg.atom_file('kasparek-atom.xml')
    fg.rss_file('kasparek-rss.xml')

def get_articles(url):
    page = soup(get(url))
    parse_articles(page)
    
if __name__ == "__main__":
    url = "https://michalkasparek.cz/vypisky.html"
    get_articles(url)
    
    
    now = datetime.datetime.now()
    print(f"{now} - fetched Kašparek")
