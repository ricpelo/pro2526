"""
12. Escribir un programa que calcule la media de cinco valores numéricos reales
(tipo float) introducidos por teclado
"""

def recoger_numero(msg: str) -> float:
    while True:
        try:
            radio = float(input(msg))
            return radio
        except ValueError:
            print('El dato introducido no es correcto')

def recoger_numeros(l: list[float]) -> None:
    i: int = 0
    while i < 5:
        numero = recoger_numero('Introduzca el número: ')
        l.append(numero)
        i += 1

def calcular_media(l: list[float]) -> float:
    return sum(l) / len(l)

lista: list[float] = []
recoger_numeros(lista)
media = calcular_media(lista)
print('La media es', media)

