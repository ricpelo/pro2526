from abc import ABC, abstractmethod    # importamos del módulo abc

class Figura(ABC):                     # Figura es subclase de ABC
    def __init__(self, ancho: float, alto: float) -> None:
        self.set_ancho(ancho)
        self.set_alto(alto)

    def set_ancho(self, ancho: float) -> None:
        self.__ancho = ancho

    def set_alto(self, alto: float) -> None:
        self.__alto = alto

    def get_ancho(self) -> float:
        return self.__ancho

    def get_alto(self) -> float:
        return self.__alto

    @abstractmethod                    # declaramos el método como abstracto
    def area(self) -> float:
        ...                            # representa que no tiene cuerpo
        


class Triangulo(Figura):
    def area(self) -> float:
        return self.get_ancho() * self.get_alto() / 2.0

    def dibujar(self) -> None:
        print("  *  ")
        print(" *** ")
        print("*****")

    # resto de código


class Rectangulo(Figura):
    def area(self) -> float:
        return self.get_ancho() * self.get_alto()

   

    # resto de código
