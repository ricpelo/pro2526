"""
Programar en Python un modelo orientado a objetos que simule el funcionamiento de un sistema de
evaluación de alumnos.
Debe contener, al menos, las clases Alumno y Asignatura.
Los alumnos deben tener un nombre y una lista de calificaciones (números reales).
Las asignaturas deben tener un nombre y una lista de alumnos matriculados.
Los alumnos deben responder, entre otros, a los siguientes métodos:
añadir_calificacion(calificacion): la calificación debe estar entre 0 y 10 (en caso contrario, lanzará
una excepción ValueError).
media(): media de las calificaciones (None si no tiene).
Las asignaturas deben responder, entre otros, a los siguientes métodos:
matricular(alumno): matricula a un alumno en esa asignatura.
media_asignatura(): la calificación media de todos los alumnos que tengan calificaciones en esa
asignatura.
aprobados(): número de alumnos con media mayor o igual que cinco.
mejor_alumno(): devuelve el alumno con mayor media. En caso de empate, debe devolver uno
cualquiera de los que tienen mayor media. Si no hay datos, debe devolver None.
"""

from typing import Iterator

class Alumno:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__notas: list[float] = []

    def __lt__(self, otro):
        def coalesce(a, b):
            return a if a is not None else b
        if not isinstance(otro, type(self)):
            return NotImplemented
        return coalesce(self.media(), 0) < coalesce(otro.media(), 0)

    @property
    def nombre(self) -> str:
        return self.__nombre

    def notas(self) -> Iterator[float]:
        return iter(self.__notas)

    def anyadir_calificacion(self, calificacion: float) -> None:
        if calificacion < 0.0 or calificacion > 10.0:
            raise ValueError('Calificación incorrecta.')
        self.__notas.append(calificacion)

    def media(self) -> float | None:
        if len(self.__notas) == 0:
            return None
        return sum(self.__notas) / len(self.__notas)


class Asignatura:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__alumnos: set[Alumno] = set()

    @property
    def nombre(self) -> str:
        return self.__nombre

    def matricular(self, alumno: Alumno) -> None:
        """Matricula a un alumno en esa asignatura."""
        self.__alumnos.add(alumno)

    def media_asignatura(self) -> float:
        """
        La calificación media de todos los alumnos que tengan
        calificaciones en esa asignatura.
        """
        suma, cantidad = 0.0, 0
        for alumno in self.__alumnos:
            for nota in alumno.notas():
                suma += nota
                cantidad += 1
        return suma / cantidad

    @staticmethod
    def __coalesce(a, b):
        return a if a is not None else b

    def aprobados(self) -> int:
        """Número de alumnos con media mayor o igual que cinco."""
        return sum(1 for alumno in self.__alumnos if Asignatura.__coalesce(alumno.media(), 0) >= 5)

    def mejor_alumno(self) -> Alumno | None:
        """
        Devuelve el alumno con mayor media. En caso de empate, debe devolver uno
        cualquiera de los que tienen mayor media.
        Si no hay datos, debe devolver None.
        """
        if sum(1 for alumno in self.__alumnos for _ in alumno.notas()) == 0:
            return None
        return max(self.__alumnos)
        return max(self.__alumnos, key=lambda a: Asignatura.__coalesce(a.media(), 0))


if __name__ == '__main__':
    a1 = Alumno("Ana")
    a2 = Alumno("Luis")
    a1.anyadir_calificacion(8)
    a1.anyadir_calificacion(6)
    a2.anyadir_calificacion(4)
    asig = Asignatura("Prog")
    asig.matricular(a1)
    asig.matricular(a2)
    assert asig.media_asignatura() == 6
    assert asig.aprobados() == 1
    assert asig.mejor_alumno() == a1
