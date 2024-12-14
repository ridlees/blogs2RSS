#!/bin/python3

import requests as r
from bs4 import BeautifulSoup as bs


def get(url):
    page = r.get(url)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

class articleEntry:
    def __init__(self, title, ahref):
        self.title = title
        self.ahref = ahref

def parse_articles(page, subtype):
    entries = []
    if subtype == "tjan":
        section = page.find('section')
        for article in section.find_all("a"):
            entry = articleEntry(article.text,article.get("href"))
            entries.append(entry)
        return entries    
    if subtype == "skvrnami":
        section = page.find("div", class_="posts-list")
        for article in section.find_all("a"):
            entry = articleEntry(article.text,article.get("href"))
            entries.append(entry)
        return entries
    if subtype == "kocour":
        for p in page.find_all("p"):
            article = p.find("a")
            entry = articleEntry(article.text,article.get("href"))
            entries.append(entry)
        return entries

def get_articles(url, subtype):
    page = soup(get(url))
    entries = parse_articles(page, subtype)
    return entries
    
if __name__ == "__main__":
    urls = ["https://tjarnikova.github.io/cti.html","https://skvrnami.github.io/log","http://blog.kocourovo.eu"]
    articles1 = get_articles(urls[0],"tjan")
    for article in articles1:
        print(article.title)
    articles2 = get_articles(urls[1],"skvrnami")
    for article in articles2:
        print(article.title)
    articles3 = get_articles(urls[2], "kocour")
    for article in articles3:
        print(article.title)
