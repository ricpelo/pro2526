"""
Crear un módulo principal.py que use las clases anteriores para representar un
modelo dinámico de objetos donde existe una factura del cliente Rosa González
que ha comprado dos televisores de 399 € cada uno y una tarjeta gráfica de 239 €.
Imprimir por pantalla todos los datos de la factura como si fuera una factura real,
incluyendo el importe total de la misma.
"""

from cliente import Cliente
from articulo import Articulo
from factura import Factura

rosa = Cliente('123', 'Rosa', 'González')
tv = Articulo('111', 'Televisor', 399.00)
gpu = Articulo('222', 'Tarjeta gráfica', 239.00)

f = Factura(1, rosa)
f.anyadir_linea(tv, 2)
f.anyadir_linea(gpu, 1)

f.imprimir()
