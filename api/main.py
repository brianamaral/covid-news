from flask import Flask
from sqlalchemy import create_engine
import pandas as pd
import time
import os


app = Flask(__name__)

engine = create_engine(
    "postgresql+psycopg2://{}:{}@{}/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_ADDRESS"),
        os.environ.get("POSTGRES_DATABASE"),
    )
)

connection = engine.connect()

@app.route('/all_articles')
def all_articles():
    data = pd.read_sql('select * from articles',connection)
    result = data.to_json(orient="records")
    return result

@app.route('/last_article')
def last_articles():
    data = pd.read_sql('select * from articles order by date desc limit 1',connection)
    result = data.to_json(orient="records")
    return result
