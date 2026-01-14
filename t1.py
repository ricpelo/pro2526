from math import gcd

def sumar_fracc(f1: tuple[int, int], f2: tuple[int, int]) -> tuple[int, int]:
    """
    >>> sumar_fracc((1, 6), (1, 3))
    (1, 2)
    >>> sumar_fracc((4, 2), (5, 1))
    (7, 1)
    """
    num = f1[0] * f2[1] + f1[1] * f2[0]
    den = f1[1] * f2[1]
    mcd = gcd(num, den)
    return (num // mcd, den // mcd)

def es_consecutiva(lst: list[int]) -> bool:
    """
    >>> es_consecutiva([4, 5, 6, 7])
    True
    >>> es_consecutiva([4, 6, 7])
    False
    """
    if len(lst) == 0:
        return True
    i, t = 1, lst[0]
    while i < len(lst):
        if lst[i] != t + 1:
            return False
        i, t = i + 1, lst[i]
    return True


def es_con_rec(lst: list[int]) -> bool:
    if len(lst) < 2:
        return True
    if lst[0] + 1 != lst[1]:
        return False
    return es_con_rec(lst[1:])


def ahorcado(intento: str, solucion: str) -> None:
    """
    La función deberá comprobar si el intento coincide con la solución.
    En caso afirmativo, deberá mostrar por la salida el mensaje
    «¡Enhorabuena!». En caso contrario, deberá mostrar la solución con
    las letras adivinadas (es decir, las letras que aparecen en el
    intento), y las letras no adivinadas sustituidas por un guión bajo.
    Se supone que las letras son siempre mayúsculas y sin acentos.
    Por ejemplo, si la solución es la palabra «INFORMATICA», tenemos:
    >>> ahorcado('MANZANA', 'INFORMATICA')
    _N___MA___A
    >>> ahorcado('MATEMATICAS', 'INFORMATICA')
    I____MATICA
    >>> ahorcado('INFORMATICA', 'INFORMATICA')
    ¡Enhorabuena!
    """
    if intento == solucion:
        print('¡Enhorabuena!')
        return
    i = 0
    while i < len(solucion):
        c = solucion[i]
        print(c if c in intento else '_', end='')
        i += 1
    print()
    

def unicos(lista: list[int]) -> list[int]:
    """
    Escribir en Python una función pura recursiva llamada unicos(lista)
    que reciba una lista de números enteros en la que todos
    aparecen dos o más veces, excepto dos de ellos que sólo aparecen
    una vez. La función deberá devolver una lista que contenga sólo
    esos dos elementos únicos.
    >>> unicos([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
    [2, 1]
    >>> unicos([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])
    [5, 6]
    >>> unicos([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4])
    [3, 2]
    """
    res: list[int] = []
    i = 0
    while i < len(lista):
        if lista.count(lista[i]) == 1:
            res.append(lista[i])
        i += 1
    return res


def unicos(lista: list[int]) -> list[int]:
    def aux(l, res, vistos):
        if len(l) == 0:
            return res
        elif l[0] in vistos:
            return aux(l[1:], res, vistos)
        elif l[0] not in res and l[0] not in l[1:]:
            return aux(l[1:], res + [l[0]], vistos + [l[0]])
        else:
            return aux(l[1:], res, vistos + [l[0]])
    return aux(lista, [], [])


def es_anagrama(c1: str, c2: str) -> bool:
    cc1 = c1[:]
    cc1.sort()
    return sorted(c1.lower()) == sorted(c2.lower())


def fibonacci_hasta(n: int) -> list[int]:
    """
    >>> fibonacci_hasta(10)
    [0, 1, 1, 2, 3, 5, 8]
    >>> fibonacci_hasta(30)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> fibonacci_hasta(0)
    [0]
    """
    res: list[int] = []
    act, sig = 0, 1
    while act <= n:
        res.append(act)
        act, sig = sig, act + sig
    return res


def cifrar_mensaje(texto: str) -> str:
    """
    >>> cifrar_mensaje('¡Hola, Mundo!')
    '¡Ipmb, Nwoep!'
    """
    res: list[str] = []
    i = 0
    while i < len(texto):
        c = texto[i]
        if c.isalpha():
            c = chr(ord(c) - 25) if c.lower() == 'z' else chr(ord(c) + 1)
        res.append(c)
        i += 1
    return ''.join(res)
