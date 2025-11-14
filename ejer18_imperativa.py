"""
18. Escribir un programa que guarde en una lista N cadenas introducidas
por teclado y luego las muestre en orden inverso a como se han introducido,
desde la última cadena introducida hasta la primera.
"""

lista: list[str] = []

n = int(input('Introduzca cuántas cadenas quiere introducir: '))

# Llena la lista:

i: int = 0
while i < n:
    lista.append(input('Introduzca una cadena: '))
    i += 1

# Recorre la lista en orden inverso:

i = n - 1
while i >= 0:
    print(lista[i])
    i -= 1
    