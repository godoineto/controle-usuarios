from model.level import Level


class User:

    def __init__(self, name, nickname, role, level):
        self.name = name
        self.nickname = nickname
        self.role = role
        self.level = Level(int(level))

    def __repr__(self):
        return str(self.__dict__)

# Autor: José Luiz de Godoi Neto

