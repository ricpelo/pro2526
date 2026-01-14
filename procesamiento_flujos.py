numeros = range(100)
filtrados = filter(lambda x: x % 2 == 1, numeros)
cuadrados = map(lambda x: x ** 2, filtrados)
suma = sum(cuadrados)
print(suma)

def agregar_elemento(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    print(lista)


suma = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, range(100))))
print(suma)

from functools import reduce

def maximo(iterable):
    return reduce(lambda acc, x: acc if acc > x else x, iterable)


def join(iterable, sep):
    return reduce(lambda acc, x: acc + sep + x, iterable, '').lstrip()