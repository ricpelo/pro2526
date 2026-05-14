import ZODB
from BTrees.OOBTree import BTree # type: ignore
import persistent
from ZODB.FileStorage.FileStorage import FileStorage
import transaction
from typing import Iterator

class Libro(persistent.Persistent):
    def __init__(self, isbn: int, titulo: str) -> None:
        self.__isbn = isbn
        self.__titulo = titulo
        self.__prestamos = BTree()

    @property
    def isbn(self) -> int:
        return self.__isbn

    @property
    def titulo(self) -> str:
        return self.__titulo

    def prestamos(self) -> Iterator['Prestamo']:
        return self.__prestamos.values()

    def prestado(self) -> bool:
        for k, prestamo in self.__prestamos.items(reverse=True):
            if not prestamo.devuelto():
                return True
        return False

    def prestar(self, usuario: 'Usuario', fecha_prestamo: str) -> 'Prestamo':
        if self.prestado():
            raise ValueError('El libro ya está prestado.')
        prestamo = Prestamo(self, usuario, fecha_prestamo)
        self.__prestamos[prestamo.fecha_prestamo] = prestamo
        usuario.anyadir_prestamo(prestamo)
        return prestamo

    def devolver(self) -> None:
        for k, prestamo in self.__prestamos.items(reverse=True):
            if not prestamo.devuelto():
                prestamo.devolver()
                return


class Usuario(persistent.Persistent):
    def __init__(self, ident: int, nombre: str) -> None:
        self.__ident = ident
        self.__nombre = nombre
        self.__prestamos = BTree()

    @property
    def ident(self) -> int:
        return self.__ident

    @property
    def nombre(self) -> str:
        return self.__nombre

    def prestamos(self) -> Iterator['Prestamo']:
        return self.__prestamos.values()

    def anyadir_prestamo(self, prestamo: 'Prestamo') -> None:
        self.__prestamos[prestamo.fecha_prestamo] = prestamo


class Prestamo(persistent.Persistent):
    def __init__(self, libro: Libro, usuario: Usuario, fecha_prestamo: str) -> None:
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion: str | None = None

    @property
    def libro(self) -> Libro:
        return self.__libro

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def fecha_prestamo(self) -> str:
        return self.__fecha_prestamo

    @property
    def fecha_devolucion(self) -> str | None:
        return self.__fecha_devolucion

    def devolver(self) -> None:
        self.__fecha_devolucion = 'xxxxxx'

    def devuelto(self) -> bool:
        return self.__fecha_devolucion is not None


rosa = Libro(100, 'El nombre de la rosa')
pepe = Usuario(1, 'Pepe')

rosa.prestar(pepe, '2026-05-13 16:00:00')
# rosa.devolver()
print(rosa.prestado())


almacen = FileStorage("biblioteca.fs")
bd = ZODB.DB(almacen)
conexion = bd.open()
raiz = conexion.root()

if not hasattr(raiz, 'libros'):
    raiz.libros = BTree()

raiz.libros[rosa.isbn] = rosa

if not hasattr(raiz, 'usuarios'):
    raiz.usuarios = BTree()

raiz.usuarios[pepe.ident] = pepe

# Libros actualmente prestados:

for libro in raiz.libros.values():
    if libro.prestado():
        print(libro)

# Historial de préstamos de un usuario:

for usuario in raiz.usuarios.values():
    for prestamo in usuario.prestamos():
        print(prestamo)

# Libros no disponibles:

for libro in raiz.libros.values():
    pass

transaction.commit()
conexion.close()
bd.close()
