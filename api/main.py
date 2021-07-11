from flask import Flask
from api_methods import DbHandler

app = Flask(__name__)

handler = DbHandler()

@app.route('/all_articles')
def all_articles():
    return handler.sql_to_response('select * from articles')

@app.route('/last_article')
def last_articles():
    return handler.sql_to_response('select * from articles order by date desc limit 1')
