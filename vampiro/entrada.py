"""
Módulo de entrada.

- Variables:

  - entrada (str): contiene la entrada del jugador.
"""


entrada: str = ''


def pedir_entrada() -> None:
    """
    Pide la entrada del jugador y la almacena en la variable
    entrada del módulo.
    """
    global entrada
    lista: list[str] = input('> ').strip().upper().split()
    entrada = ' '.join(lista)


if __name__ == '__main__':
    pedir_entrada()
    print(entrada)
