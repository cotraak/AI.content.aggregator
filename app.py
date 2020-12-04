from paperscrape import arxiv
import re
from flask import render_template, Flask
from newsscrape import news

app=Flask(__name__)

titles, abstracts, plinks=arxiv().get_recent('cs.AI')
titles=[re.sub('. \(.*\)', '', title) for title in titles]
news,nlinks=news().get_recent('CAAqIAgKIhpDQkFTRFFvSEwyMHZNRzFyZWhJQ1pXNG9BQVAB')

@app.route('/')
def homepage():
    return render_template('index.html', papers=titles, plink=plinks, news=news, nlink=nlinks)

@app.route('/papers')
def paperspage():
    return render_template('papers.html', papers=titles, plink=plinks)

@app.route('/news')
def newspage():
    return render_template('news.html', news=news, nlink=nlinks)

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=80)