"""
6. Crear la clase abstracta Instrumento que almacena en una lista las notas musicales de
una melodía (dentro de una misma octava). El método concreto add añade nuevas notas
musicales. La clase también dispone del método abstracto interpretar con la siguiente
signatura:
interpretar() -> None
que, en cada subclase que herede de Instrumento, mostrará por la salida las notas
musicales según las interprete. Las notas serán constantes estáticas definidas dentro de
la clase Nota, de la siguiente forma:
class Nota:
DO = 'do'
RE = 're'
MI = 'mi'
FA = 'fa'
SOL = 'sol'
LA = 'la'
SI = 'si'
"""

from enum import StrEnum
from abc import ABC, abstractmethod
from time import sleep


class Nota(StrEnum):
    DO = 'do'
    RE = 're'
    MI = 'mi'
    FA = 'fa'
    SOL = 'sol'
    LA = 'la'
    SI = 'si'


class Instrumento(ABC):
    def __init__(self) -> None:
        self._melodia: list[Nota] = []
        
    def add(self, n: Nota) -> 'Instrumento':
        self._melodia.append(n)
        return self
        
    @abstractmethod
    def interpretar(self) -> None:
        ...


class Piano(Instrumento):
    def interpretar(self) -> None:
        print('El piano hace... ', end='')
        for nota in self._melodia:
            print(nota, end=' ')


class Flauta(Instrumento):
    def interpretar(self) -> None:
        print('La flauta hace... ', end='')
        for nota in self._melodia:
            sleep(1.0)
            print(nota, end=' ')
            

piano_cola = Piano()
piano_cola.add(Nota.DO).add(Nota.MI).add(Nota.FA).add(Nota.SOL).add(Nota.LA).add(Nota.DO)
piano_cola.interpretar()

print()

pan = Flauta()
pan.add(Nota.DO).add(Nota.MI).add(Nota.FA).add(Nota.SOL).add(Nota.LA).add(Nota.DO)
pan.interpretar()
