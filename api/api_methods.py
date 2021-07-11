from flask import Response
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
import pandas as pd
import time
import os


class DbHandler:
    def __init__(self) -> None:
        self.connection = self._make_connection()

    def _make_connection(self) -> Connection:
        engine = create_engine(
        "postgresql+psycopg2://{}:{}@{}/{}".format(
            os.environ.get("POSTGRES_USER"),
            os.environ.get("POSTGRES_PASSWORD"),
            os.environ.get("POSTGRES_ADDRESS"),
            os.environ.get("POSTGRES_DATABASE"),
        )
    )
        connection = engine.connect()

        return connection

    def sql_to_response(self,query: str) -> Response:
        data = pd.read_sql('select * from articles',self.connection)
        json_string = data.to_json(orient="records",force_ascii=False)
        response = Response(json_string,content_type="application/json; charset=utf-8" )
        return response