from model.log import Log
import random
import datetime


def generate(quantity, user):
    logs = []
    now = datetime.datetime.now()
    one_year_ago = now - datetime.timedelta(days=365)
    count = 0
    while count < quantity:
        logs.append(Log(__calculate_radom_date__(one_year_ago, now), user.nickname))
        count += 1
    return logs


def __calculate_radom_date__(start, end):
    return start + (end - start) * random.random()

# Autor: José Luiz de Godoi Neto
