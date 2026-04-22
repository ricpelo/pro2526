from basedatos import BaseDatos
from modelo import Articulo, Usuario, Carrito

basedatos = BaseDatos()

for articulo in basedatos.raiz['articulos'].values():
    articulo.precio *= 0.85

basedatos.confirmar()
basedatos.cerrar()
