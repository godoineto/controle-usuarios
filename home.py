import time
import worker_factory as runner


def show_menu():
    print("===================================================")
    print("=============== CONTROLE DE USUARIO ===============")
    print("===================================================")
    print(" 1 - CADASTRAR USUARIO ")
    print(" 2 - PESQUISAR USUARIO ")
    print(" 3 - LISTAR SUPER USUARIOS ")
    print(" 4 - DELETAR USUARIO ")
    print(" 5 - LISTAR USUARIOS PELO NIVEL DE ACESSO ")
    print(" 6 - FODEO ;'( ")
    print(" 7 - SAIR ")
    print("===================================================")
    return int(input(" SELECIONE UMA OPCAO: "))


def validate(option):
    valid_options = [1, 2, 3, 4, 5, 6, 7]
    if option in valid_options:
        runner.run(option)
    else:
        print(" OPCAO INVALIDA. POR FAVOR, SELECIONE UMA OPCAO VALIDA.")


def start():
    option = 0
    while option != 7:
        option = show_menu()
        validate(option)
        time.sleep(1)


start()


