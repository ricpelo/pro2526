"""
XX. Escribe un programa que solicite al usuario 5 notas y que devuelva la media.
"""

notas: list[float] = []
n: int = int(input('Introduzca cantidad de notas: '))

i: int = 0
while i < n:
    notas.append(float(input('Introduzca nota: ')))
    i += 1

suma: float = 0.0
i = 0
while i < n:
    suma += notas[i]
    i += 1

media: float = suma / n
print('La media es', media)
