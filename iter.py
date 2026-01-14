def recorrer(iterable) -> None:
    it = iter(iterable)
    while True:
        try:
            sgte = next(it)
            print(sgte)
        except StopIteration:
            break


recorrer("1234")



def interpretar_codigos(codigos: list[str]) -> list[int]:
    """
    que reciba una lista de cadenas de la forma "ACCIÓN:VALOR",donde ACCIÓN representa una acción a realizar y
    VALOR un número entero sobre el que realizar dicha acción.
    Las acciones posibles son:
    "SUMA": sumar 1.
    "RESTA": restar 1.
    "DOBLE": multiplicar por 2.
    La función debe devolver una lista con los resultados de las operaciones realizadas.
    Ejemplo:
    >>> interpretar_codigos(["SUMA:10", "RESTA:4", "DOBLE:7"])
    [11, 3, 14]
    """
    res = []
    for codigo in codigos:
        accion, valor = codigo.split(':')
        valor = int(valor)
        if accion == 'SUMA':
            res.append(valor + 1)
        elif accion == 'RESTA':
            res.append(valor - 1)
        elif accion == 'DOBLE':
            res.append(valor * 2)
    return res


def normalizar_nombres(nombres: list[str]) -> list[str]:
    """
    que reciba una lista de cadenas con posibles espacios extra y que mezcla mayúsculas y minúsculas.
    La función debe:
    1. Crear una función local limpiar(nombre) que elimine espacios iniciales y finales, convierta a minúsculas y
    sustituya múltiples espacios internos consecutivos por uno solo.
    2. Recorrer toda la lista aplicando limpiar.
    3. Devolver la lista nueva.
    Ejemplo:
    >>> normalizar_nombres(["   Ana     Lopez   ", "JOSE     PÉREZ"])
    ["ana lopez", "jose pérez"]
    """
    def limpiar(nombre: str) -> str:
        return ' '.join(nombre.lower().split())
    res = []
    for nombre in nombres:
        res.append(limpiar(nombre))
    return res


from typing import Any

def colapsar(lista: list[tuple[Any, int]]) -> list[int]:
    """
    que reciba una lista de tuplas de la forma (valor, cantidad) y devuelva una nueva lista en la que cada tupla se
    convierta en cantidad copias del valor original.
    Ejemplo:
    >>> colapsar([(7, 3), (2, 1)])
    [7, 7, 7, 2]
    """
    res = []
    for valor, cantidad in lista:
        res += [valor] * cantidad
    return res



def enteros_cubiertos(lista: list[tuple[int, int]]) -> int:
    """
    que recibe una lista de tuplas que representan intervalos numéricos de la forma (límite_inferior, límite_superior)
    y que devuelva la cantidad total de enteros distintos cubiertos por esos intervalos, teniendo en cuenta que:
    Los intervalos se pueden solapar total o parcialmente, o incluso repetirse.
    Tanto límite_inferior como límite_superior son enteros y cumplen que límite_inferior ≤ límite_superior.
    Ejemplo:
    >>> enteros_cubiertos([(80, 81), (1, 2), (9, 11)])
    7 # Los enteros cubiertos por los tres intervalos son: 1, 2, 9, 10, 11, 80, 81
    >>> enteros_cubiertos([(3, 6), (4, 6), (5, 6)])
    4 # Los enteros cubiertos por los tres intervalos son: 3, 4, 5, 6
    >>> enteros_cubiertos([(1, 2), (1, 2)])
    2 # Los enteros cubiertos por los dos intervalos son: 1, 2
    """
    cubiertos = []
    for lim_inf, lim_sup in lista:
        j = lim_inf
        while j <= lim_sup:
            if j not in cubiertos:
                cubiertos.append(j)
            j += 1
    return len(cubiertos)




def pintar(lista) -> None:
    for i, e in enumerate(lista):
        print(i, e)



suma_o_resta = lambda s: (lambda x, y: x + y) if s == 'suma' else \
                             (lambda x, y: x - y)


def suma_o_resta(s: str):
    if s == 'suma':
        return lambda x, y: x + y
    return lambda x, y: x - y


def suma_o_resta(s: str):
    def suma(x, y):
        return x + y
    def resta(x, y):
        return x - y
    if s == 'suma':
        return suma
    return resta
