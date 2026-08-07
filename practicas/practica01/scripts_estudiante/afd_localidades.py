"""AFD incompleto para las localidades de IMP.

Patrón de trabajo: una o más letras seguidas opcionalmente por dígitos.
Ejemplos aceptados: X, contador, X2, Total25.
Ejemplos rechazados: cadena vacía, 2X, X_2, X2Y.
"""

from __future__ import annotations


ESTADO_INICIAL = "q0"
ESTADOS_FINALES = {"q_letras", "q_digitos"}
ESTADO_ERROR = "q_error"

LETRA = "letra"
DIGITO = "digito"
OTRO = "otro"


def clase_de(caracter: str) -> str:
    """Clasifica un carácter usando el alfabeto acordado para la práctica."""
    if caracter.isascii() and caracter.isalpha():
        return LETRA
    if caracter.isascii() and caracter.isdigit():
        return DIGITO
    return OTRO


# La primera transición funciona como ejemplo.
# TODO 3.3: agrega las transiciones que faltan para [A-Za-z]+[0-9]*.
TRANSICIONES: dict[tuple[str, str], str] = {
    (ESTADO_INICIAL, LETRA): "q_letras",
}


def siguiente_estado(estado: str, clase: str) -> str:
    """Devuelve el siguiente estado o el estado de error."""
    return TRANSICIONES.get((estado, clase), ESTADO_ERROR)


def acepta_localidad(cadena: str) -> bool:
    """Recorre el AFD y decide si la cadena completa es una localidad."""
    estado = ESTADO_INICIAL

    for caracter in cadena:
        estado = siguiente_estado(estado, clase_de(caracter))
        if estado == ESTADO_ERROR:
            return False

    return estado in ESTADOS_FINALES


if __name__ == "__main__":
    muestras = ("X", "contador", "X2", "Total25", "", "2X", "X_2", "X2Y")
    for muestra in muestras:
        print(f"{muestra!r:12} -> {acepta_localidad(muestra)}")
