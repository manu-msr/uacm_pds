"""Punto de partida del analizador léxico de IMP.

La primera versión reconoce únicamente localidades y omite espacios. Completa la
especificación siguiendo los TODO de la guía; no agregues construcciones que no estén
en la tabla léxica aprobada.
"""

from __future__ import annotations

from collections.abc import Iterable

from lark import Lark, Token


GRAMATICA_LEXICA = r"""
// Versión mínima funcional.
LOC: /[A-Za-z]+[0-9]*/

// TODO 5.2: agrega NUM. El signo se conserva como token MINUS separado.
// TODO 5.3: agrega las palabras reservadas con prioridad mayor que LOC y
// un limite que impida cortar localidades como if2 o ifX.
// TODO 5.4: agrega operadores, asignación, secuenciación y paréntesis.

%import common.WS
%ignore WS
"""


def construir_lexer() -> Lark:
    """Construye un lexer independiente, sin analizador sintáctico."""
    return Lark(GRAMATICA_LEXICA, parser=None, lexer="basic")


def analizar_fuente(texto: str) -> list[Token]:
    """Consume todo el texto y devuelve los tokens producidos."""
    return list(construir_lexer().lex(texto))


def construir_tabla_localidades(
    tokens: Iterable[Token],
) -> dict[str, dict[str, int]]:
    """Registra la primera posición y el número de apariciones de cada LOC.

    TODO 6.2:
    - omite los tokens cuyo tipo no sea LOC;
    - usa el lexema como llave;
    - conserva primera_linea, primera_columna y apariciones;
    - incrementa apariciones cuando la localidad ya exista.
    """
    raise NotImplementedError("Completa construir_tabla_localidades en el paso 6.2")
