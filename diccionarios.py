'''
def assign_person_to_job(names: list[str], jobs: list[str]) -> dict[str, str]:
    """Asigna personas a profesiones."""
    res = {}
    for n, j in zip(names, jobs):
        res[n] = j
    return res

    return {n: j for n, j in zip(names, jobs)}

    return dict(zip(names, jobs))

names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

print(assign_person_to_job(names, jobs))


def calculate_losses(inventario: dict[str, int]) -> str|int:
    """Calcula el total de unidades perdidas."""
    if len(inventario) == 0:
        return "Lucky you!"
    res = 0
    for v in inventario.values():
        res += v
    return res

print(calculate_losses({
    "tv" : 30,
    "skate" : 20,
    "stereo" : 50,
}) == 100)

print(calculate_losses({
    "painting" : 20000,
}) == 20000)

print(calculate_losses({}) == "Lucky you!")
'''

def mayor_frecuencia(s: str) -> str:
    """
    Dada una cadena, devuelve el carácter que más veces
    se repite en la cadena.
    """
    d = {}
    mayor = 0
    res = ''
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        if d[c] > mayor:
            mayor = d[c]
            res = c
    return res

print(mayor_frecuencia('esto es una prueba'))


def unique_sort(l: list[int]) -> list[int]:
    """Devuelve la lista ordenada y sin repetidos."""
    return sorted(set(l))


def integer_boolean(s: str) -> list[bool]:
    """Convierte un entero binario a booleanos."""
    return [c == '1' for c in s]

print(integer_boolean("100101") == [True, False, False, True, False, True])
print(integer_boolean("10") == [True, False])
print(integer_boolean("001") == [False, False, True])



def str2dict(lst: list[str]) -> dict[str, str]:
    return {k: v for k, v in (r.split('=') for r in lst)}

print(str2dict(['1=uno', '2=dos', '3=tres', '4=cuatro'])
== {'1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro'})
print(str2dict(['pepe=humano', 'pancho=perro', 'violeta=gato', 'gustavo=rana'])
== {'pepe': 'humano', 'pancho': 'perro', 'violeta': 'gato', 'gustavo': 'rana'})

from operator import mul, truediv

mul = lambda x, y: x * y
truediv = lambda x, y: x / y

def procesar_medidas(lista: list[tuple[float, str]]) -> list[tuple[float, str]]:
    conversion = {
        'km':  (mul, 1000),
        'hm':  (mul, 100),
        'dam': (mul, 10),
        'm':   (mul, 1),
        'dm':  (truediv, 10),
        'cm':  (truediv, 100),
        'mm':  (truediv, 1000)
    }
    # return [(op(c, factor), 'm') for c, op, factor in ((c,) + conversion[u] for c, u in lista) ]
    res = []
    for cantidad, unidades in lista:
        op, factor = conversion[unidades]
        res.append((op(cantidad, factor), 'm'))
    return res

print(procesar_medidas([(150.0, "cm"), (30.4, "dam"), (2.0, "m")]) ==
    [(1.5, "m"), (304.0, "m"), (2.0, "m")])