"""
Módulo que interpreta la entrada del jugador.

Una entrada válida es aquella que contiene un verbo
seguido opcionalmente por un nombre:

<entrada> ::= <verbo> [<nombre>]
"""

import vocabulario as voc
import entrada

entrada.pedir_entrada()

palabras = entrada.entrada.split()

if len(palabras) == 0:
    # Entrada vacía --> MAL
    pass
else:
    voc.buscar_palabra(palabras[0])
    if voc.verbo is None:
        # La primera palabra no es un verbo --> MAL
        pass
    else:
        if len(palabras) >= 2:
            voc.buscar_palabra(palabras[1])
