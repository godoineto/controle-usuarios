from worker import user_creator
from worker import user_finder
from worker import super_user_loader
from worker import user_deleter
from worker import level_user_loader
from worker import program_closer


def fodeo():
    print("fodeo")


def run(option):
    return {
        1: user_creator,
        2: user_finder,
        3: super_user_loader,
        4: user_deleter,
        5: level_user_loader,
        6: fodeo,
        7: program_closer
    }.get(option, 7).execute()


