class Log:

    def __init__(self, datetime, user_nickname):
        self.user_nickname = user_nickname
        self.datetime = datetime

    def __repr__(self):
        return str(self.__dict__)

# Autor: José Luiz de Godoi Neto
