from repository import log_repository as repository


def execute():
    print("===================================================")
    print("=============== VISUALIZAR ACESSOS ================")
    print("===================================================")
    date_to_search = input(" DIGITE UMA DATA (DD-MM-AAAA): ")
    repository.search_logs_by_date(date_to_search)

# Autor: José Luiz de Godoi Neto
