def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: R${value}')

def print_menu():
    print("""
    Escolha uma das opções abaixo
    1 - Saldo total por cliente
    2 - Saldo total por conta
    3 - Saldo por data
    4 - Sair
    """)