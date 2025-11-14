"""
Escribir un programa que calcule el mínimo común múltiplo (mcm) de dos números
enteros, de dos formas diferentes:
a) Mediante la función lcm del módulo math.
b) Aprovechando la siguiente propiedad:
                 𝑎 · 𝑏 = 𝑚𝑐𝑑 (𝑎, 𝑏) · 𝑚𝑐𝑚(𝑎, 𝑏)
"""

from math import lcm, gcd

# Datos de entrada:
x: int = 14
y: int = 22

# Salida:
mcm_a = lcm(x, y)
mcm_b = (x * y) // gcd(x, y)


