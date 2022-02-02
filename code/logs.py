from distutils.log import Log
from re import T
from sqlalchemy import create_engine, select
from models import Base
from config import DATABASE_URI
import sqlalchemy as db
from models import Users, Logs
import datetime
import crud

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
connection = engine.connect()


def login_success(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'login', 'status': True,
                    'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def login_fail_wp(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'login', 'status': False,
                    'description': 'wrong password', 'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def login_fail_dne(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'login', 'status': False,
                    'description': 'user does not exist', 'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def logout(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'logout', 'status': True,
                    'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def register_fail(user_id, description):
    query = db.insert(Logs)
    values_list = [{'user_id': user_id, 'action': 'register', 'status': False,
                    'description': description, 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def register_success(user_id):
    query = db.insert(Logs)
    values_list = [{'user_id': user_id, 'action': 'register', 'status': True,
                    'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def edit_success(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'edit', 'status': True,
                    'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def edit_fail_wp(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'edit', 'status': False,
                    'description': 'wrong password', 'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def edit_fail_dne(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'edit', 'status': False,
                   'description': 'user does not exist', 'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)


def edit_fail_ue(username):
    result = crud.get_query(Users, Users.username == username)
    query = db.insert(Logs)
    values_list = [{'user_id': result.id, 'action': 'edit', 'status': False,
                    'description': 'new username is taken', 'type': 'user', 'timestamp': datetime.datetime.now()}]
    results = connection.execute(query, values_list)
