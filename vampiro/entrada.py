"""
Módulo de entrada.

- Variables:

  - entrada (list[str]): contiene la entrada del jugador.
"""


entrada: list[str] = []


def pedir_entrada() -> None:
    """
    Pide la entrada del jugador y la almacena en la variable
    entrada del módulo.
    """
    global entrada
    entrada = input('> ').strip().upper().split()


def longitud() -> int:
    """
    Devuelve cuántos lexemas tiene la entrada.
    """
    return len(entrada)


def primer_lexema() -> str:
    """Devuelve el primer lexema."""
    try:
        return entrada[0]
    except IndexError:
        return ''


def segundo_lexema() -> str:
    """Devuelve el primer lexema."""
    try:
        return entrada[1]
    except IndexError:
        return ''


if __name__ == '__main__':
    pedir_entrada()
    print(entrada)
