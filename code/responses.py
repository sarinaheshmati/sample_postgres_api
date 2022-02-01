def login(type, message):
    print(type + "\n" + message)
    return {'code': {
        'ok': 1000,
        'wrong_password': 1001,
        'no_user': 1002,
        'already_logged_in': 1003,
        'requird_inputs': 1005
    }[type], 'message': message}


def logout(type, message):
    return {'code': {
        'ok': 2000,
        'already_logout': 2001,
        'no_user': 2002,
        'requird_inputs': 2005
    }[type], 'message': message}


def register(type, message):
    return {'code': {
        'ok': 3000,
        'exist_user': 3001,
        'required_inputs': 3005
    }[type], 'message': message}


def edit(type, message):
    return {'code': {
        'ok': 4000,
        'wrong_password': 4001,
        'exist_user': 4003,
        'no_user': 4002,
        'required_inputs': 4005
    }[type], 'message': message}
