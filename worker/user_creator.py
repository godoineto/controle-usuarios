from model.user import User
from worker import log_generate
from repository import user_repository as repository
from repository import log_repository


def execute():
    print("===================================================")
    print("=============== CADASTRO DE USUARIO ===============")
    print("===================================================")
    name = input(" DIGITE O NOME COMPLETO DO USUARIO: ")
    nickname = input(" DIGITE O NOME REDUZIDO DO USUARIO: ")
    role = input(" DIGITE O CARGO DO USUARIO: ")
    print(" ==========================")
    print(" ==== NIVEIS DE ACESSO ====")
    print(" 1 - VISITANTE")
    print(" 2 - USUARIO")
    print(" 3 - ADMINISTRATIVO")
    print(" 4 - TECNICO")
    print(" 5 - SUPER-USUARIO")
    level = input(" ESCOLHA O NIVEL DE ACESSO: ")
    user_found = repository.find_by_nickname(nickname)
    if user_found is None:
        new_user = User(name, nickname, role, level)
        repository.add(new_user)
        log_repository.add(log_generate.generate(3650, new_user))
        print(" USUARIO CADASTRADO COM SUCESSO!")
    else:
        print(" ERRO! JA EXISTE USUARIO CADASTRADO COM ESTE NOME REDUZIDO.")

# Autor: José Luiz de Godoi Neto
