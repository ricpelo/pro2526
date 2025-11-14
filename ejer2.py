"""
Ejercicio 2 de Programación funcional
Programa que calcula el volumen de una esfera
a partir de su radio.
Copyright (c) Ricardo Pérez.
Licencia: ...
"""

from math import pi

# En forma de script:

radio: float = 5.0                              # El radio de la esfera
salida: float = (4 / 3) * pi * (radio ** 3)    # El volumen de la esfera

# En forma de función:

cubo = lambda x: x * x * x
volumen = lambda r: (4 / 3) * pi * cubo(r)
resultado = volumen(radio)
