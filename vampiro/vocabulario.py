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

vocabulario: dict[str, tuple[int, int]] = {
    'COGER': (T_VERBO, COGER),
    'TOMAR': (T_VERBO, COGER),
    'ABRIR': (T_VERBO, ABRIR),
    'NORTE': (T_VERBO, NORTE),
    'N': (T_VERBO, NORTE),
    'CUCHILLO': (T_NOMBRE, CUCHILLO)
}

verbo = None
nombre = None

def buscar_palabra(palabra: str) -> None:
    """
    Comprueba si una palabra existe en el vocabulario y hace que
    el módulo la recuerde como verbo o como nombre.
    """
    global verbo, nombre
    if palabra in vocabulario:
        tipo, token = vocabulario[palabra]
        if tipo == T_VERBO:
            verbo = token
        elif tipo == T_NOMBRE:
            nombre = token
        else:
            # Error
            pass
