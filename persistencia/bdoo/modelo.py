"""
Definición de las clases del modelo de objetos.
"""

from typing import Iterator
import persistent
from BTrees.OOBTree import BTree # type: ignore


class Empleado(persistent.Persistent):
    def __init__(self, dni: str, nombre: str, salario: float) -> None:
        self.dni = dni
        self.nombre = nombre
        self.salario = salario

    def __repr__(self) -> str:
        return f'Empleado({self.dni!r}, {self.nombre!r}, {self.salario!r})'


class Departamento(persistent.Persistent):
    def __init__(self, numero: int, nombre: str) -> None:
        self.numero = numero
        self.nombre = nombre
        self.empleados = BTree()

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.empleados[empleado.dni] = empleado

    def get_empleados(self) -> Iterator[Empleado]:
        return self.empleados.values()

    def __repr__(self) -> str:
        return f'Departamento({self.numero!r}, {self.nombre!r})'
