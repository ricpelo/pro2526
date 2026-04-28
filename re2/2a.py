"""
Diseñar en Python las clases Producto y Categoria:
Los productos tienen un nombre y un precio.
Las categorías tienen un nombre y una lista de productos, y deben responder a los siguientes
métodos:
◦ producto_mas_caro(): devuelve el producto más caro de esa categoría.
◦ precio_medio(): devuelve el precio medio dentro de esa categoría.

Escribir una función cargar_tienda() sin parámetros que cargue el archivo «tienda.xml» y que
devuelva una lista con todas las categorías en forma de instancias de la clase Categoria, las
cuales deberán contener todos sus productos.
Escribir una función buscar_producto(nombre, categorias) que busque un producto en todas
las categorías y que lo devuelva si existe, o None en caso contrario.
"""

import xml.etree.ElementTree as ET
from typing import Iterator


class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.__nombre = nombre
        self.__precio = precio

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> float:
        return self.__precio


class Categoria:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__productos: list[Producto] = []

    def __iter__(self) -> Iterator[Producto]:
        return iter(self.__productos)

    @property
    def nombre(self) -> str:
        return self.__nombre

    def agregar(self, nombre_prod: str, precio_prod: float) -> None:
        producto = Producto(nombre_prod, precio_prod)
        return self.__productos.append(producto)

    def producto_mas_caro(self) -> Producto:
        """Devuelve el producto más caro de esa categoría."""
        return max(self.__productos, key=lambda p: p.precio)

    def precio_medio(self) -> float:
        """Devuelve el precio medio dentro de esa categoría."""
        return sum(p.precio for p in self.__productos) / len(self.__productos)


def cargar_tienda() -> list[Categoria]:
    """
    Carga el archivo «tienda.xml» y devuelve una lista con todas las categorías
    en forma de instancias de la clase Categoria, las cuales deben contener
    todos sus productos.
    """
    arbol = ET.parse('tienda.xml')
    raiz = arbol.getroot()
    res: list[Categoria] = []
    for categoria in raiz.iterfind('categoria'):
        nombre_cat = categoria.get('nombre')
        cat = Categoria(nombre_cat)                           # type: ignore
        for producto in categoria.iterfind('producto'):
            nombre_prod = producto.find('nombre').text        # type: ignore
            precio_prod = float(producto.find('precio').text) # type: ignore
            cat.agregar(nombre_prod, precio_prod)             # type: ignore
        res.append(cat)
    return res


def buscar_producto(nombre: str, categorias: list[Categoria]) -> Producto | None:
    """
    Busca un producto en todas las categorías y lo devuelve si existe, o
    devuelve None en caso contrario.
    """
    for categoria in categorias:
        for producto in categoria:
            if producto.nombre == nombre:
                return producto
    return None


if __name__ == '__main__':
    cats = cargar_tienda()
    assert cats[0].precio_medio() == 15
    assert cats[0].producto_mas_caro().nombre == "teclado"
    assert buscar_producto("silla", cats).precio == 50       # type: ignore
