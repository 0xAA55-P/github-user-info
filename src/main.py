from rich import print
from utils import *
import requests
import json

def show_menu():
    username: str = input("\n[INPUT] Nome de usuario (-1 para sair): ")

    if username == "-1": # exit
        raise KeyboardInterrupt()

    data = []
    user_data = get_info(username)

    if bool(user_data) == False: # dicionario vazio: False
        print("[red][ERRO] Usuario não existe.[/]")
    else:
        print_info(user_data)

def main():
    while True:
        try:
            show_menu()

        except requests.exceptions.HTTPError:
            print("[yellow][AVISO][/] Limite de requisições. Faça uma pausa.")
            break

        except KeyboardInterrupt:
            print("\n[green][SAIDA][/] Adeus!\n")
            break

        except ValueError:
            print("\n[red][ERRO][/] Valor invalido.")

if __name__ == "__main__":
    main()
