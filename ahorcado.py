def dibujar_palabra(letras: list[str], solucion: str) -> None:
    """
    Dibuja el tablero con la palabra a adivinar y guiones bajos allí donde
    no se ha adivinado la letra.
    """
    i = 0
    while i < len(solucion):
        c = solucion[i]
        if c in letras:
            print(c, end='')
        else:
            print('_', end='')
        i += 1
    print()


def comprobar_palabra(letras: list[str], solucion: str) -> bool:
    """
    Comprueba si el jugador ha adivinado todas las letras.
    """
    i = 0
    while i < len(solucion):
        c = solucion[i]
        if c not in letras:
            return False
        i += 1
    return True


letras = []
fallos = 0
intentos = 0

while True:
    solucion = 'ORDENADOR'
    letra = input('Introduzca una letra: ').upper()
    letras.append(letra)
    dibujar_palabra(letras, solucion)
    if comprobar_palabra(letras, solucion):
        print('¡Enhorabuena!')
        break
    if letra not in solucion:
        fallos += 1
        if fallos >= 5:
            print('¡Te ahorcaste!')
            break
    intentos += 1
    print('Intentos:', intentos, ' Fallos:', fallos)
