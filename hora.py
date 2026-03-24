"""
8. Escribir un programa que lea por la entrada una hora cualquiera y un
número 𝑛 que representa una cantidad en segundos. El programa mostrará
la hora introducida y las 𝑛 siguientes, que se diferencian en un
segundo. Para ello, hemos de diseñar previamente la clase Hora que
dispone de los campos hora, minuto y segundo. Los valores de los
campos se controlarán mediantes métodos get/set.
"""

class Hora:
    def __init__(self, hora: int, minuto: int, segundo: int) -> None:
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        
    @property
    def hora(self) -> int:
        return self.__hora
    
    @hora.setter
    def hora(self, hora: int) -> None:
        if hora not in range(0, 24):
            raise ValueError('La hora es incorrecta.')
        self.__hora = hora
        assert self.hora == hora
        
    @property
    def minuto(self) -> int:
        return self.__minuto
    
    @minuto.setter
    def minuto(self, minuto: int) -> None:
        if minuto not in range(0, 60):
            raise ValueError('El minuto es incorrecto.')
        self.__minuto = minuto
        assert self.minuto == minuto

    @property
    def segundo(self) -> int:
        return self.__segundo
    
    @segundo.setter
    def segundo(self, segundo: int) -> None:
        if segundo not in range(0, 60):
            raise ValueError('El segundo es incorrecto.')
        self.__segundo = segundo
        assert self.segundo == segundo
        
    def __str__(self) -> str:
        return f'{self.hora:02}:{self.minuto:02}:{self.segundo:02}'
    
    def __repr__(self) -> str:
        return f'Hora({self.hora!r}, {self.minuto!r}, {self.segundo!r})'
    
    def incrementar_segundo(self) -> None:
        self.segundo = (self.segundo + 1) % 60
        if self.segundo == 0:
            self.minuto = (self.minuto + 1) % 60
            if self.minuto == 0:
                self.hora = (self.hora + 1) % 24
        

try:
    entrada = input('Introduzca una hora en formato hh:mm:ss: ')
    h, m, s = map(int, entrada.split(':'))
    hora = Hora(h, m, s)
    n = int(input('Introduzca el valor de n: '))
    for _ in range(n + 1):
        print(hora)
        hora.incrementar_segundo()
except ValueError:
    print('La entrada es incorrecta.')
