from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint
class news:
    def __init__(self):
        self.url='https://news.google.com/rss/topics/'
    def get_recent(self, topic):
        data=requests.get(self.url+topic+'?hl=en-US')
        soup=BeautifulSoup(data.content, 'lxml-xml')
        titles=soup.find_all('title')[1:]
        links=soup.find_all('link')[1:]
        return [title.text for title in titles], [link.text for link in links]      