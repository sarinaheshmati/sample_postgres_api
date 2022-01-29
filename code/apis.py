
from flask import Flask, request
import logs
from validation import exist
import responses
app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    user = request.form['username']
    passw = request.form['password']

    with open("files/users.txt", "r") as f:
        all_users = f.readlines()

    for i, x in enumerate(all_users):
        s = x.split(" ")
        if s[0] == user:
            if s[1] == passw:
                if s[2].replace('\n', '') == '1':
                    return responses.login('already_logged_in', f"{user} has already been logged in.")
                else:
                    all_users[i] = f'{user} {s[1]} 1\n'
                    with open('files/users.txt', 'w') as f:
                        f.writelines(all_users)
                    logs.login(username=user)
                    return responses.login('ok', f"{user} is logged in.")
            else:
                logs.try_login(username=user)
                return responses.login('wrong_password', f"wrong password!")

    logs.no_login(username=user, password=passw)
    return responses.login('no_user', f'this account does not exist.')


@app.route("/logout")
def logout():
    user = request.args.get('username')

    with open("files/users.txt", "r") as f:
        all_users = f.readlines()

    for i, x in enumerate(all_users):
        s = x.split(" ")
        if s[0] == user:
            if s[2].replace('\n', '') == '0':
                return responses.logout('already_logout', f"{user} has already been logged out.")
            else:
                all_users[i] = f'{user} {s[1]} 0\n'
                with open("files/users.txt", "w") as f:
                    f.writelines(all_users)
                logs.logout(username=user)
                return responses.logout('ok', f"{user} is logged out.")
    return responses.logout('no_user', f'this account does not exist.')


@app.route("/register", methods=["POST"])
def register():
    user = request.form['username']
    passw = request.form['password']
    okk = exist(user)
    if okk == 1:
        logs.register_denied(username=user)
        return responses.register('exist_user', f"this user already exists, please try again.")

    if okk == 0:
        logs.register(username=user, password=passw)
        with open("files/users.txt", "a+") as fi:
            fi.write(f"{user} {passw}\n")
        return responses.register('ok', f"your account has been successfully made")


@app.route("/edit", methods=["PUT"])
def edit():
    user_old = request.form['username']
    passw_old = request.form['password']
    user_new = request.form['newusername']
    passw_new = request.form['newpassword']
    with open("files/users.txt", "r") as f:
        all_users = f.readlines()

    for i, x in enumerate(all_users):
        s = x.split(" ")
        if s[0] == user_old:
            if s[1] == passw_old:
                all_users[i] = f'{user_new} {passw_old} 0\n'
                with open('files/users.txt', 'w') as f:
                    f.writelines(all_users)
                logs.edit(username=user_old, newusername=user_new)
                return responses.edit('ok', f"your username has changed to {user_new} and your password has been updated.") 
            else:
                logs.try_login(username=user_old)
                return responses.edit('wrong_password', f"wrong password!")

    logs.no_login(username=user_old, password=passw_old)
    return responses.edit('no_user', f'this account does not exist.') 


if __name__ == '__main__':
    app.run()
