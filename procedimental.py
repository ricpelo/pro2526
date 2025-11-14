"""
11. Escribe una función que calcule la longitud y el área de una circunferencia. Para ello,
el usuario debe introducir el radio (que puede contener decimales).
Recordemos:
𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑 = 2𝜋 · 𝑟𝑎𝑑𝑖𝑜
𝑎𝑟𝑒𝑎 = 𝜋 · 𝑟𝑎𝑑𝑖𝑜2
"""

from math import pi

def recoger_numero(msg: str) -> float:
    while True:
        try:
            radio = float(input(msg))
            return radio
        except ValueError:
            print('El dato introducido no es correcto')
















def longitud(radio: float) -> float:
    return 2 * pi * radio

def area(radio: float) -> float:
    return pi * radio ** 2





r = recoger_numero('Introduzca el radio: ')
print('La longitud de la circunferencia es', longitud(r))
print('El área de la circunferencia es', area(r))
