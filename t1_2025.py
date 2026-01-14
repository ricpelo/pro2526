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
    i = 0
    cubiertos = []
    while i < len(lista):
        lim_inf, lim_sup = lista[i]
        j = lim_inf
        while j <= lim_sup:
            if j not in cubiertos:
                cubiertos.append(j)
            j += 1
        i += 1
    return len(cubiertos)


def parejas(numeros: str) -> list[tuple[int, int]]:
    """
    que reciba una cadena de números separados por espacios y que devuelva una lista de tuplas con las parejas
    que hay dentro de la cadena. El primer número de la cadena representa la cantidad de números que hay detrás,
    por lo que no se debe contar a la hora de crear las parejas.
    Ejemplo:
    >>> parejas("7 1 2 1 2 1 3 2")
    [(1, 1), (2, 2)]
    >>> parejas("9 10 20 20 10 10 30 50 10 20")
    [(10, 10), (20, 20), (10, 10)]
    >>> parejas("4 2 3 4 1")
    [] # aunque hay dos 4, el primero no se cuenta
    """
    numeros = numeros.split()[1:]
    i = 0
    res = []
    while i < len(numeros):
        n = numeros[i]
        if numeros.count(n) >= 2:
            res.append((int(n), int(n)))
            numeros.remove(n)
            numeros.remove(n)
        else:
            i += 1
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
    i = 0
    res = []
    while i < len(lista):
        valor, cantidad = lista[i]
        res += [valor] * cantidad
        i += 1
    return res


def maximo_no_adyacente(lista: list[int]) -> int:
    """
    que devuelva el mayor valor de la lista tal que ningún otro elemento igual esté adyacente a él.
    Ejemplo:
    >>> maximo_no_adyacente([4, 4, 2, 4])
    2 # Porque los 4 están adyacentes
    >>> maximo_no_adyacente([3, 5, 3])
    5
    """
    i = 0
    descartados = []
    while i < len(lista):
        n = lista[i]
        if i > 0 and lista[i - 1] == n or i < len(lista) - 1 and lista[i + 1] == n:
            descartados.append(n)
        i += 1
    i = 0
    maximo = None
    while i < len(lista):
        n = lista[i]
        if n not in descartados and (maximo is None or n > maximo):
            maximo = n
        i += 1
    return maximo


def evaluar_arbol(exp: list | int) -> int:
    """
    que reciba un árbol sintáctico representado mediante listas anidadas, donde cada nodo interno es una cadena
    que representa una operación a realizar ("+", "-" o "*") y sus hijos son números enteros o más subárboles.
    La función debe evaluar completamente el árbol y devolver el resultado numérico.
    Ejemplo:
    >>> evaluar_arbol(["+", ["*", 2, 3], 5]) # (2 * 3) + 5
    11
    >>> evaluar_arbol(["+", ["-", 4, ["*", 2, 3]], 5]) # (4 - (2 * 3)) + 5
    3
    """
    if type(exp) == int:
        return exp
    op, op1, op2 = exp
    if op == '+':
        return evaluar_arbol(op1) + evaluar_arbol(op2)
    if op == '-':
        return evaluar_arbol(op1) - evaluar_arbol(op2)
    if op == '*':
        return evaluar_arbol(op1) * evaluar_arbol(op2)


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
    i = 0
    res = []
    while i < len(codigos):
        accion, valor = codigos[i].split(':')
        valor = int(valor)
        if accion == 'SUMA':
            res.append(valor + 1)
        elif accion == 'RESTA':
            res.append(valor - 1)
        elif accion == 'DOBLE':
            res.append(valor * 2)
        i += 1
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
    i = 0
    res = []
    while i < len(nombres):
        res.append(limpiar(nombres[i]))
        i += 1
    return res


def compresion_simple(lista: list[int]) -> list[tuple[int, int]]:
    """
    que reciba una lista y devuelva otra lista donde las repeticiones consecutivas son sustituidas por tuplas de la
    forma (valor, cantidad).
    Ejemplo:
    >>> compresion_simple([1, 1, 1, 2, 2, 1, 3])
    [(1, 3), (2, 2), (1, 1), (3, 1)]
    """
    i = 0
    res = []
    while i < len(lista):
        valor = lista[i]
        i += 1
        cantidad = 1
        while i < len(lista) and valor == lista[i]:
            cantidad += 1
            i += 1
        res.append((valor, cantidad))
    return res

        