import requests
from bs4 import BeautifulSoup
import re
import feedparser
import collections

class arxiv:

    def __init__(self):
        self.url='http://arxiv.org/rss/cs/cs.AI'
    
    def get_recent(self):
        feed=feedparser.parse(self.url)
        items=feed.entries
        
        titles=[item['title'] for item in items]
        abstracts=[item['summary'] for item in items]
        links=[item['link'] for item in items]
        titles=[re.sub(r'\. \(.*?\)', '', title) for title in titles]
        

        return list(zip(titles, [x.replace('<p>','').replace('</p>','') for x in abstracts], links))

class news:

    def __init__(self):
        self.urls={'Google news':'https://news.google.com/rss/topics/CAAqIAgKIhpDQkFTRFFvSEwyMHZNRzFyZWhJQ1pXNG9BQVAB?hl=en-US', 
        'DeepMind':'https://deepmind.com/blog/feed/basic/',
        'Wired':'https://www.wired.com/feed/category/science/latest/rss',
        'MachineLearningMastery':'http://machinelearningmastery.com/blog/feed',
        'OpenAI': 'https://openai.com/blog/rss/',
        'AWS':'https://aws.amazon.com/blogs/ai/feed',
        'Ibenta Blog':'https://www.inbenta.com/en/blog/feed',
        'TDS': 'https://towardsdatascience.com/feed'}
    
    def get_recent(self):
        feed={}
        res=collections.defaultdict(list)
        for source, url in self.urls.items():
            feed=feedparser.parse(url)
            items=feed.entries

            for item in items:
                temp={}
                temp['title']=item['title']
                temp['link']=item['link']
                temp['time']=item['published_parsed']
                res[source].append(temp)
        t=[]
        count=0
        for s,r in res.items():
            t.extend(r)
        temp_res=list(sorted(t, key=lambda x: x['time'], reverse=True))
        return temp_res[:20], res
