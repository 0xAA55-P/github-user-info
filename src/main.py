"""Github User Info

Programa simples para exibir algumas informações de um usuário do github

Dev: Anna
Github: https://github.com/0xAA55-P
Data de Atualização: 11/05/2026

"""

from rich import print as bprint
from utils import print_info, get_info

def show_menu():
    username: str = input("\n[INPUT] Nome de usuario (-1 para sair): ")

    if username == "-1": # exit
        raise KeyboardInterrupt()

    user_data = get_info(username)

    if user_data is not None:
        print_info(user_data)

def main():
    while True:
        try:
            show_menu()

        except KeyboardInterrupt:
            bprint("\n[green][SAIDA][/] Adeus!\n")
            break

        except ValueError:
            bprint("\n[red][ERRO][/] Valor invalido.")

if __name__ == "__main__":
    main()
