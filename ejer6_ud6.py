"""
Escribir una función que reciba una cantidad de días, minutos y segundos,
y que calcule y devuelva el número de segundos en los datos de entrada indicados.
Dar un ejemplo de uso.
"""

segundos = lambda dias, minutos, segs: 86_400 * dias + 60 * minutos + segs
ejemplo = segundos(5, 27, 6)
