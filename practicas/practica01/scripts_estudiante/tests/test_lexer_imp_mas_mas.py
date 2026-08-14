"""Pruebas que se habilitan al extender el lexer a IMP++."""

from __future__ import annotations

import unittest

from lark.exceptions import UnexpectedCharacters

from lexer import tokenizar


def tipos_y_lexemas(codigo_fuente: str) -> list[tuple[str, str]]:
    return [(token.type, str(token)) for token in tokenizar(codigo_fuente)]


class PruebasLexerImpMasMas(unittest.TestCase):
    @unittest.skip("Retira este decorador después de extender LOC")
    def test_identificador_con_guion_bajo(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("contador_1 := 0;"),
            [("LOC", "contador_1"), ("ASSIGN", ":="), ("NUM", "0"), ("SEMI", ";")],
        )

    @unittest.skip("Retira este decorador después de agregar comentarios")
    def test_comentario_se_ignora(self) -> None:
        tokens = tokenizar("X := 1; // avance\nY := 2;")
        self.assertEqual([str(token) for token in tokens], ["X", ":=", "1", ";", "Y", ":=", "2", ";"])
        self.assertEqual((tokens[4].type, tokens[4].line, tokens[4].column), ("LOC", 2, 1))

    @unittest.skip("Retira este decorador después de agregar palabras y llaves")
    def test_palabras_reservadas_y_llaves(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("int bool print for { } printable"),
            [
                ("INT", "int"),
                ("BOOL", "bool"),
                ("PRINT", "print"),
                ("FOR", "for"),
                ("LBRACE", "{"),
                ("RBRACE", "}"),
                ("LOC", "printable"),
            ],
        )

    @unittest.skip("Retira este decorador después de agregar INC y DEC")
    def test_incremento_y_decremento_son_tokens_completos(self) -> None:
        self.assertEqual(
            tipos_y_lexemas("X++ + Y-- - 1"),
            [
                ("LOC", "X"),
                ("INC", "++"),
                ("PLUS", "+"),
                ("LOC", "Y"),
                ("DEC", "--"),
                ("MINUS", "-"),
                ("NUM", "1"),
            ],
        )

    @unittest.skip("Retira este decorador cuando la extensión esté completa")
    def test_programa_imp_mas_mas(self) -> None:
        codigo = """int contador_1 := 0;
bool activo := true;
for (contador_1 := 0; contador_1 <= 2; contador_1++) {
    print(contador_1); // salida
}
"""
        tipos = [token.type for token in tokenizar(codigo)]
        self.assertEqual(
            tipos,
            [
                "INT", "LOC", "ASSIGN", "NUM", "SEMI",
                "BOOL", "LOC", "ASSIGN", "TRUE", "SEMI",
                "FOR", "LPAR", "LOC", "ASSIGN", "NUM", "SEMI",
                "LOC", "LE", "NUM", "SEMI", "LOC", "INC", "RPAR",
                "LBRACE", "PRINT", "LPAR", "LOC", "RPAR", "SEMI", "RBRACE",
            ],
        )

    # TODO: agrega un caso válido propio y un caso que espere
    # UnexpectedCharacters, como se solicita en el Ejercicio 4.


if __name__ == "__main__":
    unittest.main(verbosity=2)
