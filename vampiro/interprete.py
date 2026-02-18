"""
Módulo que interpreta la entrada del jugador.

Una entrada válida es aquella que contiene un verbo
seguido opcionalmente por un nombre:

<entrada> ::= <verbo> [<nombre>]
"""

import vocabulario as voc
import entrada


verbo: voc.Palabra|None = None
nombre: voc.Palabra|None = None


def interpretar() -> None:
    """
    Interpreta la entrada del jugador y guarda el verbo y el nombre
    asociados a ella.
    """
    global verbo, nombre

    if entrada.longitud() == 0:
        # Entrada vacía --> MAL
        pass
    else:
        verbo = voc.buscar_palabra(entrada.primer_lexema())
        if verbo is None:
            # El primer lexema no existe como palabra
            print('No he entendido nada.')
            pass
        elif not voc.es_verbo(verbo):
            # La primera palabra no es un verbo --> MAL
            print('No puedes hacer eso.')
            pass
        else:
            if entrada.longitud() >= 2:
                nombre = voc.buscar_palabra(entrada.segundo_lexema())
                if nombre is not None and not voc.es_nombre(nombre):
                    # Hay una segunda palabra y no es un nombre --> MAL
                    pass
