"""
16. Escribir un programa que muestre por pantalla la tabla de multiplicar de
un número comprendido entre 0 y 10, introducido por teclado.
"""

while True:
    try:
        n: int = int(input('Introduzca un número entre 0 y 10: '))
        if n >= 0 and n <= 10:
            break
        print('El número introducido debe estar entre 0 y 10.')
    except ValueError:
        print('Dato de entrada incorrecto.')

i: int = 0
while i <= 10:
    print(n, 'x', i, '=', n * i)
    i += 1
