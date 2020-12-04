import requests
from bs4 import BeautifulSoup
import re

class arxiv:

    def __init__(self):
        self.url='http://arxiv.org/rss/cs/'
    
    def get_recent(self, tag):
        data=requests.get(self.url+tag)
        soup=BeautifulSoup(data.content, 'lxml-xml')
        titles=[item.text for item in soup.find_all('title')[2:]]
        abstracts=[item.text for item in soup.find_all('description')[1:]]
        links=[item.text for item in soup.find_all('link')[2:]]
        
        return titles, abstracts, links