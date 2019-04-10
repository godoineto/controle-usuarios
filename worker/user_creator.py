from model.user import User
import user_repository as repository


def execute():
    print("===================================================")
    print("=============== CADASTRO DE USUARIO ===============")
    print("===================================================")
    name = input(" DIGITE O NOME COMPLETO DO USUARIO: ")
    nickname = input(" DIGITE O NOME REDUZIDO DO USUARIO: ")
    role = input(" DIGITE O CARGO DO USUARIO: ")
    repository.add(User(name, nickname, role, ""))
