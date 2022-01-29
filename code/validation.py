
# def check(username, password):
#     with open("files/users.txt", "r") as f:
#         for x in f.readlines():
#             s = x.split(" ")
#             if s[0] == username:
#                 if s[1] == password:
#                     return 1
#                 else:
#                     return 2
#             s = 0
#         return 0


def exist(username):
    with open("files/users.txt", "r") as f:
        for x in f:
            s = x.split(" ")
            if s[0] == username:
                return 1
            s = 0
        return 0
