"""
Programar en Python un modelo orientado a objetos que simule el funcionamiento de la gestión de
reservas de asientos en una sala de cine.
El modelo debe contar con una clase Sala que represente una sala del cine.
Al crear una sala, se debe indicar el número de filas y el número de asientos por fila que tiene la sala.
Las salas deben responder, entre otros, a los siguientes métodos:
reservar(fila, asiento): Reserva un asiento si está libre. Devuelve True si se reserva correctamente,
o False si ya estaba ocupado o es incorrecto.
liberar(fila, asiento): Libera un asiento si estaba ocupado. Devuelve True si se libera, o False
en caso contrario.
ocupacion(): Devuelve el número total de asientos ocupados.
disponibles_en_fila(fila): Devuelve el número de asientos libres en esa fila.

Ejemplos de uso:
s = Sala(3, 5)
s.reservar(0, 0) == True
s.reservar(0, 0) == False
s.ocupacion() == 1
s.disponibles_en_fila(0) == 4
"""

class Sala:
    def __init__(self, num_filas: int, num_asientos: int) -> None:
        self.num_filas = num_filas
        self.num_asientos = num_asientos
        self.__reservas: set[tuple[int, int]] = set()

    @property
    def num_filas(self) -> int:
        return self.__num_filas

    @property
    def num_asientos(self) -> int:
        return self.__num_asientos

    @num_filas.setter
    def num_filas(self, num_filas: int) -> None:
        if num_filas < 0:
            raise ValueError('No puede ser negativo.')
        self.__num_filas = num_filas

    @num_asientos.setter
    def num_asientos(self, num_asientos: int) -> None:
        if num_asientos < 0:
            raise ValueError('No puede ser negativo.')
        self.__num_asientos = num_asientos

    def reservar(self, fila: int, asiento: int) -> bool:
        """
        Reserva un asiento si está libre.
        Devuelve True si se reserva correctamente,
        o False si ya estaba ocupado o es incorrecto.
        """
        if fila not in range(0, self.num_filas):
            return False
        if asiento not in range(0, self.num_asientos):
            return False
        if (fila, asiento) in self.__reservas:
            return False
        self.__reservas.add((fila, asiento))
        return True

    def liberar(self, fila: int, asiento: int) -> bool:
        """
        Libera un asiento si estaba ocupado.
        Devuelve True si se libera, o False en caso contrario.
        """
        if (fila, asiento) in self.__reservas:
            self.__reservas.remove((fila, asiento))
            return True
        return False

    def ocupacion(self) -> int:
        """
        Devuelve el número total de asientos ocupados.
        """
        return len(self.__reservas)

    def disponibles_en_fila(self, fila: int) -> int:
        """
        Devuelve el número de asientos libres en esa fila.
        """
        return self.num_asientos - sum(1 for f, _ in self.__reservas if f == fila)


if __name__ == '__main__':
    s = Sala(3, 5)
    assert s.reservar(0, 0) == True
    assert s.reservar(0, 0) == False
    assert s.ocupacion() == 1
    assert s.disponibles_en_fila(0) == 4
