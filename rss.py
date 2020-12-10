import requests
from bs4 import BeautifulSoup
import re
import feedparser

class arxiv:

    def __init__(self):
        self.url='http://arxiv.org/rss/cs/'
    
    def get_recent(self, tag):
        url=self.url+tag
        feed=feedparser.parse(url)
        items=feed.entries
        
        titles=[item['title'] for item in items]
        abstracts=[item['summary'] for item in items]
        links=[item['link'] for item in items]
        
        return titles, abstracts, links

class news:
    def __init__(self):
        self.url='https://news.google.com/rss/topics/'
    def get_recent(self, topic):
        url=self.url+topic+'?hl=en-US'
        feed=feedparser.parse(url)
        items=feed.entries
        
        titles=[item['title'] for item in items]
        links=[item['link'] for item in items]

        return titles, links