"""
Escribir un programa que muestre por pantalla todo lo que recibe por la entrada
y que se detiene cuando recibe un "fin" (el "fin" no se imprime).
"""

while True:
    cadena = input('Introduzca una cadena ("fin" para finalizar): ')
    if cadena == "fin":
        break
    print(cadena)
