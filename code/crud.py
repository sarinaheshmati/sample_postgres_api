#import queue
#from shutil import register_unpack_format
from sqlalchemy import create_engine, select
from models import Base
from config import DATABASE_URI
import sqlalchemy as db
from models import Users, Logs

engine = create_engine(DATABASE_URI)


Base.metadata.create_all(engine)

connection = engine.connect()


def insert(username, password, email):
    query = db.insert(Users)
    values_list = [{'username': username,
                    'password': password, 'email': email}]
    h = connection.execute(query, values_list)


def get_query(table_name, where_clause):
    query = connection.execute(select(table_name).where(where_clause))
    return query.fetchone()


def update_login(old_user):
    query = db.update(Users).values(status=True)
    query = query.where(Users.username == old_user)
    results = connection.execute(query)


def update_logout(old_user):
    query = db.update(Users).values(status=False)
    query = query.where(Users.username == old_user)
    results = connection.execute(query)


def update_edit(old_user, new_user, new_passw):
    query = db.update(Users).values(username=new_user, password=new_passw)
    query = query.where(Users.username == old_user)
    results = connection.execute(query)

