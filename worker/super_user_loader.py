from model.level import Level
from repository import user_repository as repository


def execute():
    print("===================================================")
    print("============= TODOS OS SUPER-USUARIOS =============")
    print("===================================================")
    users_found = repository.find_by_level(Level.SUPER_USUARIO)
    for user in users_found:
        print(user)
        print(" TOTAL: " + str(len(users_found)))
    if not users_found:
        print(" NENHUM SUPER-USUARIO CADASTRADO!")

# Autor: José Luiz de Godoi Neto
