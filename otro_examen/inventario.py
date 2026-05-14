import ZODB
from BTrees.OOBTree import BTree # type: ignore
from persistent import Persistent
import transaction
from ZODB.FileStorage import FileStorage


class Producto(Persistent):
    def __init__(self, ident: int, nombre: str) -> None:
        self.__ident = ident
        self.nombre = nombre
        self.__stock = 0
        self.__movimientos = BTree()

    @property
    def movimientos(self):
        return self.__movimientos

    @property
    def ident(self) -> int:
        return self.__ident

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def stock(self) -> int:
        return self.__stock

    def registrar_movimiento(self, movimiento: 'Movimiento') -> None:
        self.__movimientos[movimiento.numero] = movimiento
        self.__stock += movimiento.cantidad

    def crear_movimiento(self, cantidad: int, fecha_hora: str) -> None:
        Movimiento(self, cantidad, fecha_hora)


class Movimiento(Persistent):
    __ultimo: int = 0

    def __init__(self, producto: Producto, cantidad: int, fecha_hora: str) -> None:
        Movimiento.__ultimo += 1
        self.__numero = Movimiento.__ultimo
        self.__producto = producto
        self.__cantidad = cantidad
        self.__fecha_hora = fecha_hora
        producto.registrar_movimiento(self)

    def __str__(self) -> str:
        return f'Muevo {self.cantidad} unidades del producto {self.producto.nombre} el {self.fecha_hora}.'

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def producto(self) -> Producto:
        return self.__producto

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @property
    def fecha_hora(self) -> str:
        return self.__fecha_hora

almacen = FileStorage('inventario.fs')
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

cola = Producto(1, 'Coca cola')
fanta = Producto(2, 'Fanta')

raiz.productos = BTree()
raiz.productos[cola.ident] = cola
raiz.productos[fanta.ident] = fanta

m1 = Movimiento(cola, 200, '2026-05-12 20:39:07')
m2 = Movimiento(cola, -50, '2026-05-12 21:00:10')
m3 = Movimiento(fanta, 100, '2026-05-12 20:45:07')

raiz.movimientos = BTree()
raiz.movimientos[m1.fecha_hora] = m1
raiz.movimientos[m2.fecha_hora] = m2
raiz.movimientos[m3.fecha_hora] = m3

for mov in raiz.movimientos.values('2026-05-12 20:00:00', '2026-05-12 20:40:00'):
    print(mov)

print(cola.stock)

for mov in raiz.productos[1].movimientos.values():
    print(mov)

print(sorted(raiz.productos))


transaction.commit()
conexion.close()
bd.close()
