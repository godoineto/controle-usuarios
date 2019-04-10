from repository import user_repository as repository


def execute():
    print("===================================================")
    print("=============== PROCURAR DE USUARIO ===============")
    print("===================================================")
    nickname = input(" QUAL O NICKNAME DO USUARIO QUE DESEJA ENCONTRAR? ")
    user_found = repository.find_by_nickname(nickname)
    if user_found is None:
        print(" USUARIO NAO ENCONTRADO")
    else:
        print(" USUARIO ENCONTRADO: ")
        print(str(user_found))

# Autor: José Luiz de Godoi Neto
