import user_repository as repository


def execute():
    print("===================================================")
    print("================= DELETAR USUARIO =================")
    print("===================================================")
    nickname = input(" QUAL O NOME REDUZIDO DO USUARIO PARA DELETAR? ")
    user_to_remove = repository.find_by_nickname(nickname)
    if user_to_remove is None:
        print(" NAO EXISTE USUARIO COM ESTE NOME REDUZIDO!")
    else:
        repository.delete(user_to_remove)
        print(" USUARIO REMOVIDO COM SUCESSO!")
