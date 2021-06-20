from flask import Flask
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)


#change for your POSTGRES credentials
POSTGRES_USER = ''
POSTGRES_PASSWORD = ''
POSTGRES_ADDRES = ''
POSTGRES_DATABASE = ''

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(POSTGRES_USER,POSTGRES_PASSWORD,
                                                              POSTGRES_ADDRES,POSTGRES_DATABASE))
connection = engine.connect()

@app.route('/all_articles')
def all_articles():
    data = pd.read_sql('select * from articles',connection)
    result = data.to_json(orient="records")
    return result