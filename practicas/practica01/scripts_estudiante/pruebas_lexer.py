"""Pruebas graduadas para la Práctica 1.

Retira cada decorador @unittest.skip al llegar al paso indicado. La prueba mínima
permanece activa desde el inicio.
"""

from __future__ import annotations

import unittest

from lark.exceptions import UnexpectedCharacters

from afd_localidades import acepta_localidad
from lexer_imp import analizar_fuente, construir_tabla_localidades


def tipos_y_lexemas(texto: str) -> list[tuple[str, str]]:
    return [(token.type, str(token)) for token in analizar_fuente(texto)]


class PruebasAFD(unittest.TestCase):
    def test_localidad_minima(self) -> None:
        self.assertTrue(acepta_localidad("X"))

    @unittest.skip("Habilitar después de completar el paso 3.3")
    def test_localidades_completas(self) -> None:
        for cadena in ("contador", "X2", "Total25"):
            with self.subTest(cadena=cadena):
                self.assertTrue(acepta_localidad(cadena))

    @unittest.skip("Habilitar después de completar el paso 3.3")
    def test_localidades_invalidas(self) -> None:
        for cadena in ("", "2X", "X_2", "X2Y"):
            with self.subTest(cadena=cadena):
                self.assertFalse(acepta_localidad(cadena))


class PruebasLexer(unittest.TestCase):
    def test_version_inicial(self) -> None:
        self.assertEqual(tipos_y_lexemas("X"), [("LOC", "X")])

    @unittest.skip("Habilitar después de completar el paso 5.2")
    def test_localidades_y_numerales(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("X 25"),
            [("LOC", "X"), ("NUM", "25")],
        )

    @unittest.skip("Habilitar después de completar el paso 5.3")
    def test_palabras_reservadas_no_son_localidades(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("if X then skip else if2"),
            [
                ("IF", "if"),
                ("LOC", "X"),
                ("THEN", "then"),
                ("SKIP", "skip"),
                ("ELSE", "else"),
                ("LOC", "if2"),
            ],
        )

    @unittest.skip("Habilitar después de completar el paso 5.4")
    def test_operadores_y_delimitadores(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("X := (Y + 2) <= 10 && true;"),
            [
                ("LOC", "X"),
                ("ASSIGN", ":="),
                ("LPAR", "("),
                ("LOC", "Y"),
                ("PLUS", "+"),
                ("NUM", "2"),
                ("RPAR", ")"),
                ("LE", "<="),
                ("NUM", "10"),
                ("AND", "&&"),
                ("TRUE", "true"),
                ("SEMI", ";"),
            ],
        )

    @unittest.skip("Habilitar después de completar el paso 6.2")
    def test_tabla_de_localidades(self) -> None:
        tokens = analizar_fuente("X := X + Y")
        self.assertEqual(
            construir_tabla_localidades(tokens),
            {
                "X": {
                    "primera_linea": 1,
                    "primera_columna": 1,
                    "apariciones": 2,
                },
                "Y": {
                    "primera_linea": 1,
                    "primera_columna": 10,
                    "apariciones": 1,
                },
            },
        )

    @unittest.skip("Habilitar después de completar el paso 7.2")
    def test_caracter_desconocido(self) -> None:
        with self.assertRaises(UnexpectedCharacters):
            analizar_fuente("X := 2 @ Y")


if __name__ == "__main__":
    unittest.main(verbosity=2)
