import email
import re
from flask import Flask, request
import sqlalchemy
import responses
import crud
from models import Users
from sqlalchemy import and_
import logs
from sqlalchemy.exc import SQLAlchemyError
from psycopg2.errors import UniqueViolation
import smtplib
import passwords
import hashlib, uuid
app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']

    result = crud.get_query(Users, Users.username == username)

    if result is not None:
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        if result.password == hashed_password:
            if result.status:
                return responses.login('already_logged_in', f"{username} has already been logged in.")
            else:
                crud.update_login(username)
                logs.login_success(username)
                return responses.login('ok', f"{username} is logged in.")
        else:
            logs.login_fail_wp(username)
            return responses.login('wrong_password', f"wrong password!")
    logs.login_fail_dne(username)
    return responses.login('no_user', f'this account does not exist.')


@ app.route("/logout")
def logout():

    username = request.args.get('username')
    result = crud.get_query(Users, Users.username == username)

    if result is not None:
        if result.status == False:
            return responses.logout('already_logout', f"{username} has already been logged out.")
        else:
            crud.update_logout(username)
            logs.logout(username)
            return responses.logout('ok', f"{username} is logged out.")
    return responses.logout('no_user', f'this account does not exist.')


@ app.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    _email = request.form['email']

    try:
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

        crud.insert(username, hashed_password, _email)
        result = crud.get_query(Users, username == username)

        logs.register_success(result.id)
        return responses.register('ok', f"your account has been successfully made")\

    except SQLAlchemyError as e:
        if type(e.__dict__['orig']) is UniqueViolation:
            logs.register_fail(
                None, f"{username}, {_email}: {e.__dict__['orig']}")
            return responses.register('exist_user', f"this username or email has already been taken, please try again.")
        else:
            return e


@ app.route("/edit_np", methods=["PATCH"])
def edit_np():
    user_old = request.form['username']
    passw = request.form['password']
    user_new = request.form['newusername']

    result_old = crud.get_query(Users, Users.username == user_old)
    result_new = crud.get_query(Users, Users.username == user_new)
    if result_old is not None:
        if result_old.password == passw:
            if result_new is None:
                crud.update_edit_np(user_old, user_new)
                logs.edit_success(user_old)
                return responses.edit('ok', f"your username has changed to {user_new}")
            else:
                logs.edit_fail_ue(user_old)
                return responses.edit('exist_user', f"this username has already been taken.")
        else:
            logs.edit_fail_wp(user_old)
            return responses.edit('wrong_password', f"wrong password!")

    logs.edit_fail_dne(username=user_old)
    return responses.edit('no_user', f'this account does not exist.')


@ app.route("/reset/password", methods=["POST"])
def request_reset_password():
    username = request.form['username']
    _email = request.form['email']

    result = crud.get_query(Users, and_(
        Users.username == username, Users.email == _email)
    )

    if result is not None:
        email_password = passwords.email_password
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login("sarinaheshmati.test@gmail.com", email_password)
            message = f"hello! \n if you want to change your password use the following link, if not ignore this email. \n http://127.0.0.1:5000/reset/password?param={username}///{_email}"
            smtp.sendmail("sarinaheshmati.test@gmail.com",
                          _email, message)
            smtp.quit()
            return 'done successfully'
        except Exception as ex:
            return ("Something went wrong....", ex)

    else:
        return responses.edit('no_user', f'this account does not exist.')


@ app.route("/reset/password")
def reset_password():

    param = request.args.get('param')
    param = param.split('///')
    result = crud.get_query(Users,  and_(
        Users.username == param[0], Users.email == param[1]))

    if result is not None:
        return f'http://127.0.0.1:5000/change/password?username={param[0]}&password='
    else:
        return responses.edit('no_user', f'this account does not exist.')


@ app.route("/change/password")
def change_password():

    username = request.args.get('username')
    password = request.args.get('password')
    result = crud.get_query(Users, Users.username == username)
    if result is not None:
        crud.update_edit_p(username, password)
        return ("your password has been updated.")
    else:
        return responses.edit('no_user', f'this account does not exist.')


if __name__ == '__main__':
    app.run()
