from flask import Flask, request
import responses
import crud
from models import Users
from sqlalchemy import and_
import logs
app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.form['username']
    passw = request.form['password']

    result = crud.get_query(Users, Users.username == user)

    if result is not None:
        if result.password == passw:
            if result.status:
                return responses.login('already_logged_in', f"{user} has already been logged in.")
            else:
                crud.update_login(user)
                logs.login_success(user)
                return responses.login('ok', f"{user} is logged in.")
        else:
            logs.login_fail_wp(user)
            return responses.login('wrong_password', f"wrong password!")
    logs.login_fail_dne(user)
    return responses.login('no_user', f'this account does not exist.')


@ app.route("/logout")
def logout():
    user = request.args.get('username')
    result = crud.get_query(Users, Users.username == user)
    if result is not None:
        if result.status == False:
            return responses.logout('already_logout', f"{user} has already been logged out.")
        else:
            crud.update_logout(user)
            logs.logout(user)
            return responses.logout('ok', f"{user} is logged out.")
    return responses.logout('no_user', f'this account does not exist.')


@ app.route("/register", methods=["POST"])
def register():
    user = request.form['username']
    passw = request.form['password']
    eemail = request.form['email']
    result = crud.get_query(Users, Users.username == user)
    result_e = crud.get_query(Users, Users.email == eemail)
    if result is not None and result_e != None:
        logs.register_fail(user)
        return responses.register('exist_user', f"this username or email has already been taken, please try again.")

    else:
        logs.register_success(user)
        crud.insert(user, passw, eemail)
        return responses.register('ok', f"your account has been successfully made")


@ app.route("/edit", methods=["PATCH"])
def edit():
    user_old = request.form['username']
    passw_old = request.form['password']
    user_new = request.form['newusername']
    passw_new = request.form['newpassword']

    result_old = crud.get_query(Users, Users.username == user_old)
    result_new = crud.get_query(Users, Users.username == user_new)
    if result_old is not None:
        if result_old.password == passw_old:
            if result_new is None:
                crud.update_edit(user_old, user_new, passw_new)
                logs.edit_success(user_old)
                return responses.edit('ok', f"your username has changed to {user_new} and your password has been updated.")
            else:
                logs.edit_fail_ue(user_old)
                return responses.edit('exist_user', f"this username has already been taken.")
        else:
            logs.edit_fail_wp(user_old)
            return responses.edit('wrong_password', f"wrong password!")

    logs.edit_fail_dne(username=user_old)
    return responses.edit('no_user', f'this account does not exist.')


if __name__ == '__main__':
    app.run()
