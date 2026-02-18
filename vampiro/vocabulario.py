"""
Módulo que gestiona el vocabulario del juego.
"""

# Tipos de palabras:
T_VERBO = 0
T_NOMBRE = 1

# Tokens:
COGER = 0
DEJAR = 1
ABRIR = 2
NORTE = 3
CUCHILLO = 4
CERRAR = 5

Palabra = tuple[int, int]

vocabulario: dict[str, Palabra] = {
    'COGER': (T_VERBO, COGER),
    'TOMAR': (T_VERBO, COGER),
    'ABRIR': (T_VERBO, ABRIR),
    'NORTE': (T_VERBO, NORTE),
    'N': (T_VERBO, NORTE),
    'CUCHILLO': (T_NOMBRE, CUCHILLO)
}

def buscar_palabra(lexema: str) -> Palabra|None:
    """
    Comprueba si en el vocabulario hay una palabra
    con ese lexema, y la devuelve en ese caso.
    En caso contrario, que devuelva None.
    """
    if lexema in vocabulario:
        return vocabulario[lexema]
    return None


def es_verbo(p: Palabra) -> bool:
    """Devuelve True si p es un verbo."""
    return p[0] == T_VERBO


def es_nombre(p: Palabra) -> bool:
    """Devuelve True si p es un nombre."""
    return p[0] == T_NOMBRE
