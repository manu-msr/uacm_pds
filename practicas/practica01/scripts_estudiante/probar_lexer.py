"""Controlador de línea de comandos para observar el lexer de IMP."""

from __future__ import annotations

import argparse
from pathlib import Path

from lark.exceptions import UnexpectedCharacters

from lexer_imp import analizar_fuente, construir_tabla_localidades


def argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Muestra los tokens producidos para un archivo de IMP."
    )
    parser.add_argument("archivo", type=Path, help="archivo fuente que se analizará")
    parser.add_argument(
        "--tabla",
        action="store_true",
        help="muestra también la tabla inicial de localidades",
    )
    return parser.parse_args()


def mostrar_tokens(tokens: list) -> None:
    print(f"{'tipo':<12} {'lexema':<16} {'línea':>6} {'columna':>8}")
    print("-" * 46)
    for token in tokens:
        print(
            f"{token.type:<12} {str(token)!r:<16} "
            f"{token.line:>6} {token.column:>8}"
        )


def mostrar_tabla(tabla: dict[str, dict[str, int]]) -> None:
    print("\nTabla inicial de localidades")
    print(f"{'lexema':<16} {'primera posición':<18} {'apariciones':>11}")
    print("-" * 49)
    for lexema, datos in tabla.items():
        posicion = f"{datos['primera_linea']}:{datos['primera_columna']}"
        print(f"{lexema:<16} {posicion:<18} {datos['apariciones']:>11}")


def main() -> int:
    opciones = argumentos()
    texto = opciones.archivo.read_text(encoding="utf-8")

    try:
        tokens = analizar_fuente(texto)
    except UnexpectedCharacters as error:
        print(
            f"Error léxico en línea {error.line}, columna {error.column}: "
            f"{error.get_context(texto).strip()}"
        )
        return 1

    mostrar_tokens(tokens)

    if opciones.tabla:
        try:
            tabla = construir_tabla_localidades(tokens)
        except NotImplementedError as error:
            print(f"\nPendiente: {error}")
            return 2
        mostrar_tabla(tabla)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
