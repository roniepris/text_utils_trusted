from typing import List


def inverter_texto(texto: str) -> str:
    """Retorna o texto invertido."""
    return texto[::-1]


def contar_palavras(texto: str) -> int:
    """Conta o número de palavras em uma string."""
    return len(texto.split())


def remover_espacos_extras(texto: str) -> str:
    """Remove espaços duplicados."""
    return " ".join(texto.split())


def para_snake_case(texto: str) -> str:
    """Converte texto para snake_case."""
    return texto.strip().lower().replace(" ", "_")


def dividir_linhas(texto: str) -> List[str]:
    """Divide texto em linhas."""
    return texto.splitlines()
