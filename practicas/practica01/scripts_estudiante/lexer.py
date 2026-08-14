"""Analizador léxico independiente para IMP e IMP++."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from lark import Lark, Token
from lark.exceptions import UnexpectedCharacters


RUTA_GRAMATICA = Path(__file__).with_name("imp.lark")


def construir_lexer() -> Lark:
    """Construye el lexer a partir de la especificación local."""
    gramatica = RUTA_GRAMATICA.read_text(encoding="utf-8")
    return Lark(
        gramatica,
        parser=None,
        lexer="basic",
        propagate_positions=True,
    )


def tokenizar(codigo_fuente: str) -> list[Token]:
    """Devuelve, en orden, los tokens del código fuente."""
    return list(construir_lexer().lex(codigo_fuente))


def mostrar_tokens(tokens: list[Token]) -> None:
    """Muestra tipo, lexema y posición de cada token."""
    print(f"{'TIPO':<10} {'LEXEMA':<16} POSICIÓN")
    for token in tokens:
        print(f"{token.type:<10} {str(token)!r:<16} {token.line}:{token.column}")


def leer_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analizador léxico de IMP++")
    parser.add_argument("archivo", type=Path, help="archivo fuente con extensión .imp")
    return parser.parse_args()


def main() -> int:
    argumentos = leer_argumentos()
    codigo_fuente = argumentos.archivo.read_text(encoding="utf-8")

    try:
        mostrar_tokens(tokenizar(codigo_fuente))
    except UnexpectedCharacters as error:
        print(
            f"Error léxico en línea {error.line}, columna {error.column}: "
            f"{error.char!r}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
