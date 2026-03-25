"""
Diseñar la clase Hora, que representa un instante de tiempo compuesto por la
hora (de 0 a 23) y los minutos. Dispone de los métodos:
__init__(hora,minutos): construye un objeto con los datos pasados como argu-
mentos.
inc(): incrementa el instante en un minuto y no devuelve nada.
set_minutos(valor): asigna un valor (si es válido) a los minutos. Devuelve True
o False según se haya podido modificar los minutos o no.
set_hora(valor): asigna un valor (si está comprendido entre 0 y 23) a la hora.
Devuelve True o False según se haya podido cambiar la hora o no.
__str__(): devuelve una cadena con la representación de la hora.

A partir de la clase Hora diseñada en el ejercicio anterior, implementar la clase
HoraExacta, que incluye en la hora los segundos. Además de los métodos heredados
desde la clase Hora, dispondrá de:
__init__(hora,minutos,segundos): construye un objeto con los datos pasados
como argumentos.
set_segundos(valor): asigna un valor (si está comprendido entre 0 y 59) a los
segundos. Devuelve True o False según se haya podido cambiar los segundos o
no.
inc(): incrementa la hora en un segundo.
"""

class Hora:
    def __init__(self, hora: int, minutos: int) -> None:
        self.set_hora(hora)
        self.set_minutos(minutos)
        
    def __eq__(self, otro):
        if isinstance(otro, type(self)):
            return NotImplemented
        return (self.__hora, self.__minutos) == (otro.__hora, otro.__minutos)
        
    def set_hora(self, hora: int) -> None:
        if hora not in range(0, 24):
            return False
        self.__hora = hora
        return True
        
    def set_minutos(self, minutos: int) -> bool:
        if minutos not in range(0, 60):
            return False
        self.__minutos = minutos
        return True
    
    def inc(self) -> None:
        self.__minutos = (self.__minutos + 1) % 60
        if self.__minutos == 0:
            self.__hora = (self.__hora + 1) % 24
        
    def __str__(self) -> str:
        return f'{self.__hora:02}:{self.__minutos:02}'


class HoraExacta(Hora):
    def __init__(self, hora: int, minutos: int, segundos: int) -> None:
        super().__init__(hora, minutos)
        self.set_segundos(segundos)
        
    def __eq__(self, otro):
        ...
        
    def set_segundos(self, segundos: int) -> bool:
        if segundos not in range(0, 60):
            return False
        self.__segundos = segundos
        return True

    def inc(self) -> None:
        self.__segundos = (self.__segundos + 1) % 60
        if self.__segundos == 0:
            super().inc()

    def __str__(self) -> str:
        return super().__str__() + f':{self.__segundos:02}'


if __name__ == '__main__':
    h = Hora(14, 5)
    assert str(h) == '14:05'
    h = Hora(23, 59)
    h.inc()
    assert str(h) == '00:00'
    h = HoraExacta(14, 5, 0)
    assert str(h) == '14:05:00'
    h = HoraExacta(23, 59, 59)
    h.inc()
    assert str(h) == '00:00:00'