import re
from flask import render_template, Flask
from rss import news, arxiv

app=Flask(__name__)

papers=arxiv().get_recent()
latest_news, news=news().get_recent()

@app.route('/')
def homepage():
    return render_template('index.html', papers=papers[:20], temp_res=latest_news)

@app.route('/papers')
def paperspage():
    return render_template('papers.html', papers=papers)

@app.route('/news')
def newspage():
    return render_template('news.html', news=news)

@app.route('/about')
def aboutpage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=80)