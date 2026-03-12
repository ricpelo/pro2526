"""
Módulo principal del programa.

Crear un módulo principal.py que use las clases anteriores para representar un
modelo dinámico de objetos donde el cliente Antonio Martínez tiene dos cuentas
corrientes, cada una de ellas con tres movimientos. Imprimir por pantalla el saldo
actual de cada cuenta.
"""

from cliente import Cliente
from cuenta import Cuenta

antonio = Cliente('123', 'Antonio', 'Martínez')

Cuenta(antonio)
Cuenta(antonio)

print(Cuenta.buscar_cuenta(1) \
    .agregar_movimiento('INGRESO', 400.00) \
    .agregar_movimiento('SACAR DEL CAJERO', -50.00) \
    .agregar_movimiento('NÓMINA', 2000.00))

print(Cuenta.buscar_cuenta(2) \
    .agregar_movimiento('INGRESO', 5000.00) \
    .agregar_movimiento('TRANSFERENCIA', -100.00) \
    .agregar_movimiento('METO POR CAJERO', 50.00))
