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
        titles=[re.sub(r'\. \(.*?\)', '', title) for title in titles]
        

        return list(zip(titles, [x.replace('<p>','').replace('</p>','') for x in abstracts], links))

class news:
    def __init__(self):
        self.url='https://news.google.com/rss/topics/'
    def get_recent(self, topic):
        url=self.url+topic+'?hl=en-US'
        feed=feedparser.parse(url)
        items=feed.entries
        
        titles=[item['title'] for item in items]
        links=[item['link'] for item in items]

        return list(zip(titles, links))