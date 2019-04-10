from repository import user_repository as repository


def execute():
    print("===================================================")
    print("=============== USUARIOS POR NIVEL ================")
    print("===================================================")
    print(" 1 - VISITANTE")
    print(" 2 - USUARIO")
    print(" 3 - ADMINISTRATIVO")
    print(" 4 - TECNICO")
    print(" 5 - SUPER-USUARIO")
    level = input(" POR QUAL NIVEL DE ACESSO DESEJA PESQUISAR? ")
    users_found = repository.find_by_level(int(level))
    for user in users_found:
        print(user)
        print(" TOTAL: " + str(len(users_found)))
    if not users_found:
        print(" NENHUM USUARIO CADASTRADO NESTE NIVEL!")


# Autor: José Luiz de Godoi Neto
