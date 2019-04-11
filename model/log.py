

class Log:

    def __init__(self, access, user_nickname):
        self.user_nickname = user_nickname
        self.access = access

    def __format_date__(self):
        return self.access.strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        return str("\n USUARIO: " + self.user_nickname + " ACESSOU EM: " + self.access.strftime("%d/%m/%Y %H:%M"))

# Autor: José Luiz de Godoi Neto
