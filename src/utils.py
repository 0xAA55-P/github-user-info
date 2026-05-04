from rich import print
import requests

def get_info(username: str) -> dict:
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()

        if not response.content:
            raise ValueError("[red][ERRO][/] Resposta vazia do servidor.")

        result = response.json()

        return result

    except requests.exceptions.HTTPError as e:
        raise
        return {}

def print_info(user_data: dict) -> None:
    if user_data.get('name') == None:
        print(f"\nNome de usuario não disponivel.")
    else:
        print(f"\nNome: {user_data.get('name')}")

    print(f"ID: {user_data.get('id')}")
    print(f"Seguidores: {user_data.get('followers')}")
    print(f"Repositorios publicos: {user_data.get('public_repos')}")
    