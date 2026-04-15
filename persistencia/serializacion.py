"""
Ejemplo de uso del módulo pickle
"""

import pickle


class Empleado:
    def __init__(self, nombre: str, salario: float) -> None:
        self.nombre = nombre
        self.salario = salario

    def __repr__(self) -> str:
        return f'Empleado({self.nombre!r}, {self.salario!r})'


class Departamento:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.empleados: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)

    def get_empleados(self) -> list[Empleado]:
        return self.empleados

    def __repr__(self) -> str:
        return f'Departamento({self.nombre!r})'


def guardar_datos(archivo: str, objeto) -> None:
    """Guarda el objeto en un archivo."""
    with open(archivo, 'wb') as f:
        pickle.dump(objeto, f)


def cargar_datos(archivo: str):
    """Carga el objeto desde el archivo."""
    with open(archivo, 'rb') as f:
        return pickle.load(f)


e1 = Empleado('Juan Pérez', 30000.00)
e2 = Empleado('María López', 35000.00)

d1 = Departamento('Informática')
d1.agregar_empleado(e1)
d1.agregar_empleado(e2)

e3 = Empleado('José Martínez', 15000.00)

d2 = Departamento('Inglés')
d2.agregar_empleado(e3)

deps = [d1, d2]
guardar_datos('departamentos.pickle', deps)

deps_guardados = cargar_datos('departamentos.pickle')

for dep in deps_guardados:
    print(dep.nombre, dep.get_empleados())

print(id(e3))
print(id(deps_guardados[1].get_empleados()[0]))
print(e3)
print(deps_guardados[1].get_empleados()[0])
