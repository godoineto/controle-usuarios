import datetime
logs = []


def add(new_logs):
    logs.extend(new_logs)


def search_logs_by_date(date_to_search):
    start_converted = __format_date__(date_to_search, 00, 00, 00)
    end_converted = __format_date__(date_to_search, 23, 59, 59)
    logs_found = list(filter(lambda log: start_converted <= log.access <= end_converted, logs))
    logs_found.sort(key=lambda log: log.access)
    print(*logs_found)


def __format_date__(date, hour, minute, second):
    return datetime.datetime.strptime(date, "%d-%m-%Y").replace(hour=hour, minute=minute, second=second)

# Autor: José Luiz de Godoi Neto
