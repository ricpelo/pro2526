"""
Tienda online.
"""

from persistent import Persistent
from BTrees.OOBTree import BTree # type: ignore
from typing import Iterator


class Articulo(Persistent):
    """Un artículo de la tienda online."""

    def __init__(self, codigo: int, denominacion: str, precio: float) -> None:
        self.codigo = codigo
        self.denominacion = denominacion
        self.precio = precio

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.codigo == otro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int) -> None:
        if codigo <= 0:
            raise ValueError('El código debe ser un número entero positivo.')
        self.__codigo = codigo

    @property
    def denominacion(self) -> str:
        return self.__denominacion

    @denominacion.setter
    def denominacion(self, denominacion: str) -> None:
        if len(denominacion) == 0:
            raise ValueError('La denominación no puede ser vacía.')
        self.__denominacion = denominacion

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, precio: float) -> None:
        if precio < 0:
            raise ValueError('El precio no puede ser negativo.')
        self.__precio = precio

    def __str__(self) -> str:
        return f'{self.codigo} {self.denominacion:15} {self.precio:5.2f} €'


class Usuario(Persistent):
    """Un usuario de la tienda online."""

    def __init__(self, dni: str, nombre: str) -> None:
        self.__dni = dni
        self.nombre = nombre
        self.carrito = None

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.dni == otro.dni

    def __hash__(self) -> int:
        return hash(self.dni)

    @property
    def dni(self) -> str:
        return self.__dni

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def carrito(self) -> 'Carrito|None':
        return self.__carrito

    @carrito.setter
    def carrito(self, carrito: 'Carrito|None') -> None:
        self.__carrito = carrito

    def __str__(self) -> str:
        return f'Usuario {self.nombre} con DNI {self.dni}'


class Detalle(Persistent):
    """Una línea de detalle dentro del carrito."""

    def __init__(self, carrito: 'Carrito', articulo: Articulo, cantidad: int = 1) -> None:
        self.__carrito = carrito
        self.__articulo = articulo
        self.__set_cantidad(cantidad)

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return (self.carrito, self.articulo) == (otro.carrito, otro.articulo)

    def __hash__(self) -> int:
        return hash((self.carrito, self.articulo))

    @property
    def carrito(self) -> 'Carrito':
        return self.__carrito

    @property
    def articulo(self) -> Articulo:
        return self.__articulo

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @property
    def importe(self) -> float:
        return self.articulo.precio * self.cantidad

    def __set_cantidad(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError('La cantidad debe ser siempre mayor que cero.')
        self.__cantidad = cantidad

    def incrementar_cantidad(self, incremento: int = 1) -> None:
        self.__set_cantidad(self.cantidad + incremento)

    def decrementar_cantidad(self, decremento: int = 1) -> None:
        self.__set_cantidad(self.cantidad - decremento)


class Carrito(Persistent):
    """Un carrito de la tienda online."""

    def __init__(self, usuario: Usuario) -> None:
        self.__usuario = usuario
        usuario.carrito = self
        self.__detalles = BTree()

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.usuario == otro.usuario

    def __hash__(self) -> int:
        return hash(self.usuario)

    def __iter__(self) -> Iterator[Detalle]:
        return iter(self.__detalles.values())

    def get_detalles(self):
        return self.__detalles

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def total(self) -> float:
        return sum(detalle.importe for detalle in self)

    def agregar_articulo(self, articulo: Articulo, cantidad: int = 1) -> None:
        """Añade un artículo al carrito, con la cantidad indicada."""
        if articulo.codigo in self.__detalles:
            detalle = self.__detalles[articulo.codigo]
            detalle.incrementar_cantidad(cantidad)
        else:
            self.__detalles[articulo.codigo] = Detalle(self, articulo, cantidad)

    def quitar_articulo(self, articulo: Articulo, cantidad: int = 1) -> None:
        self.quitar_articulo_por_codigo(articulo.codigo, cantidad)

    def quitar_articulo_por_codigo(self, codigo: int, cantidad: int = 1) -> None:
        if codigo in self.__detalles:
            detalle = self.__detalles[codigo]
            cant_anterior = detalle.cantidad
            if cant_anterior == cantidad:
                del self.__detalles[codigo]
            else:
                detalle.decrementar_cantidad(cantidad)
        else:
            raise ValueError('El artículo no está en el carrito.')

    def buscar_articulo(self, articulo: Articulo) -> Detalle|None:
        for detalle in self:
            if detalle.articulo == articulo:
                return detalle
        return None
