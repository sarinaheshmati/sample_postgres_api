#import queue
#from shutil import register_unpack_format
from sqlalchemy import create_engine, true, select
from models import Base
from config import DATABASE_URI
import sqlalchemy as db
from models import Users, Logs

engine = create_engine(DATABASE_URI)


Base.metadata.create_all(engine)

connection = engine.connect()


def insert():
    query = db.insert(Users)
    values_list = [{'username': 'u3', 'password': 'p3', 'email': 'u3@u3.com', 'enable': 1, 'status': 0},
                   {'username': 'u2', 'password': 'p2', 'email': 'u2@u2.com', 'enable': 1, 'status': 0}]
    h = connection.execute(query, values_list)


def get_query(table_name, where_clause):
    query = connection.execute(select(table_name).where(where_clause))

    return query.fetchone()


def update():
    query = db.update(Users).values(username='u5')
    query = query.where(Users.id == 38)
    results = connection.execute(query)
