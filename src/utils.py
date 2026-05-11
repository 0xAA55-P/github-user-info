"""Utilitários principais para o programa

"""

from rich import print as bprint
import requests

def get_info(name: str) -> dict | None:
    """Pega as informações do usuário

    Args:
        name: Nome de usuário

    Returns:
        JSON formatado com as informações se o usuário existir
        None se ocorrer algum erro com a API

    Raises:
        requests.Timeout: Caso a api leve 5 segundos para responder
        requests.exceptions.HTTPError: Limite de requisições atingido
        ValueError: Resposta Vazia da API
    """

    try:
        resp = requests.get(f"https://api.github.com/users/{name}", timeout=5)
        resp.raise_for_status()

        if not resp.content:
            raise ValueError("\n[red][ERRO][/] Resposta vazia do servidor.")

        result = resp.json()

        return result

    except requests.exceptions.HTTPError:
        bprint("\n[yellow][AVISO][/] Limite de requisições. Faça uma pausa.")
        return None

    except requests.Timeout:
        bprint("\n[yellow][AVISO][/] Tempo limite de resposta excedido.")
        return None

def print_info(user_data: dict) -> None:
    if user_data.get("name") is None:
        bprint("\nNome de usuario não disponivel.")
    else:
        bprint(f"\nNome: {user_data.get('name')}")

    bprint(f"ID: {user_data.get('id')}")
    bprint(f"Seguidores: {user_data.get('followers')}")
    bprint(f"Repositorios publicos: {user_data.get('public_repos')}")
