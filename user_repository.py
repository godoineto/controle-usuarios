from model.level import Level
users = []


def add(new_user):
    users.append(new_user)


def find_by_nickname(nickname):
    return next(filter(lambda user: user.nickname == nickname, users), None)


def find_by_level(level):
    level = Level(level)
    return list(filter(lambda user: user.level == level, users))


def delete(user_to_remove):
    users.remove(user_to_remove)
