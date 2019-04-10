import user_repository as repository


def execute():
    print("===================================================")
    print("=============== PROCURAR DE USUARIO ===============")
    print("===================================================")
    nickname = input(" QUAL O NICKNAME DO USUARIO QUE DESEJA ENCONTRAR? ")
    user_found = next(filter(lambda user: user.nickname == nickname, repository.list_all()), None)
    print(str(user_found.name))
