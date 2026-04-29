"""
Programar en Python un modelo orientado a objetos que simule el funcionamiento de un sistema de
archivos y directorios.
Debe contener, al menos, la clase Entrada (clase abstracta) y las clases Archivo y Directorio (subclases
de Entrada).
Todas las entradas deben tener un nombre.
Todos los archivos tienen un tamaño definido como un número entero positivo.
Todos los directorios tienen una lista de entradas, cada una de las cuales pueden ser archivos o
directorios.
"""

from abc import ABC, abstractmethod

class Entrada(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @abstractmethod
    def tamanyo(self) -> int:
        ...


class Archivo(Entrada):
    def __init__(self, nombre: str, tamanyo: int) -> None:
        super().__init__(nombre)
        if tamanyo < 0:
            raise ValueError('El tamaño debe ser positivo.')
        self.__tamanyo = tamanyo

    def tamanyo(self) -> int:
        return self.__tamanyo


class Directorio(Entrada):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.__entradas: list[Entrada] = []

    def tamanyo(self) -> int:
        return sum(e.tamanyo() for e in self.__entradas)

    def anyadir(self, entrada: Entrada) -> None:
        self.__entradas.append(entrada)

    def buscar(self, nombre: str) -> Entrada | None:
        """
        Devuelve la entrada con ese nombre (búsqueda recursiva),
        o None si no existe.
        """
        for e in self.__entradas:
            if e.nombre == nombre:
                return e
            if isinstance(e, Directorio):
                res = e.buscar(nombre)
                if res is not None:
                    return res
        return None

    def listar(self) -> tuple:
        """
        Devuelve una tupla con los nombres de las entradas directas
        (no recursivas).
        """
        return tuple(e.nombre for e in self.__entradas)


if __name__ == '__main__':
    d = Directorio("root")
    d.anyadir(Archivo("a.txt", 10))
    d.anyadir(Archivo("b.txt", 20))
    sub = Directorio("docs")
    sub.anyadir(Archivo("c.txt", 5))
    d.anyadir(sub)
    assert d.tamanyo() == 35
    assert d.buscar("c.txt").tamanyo() == 5 # type: ignore
    assert d.listar() == ("a.txt", "b.txt", "docs")
