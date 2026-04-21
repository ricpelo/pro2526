"""
Tienda online.
"""

import ZODB
from persistent import Persistent
from BTrees.OOBTree import BTree # type: ignore


class Articulo(Persistent):
    """Un artículo de la tienda online."""

    def __init__(self, codigo: int, denominacion: str, precio: float) -> None:
        self.codigo = codigo
        self.denominacion = denominacion
        self.precio = precio

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


class Usuario(Persistent):
    """Un usuario de la tienda online."""

    def __init__(self, dni: str, nombre: str) -> None:
        self.__dni = dni
        self.nombre = nombre
        self.carrito = None

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


class Carrito(Persistent):
    """Un carrito de la tienda online."""

    def __init__(self, usuario: Usuario) -> None:
        self.__usuario = usuario
        usuario.carrito = self

    @property
    def usuario(self) -> Usuario:
        return self.__usuario
