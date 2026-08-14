"""Pruebas de regresión para el lexer funcional de IMP."""

from __future__ import annotations

import unittest

from lark.exceptions import UnexpectedCharacters

from lexer import tokenizar


def tipos_y_lexemas(codigo_fuente: str) -> list[tuple[str, str]]:
    return [(token.type, str(token)) for token in tokenizar(codigo_fuente)]


class PruebasLexerBase(unittest.TestCase):
    def test_asignacion_aritmetica(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("X := X + 2;"),
            [
                ("LOC", "X"),
                ("ASSIGN", ":="),
                ("LOC", "X"),
                ("PLUS", "+"),
                ("NUM", "2"),
                ("SEMI", ";"),
            ],
        )

    def test_palabra_reservada_y_localidad(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("if if2 then skip"),
            [("IF", "if"), ("LOC", "if2"), ("THEN", "then"), ("SKIP", "skip")],
        )

    def test_operadores_booleanos(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("!(X <= 10) || false && true"),
            [
                ("NOT", "!"),
                ("LPAR", "("),
                ("LOC", "X"),
                ("LE", "<="),
                ("NUM", "10"),
                ("RPAR", ")"),
                ("OR", "||"),
                ("FALSE", "false"),
                ("AND", "&&"),
                ("TRUE", "true"),
            ],
        )

    def test_posicion_en_segunda_linea(self) -> None:
        tokens = tokenizar("X := 1;\nY := 2")
        token_y = tokens[4]
        self.assertEqual((token_y.type, token_y.line, token_y.column), ("LOC", 2, 1))

    def test_caracter_no_reconocido(self) -> None:
        with self.assertRaises(UnexpectedCharacters):
            tokenizar("X := 2 @ Y")


if __name__ == "__main__":
    unittest.main(verbosity=2)
