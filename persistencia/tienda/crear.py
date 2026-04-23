"""
Crear una base de datos con un carrito de compra online.
"""

from basedatos import BaseDatos
from BTrees.OOBTree import BTree # type: ignore
from modelo import Articulo, Usuario, Carrito, Detalle

pepe = Usuario('111A', 'Pepe')

carrito = Carrito(pepe)

tornillo = Articulo(1, 'Tornillo', 4.00)
tuerca = Articulo(2, 'Tuerca', 2.00)
picaporte = Articulo(3, 'Picaporte', 15.00)

carrito.agregar_articulo(tornillo)
carrito.agregar_articulo(tuerca, 5)

basedatos = BaseDatos()
raiz = basedatos.raiz

raiz['usuarios'] = BTree()
raiz['usuarios'][pepe.dni] = pepe

raiz['articulos'] = BTree()
raiz['articulos'][tornillo.codigo] = tornillo
raiz['articulos'][tuerca.codigo] = tuerca
raiz['articulos'][picaporte.codigo] = picaporte

"""
raiz['detalles'] = BTree()

for usuario in raiz['usuarios'].values():
    if usuario.carrito is not None:
        for detalle in usuario.carrito:
            raiz['detalles'][...] = detalle
"""

basedatos.confirmar()
basedatos.cerrar()
