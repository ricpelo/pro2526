from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def mover(self) -> None:
        ...

class Gato(Animal):
    def mover(self) -> None:
        print('Se mueve caminando.')

class Pez(Animal):
    def mover(self) -> None:
        print('Se mueve nadando.')


def mover_dos_veces(a: Animal):
    a.mover()
    a.mover()
