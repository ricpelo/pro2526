import random

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

numero = random.randint(0, 86015)
contador = 0

with open('/usr/share/dict/words', 'r') as f:
    for palabra in f:
        contador += 1
        if contador > numero:
            break

palabra = palabra.strip() \
    .translate(str.maketrans({'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'})) \
    .upper()

letras = []
fallos = 0
intentos = 0

print(palabra)

while True:
    solucion = palabra
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

with open('ahorcado.txt', 'w') as f:
    print(f'Solución: {palabra}', file=f)
    f.write(f'Solución: {palabra}\n')
    print(f'Intentos: {intentos}', file=f)
    f.write(f'Intentos: {intentos}\n')
