from flask import Flask
from api_methods import DbHandler

app = Flask(__name__)

handler = DbHandler()

@app.route('/all_articles')
def all_articles():
    return handler.sql_to_response('select * from articles')
'''
@app.route('/last_article')
def last_articles():
    data = pd.read_sql('select * from articles order by date desc limit 1',connection)
    json_string = data.to_json(orient="records",force_ascii=False)
    response = Response(json_string,content_type="application/json; charset=utf-8" )
    return response
'''