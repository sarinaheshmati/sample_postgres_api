import datetime

x = datetime.datetime.now()


def login(username):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} was logged in.\n")


def logout(username):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} was logged out.\n")
    # with open('files/users.txt', "a+") as h:
    #     for z in h:
    #         s = z.split(" ")
    #         h.write(s[2] == 0)


def try_login(username):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} tried to log in with wrong password.\n")


def no_login(username, password):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: attack was detected by {username}, {password}.\n")


def register(username, password):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} made an account, password: {password}.\n")


def register_denied(username):
    with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} registery was denied, the account already exists.\n")

def edit(username, newusername):
   with open("files/logs.txt", "a+") as f:
        f.write(f"{x}: {username} changed its username to {newusername}.\n")
