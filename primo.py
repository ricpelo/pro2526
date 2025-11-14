"""
11. Escribir un programa que determine si un número entero introducido
por teclado es primo o compuesto.
"""

n: int = int(input('Introduzca un número entero: '))

num_divisores = 0
i = 1
while i <= n:
    if n % i == 0:
        num_divisores += 1
    i += 1

if num_divisores == 2:
    print("Es primo")
else:
    print("Es compuesto")
