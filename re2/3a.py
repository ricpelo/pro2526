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

class Alumno:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__notas: list[float] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    def anyadir_calificacion(self, calificacion: float) -> None:
        if calificacion < 0.0 or calificacion > 10.0:
            raise ValueError('Calificación incorrecta.')
        self.__notas.append(calificacion)

    def media(self) -> float | None:
        if len(self.__notas) == 0:
            return None
        return sum(self.__notas) / len(self.__notas)
