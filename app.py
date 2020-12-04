from paperscrape import arxiv
import re
from flask import render_template, Flask

app=Flask(__name__)

titles, abstracts, links=arxiv().get_recent('cs.AI')
titles=[re.sub('. \(.*\)', '', title) for title in titles]

@app.route('/')
def homepage():
    return render_template('index.html', papers=titles, plink=links, news=['#']*10)

@app.route('/papers')
def paperspage():
    return render_template('papers.html', papers=titles, plink=links)

@app.route('/news')
def newspage():
    return render_template('news.html', news=['#']*10)

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=80)