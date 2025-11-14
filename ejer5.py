"""
Escribir un programa que reciba dos datos de entrada y que los
ordene de menor a mayor, indicando cuál es el primero y cuál
el segundo.
"""

# Datos de entrada:
a = False
b = True

# Datos de salida:
menor = a if a < b else b    # min(a, b)
mayor = a if a > b else b    # max(a, b)
orden: str = str(a) + ' es menor que ' + str(b) if a < b else \
             str(a) + ' es igual que ' + str(b) if a == b else \
             str(a) + ' es mayor que ' + str(b)

