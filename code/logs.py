from distutils.log import Log
from re import T
from sqlalchemy import create_engine, select
from models import Base
from config import DATABASE_URI
import sqlalchemy as db
from models import Users, Logs
import datetime
import crud

x = datetime.datetime.now()

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)

connection = engine.connect()


def login_success(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'login', 'status': True,
                    'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def login_fail_wp(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'login', 'status': False,
                    'description': 'wrong password', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def login_fail_dne(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'login', 'status': False,
                    'description': 'user does not exist', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def logout(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'logout', 'status': True,
                    'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def register_fail(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'register', 'status': False,
                    'description': 'username or password is taken', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def register_success(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'register', 'status': True,
                    'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def edit_success(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'edit', 'status': True,
                    'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def edit_fail_wp(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'edit', 'status': False,
                    'description': 'wrong password', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def edit_fail_dne(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'edit', 'status': False,
                   'description': 'user does not exist', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)


def edit_fail_ue(old_user):
    result = crud.get_query(Users, Users.username == old_user)
    query = db.insert(Logs)
    values_list = [{'user_id':result.id , 'action': 'edit', 'status': False,
                    'description': 'new username is taken', 'type': 'user', 'timestamp': x}]
    results = connection.execute(query, values_list)
