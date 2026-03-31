"""
Pacote: text_utils
Ferramentas para manipulação de texto.
"""

from .formatacao import (
    inverter_texto,
    contar_palavras,
    remover_espacos_extras,
    para_snake_case,
    dividir_linhas,
)

__all__ = [
    "inverter_texto",
    "contar_palavras",
    "remover_espacos_extras",
    "para_snake_case",
    "dividir_linhas",
]

__version__ = "0.1.0"
