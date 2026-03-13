from casquillo import Casquillo
from bombilla import Bombilla

class Lampara:
    """
    Una lámpara.
    """
    
    def __init__(
        self,
        num_pequenyos: int,
        num_medianos: int,
        potencia_maxima: float
    ):
        self.__set_potencia_maxima(potencia_maxima)
        self.__casquillos: set[Casquillo] = set()
        
        for _ in range(num_pequenyos):
            self.__casquillos.add(Casquillo('P'))

        for _ in range(num_medianos):
            self.__casquillos.add(Casquillo('M'))

    @property
    def potencia_maxima(self) -> float:
        return self.__potencia_maxima
    
    def __set_potencia_maxima(self, potencia_maxima: float) -> None:
        if potencia_maxima < 0:
            raise ValueError('La potencia máxima no puede ser negativa.')
        self.__potencia_maxima = potencia_maxima
        
    @property
    def casquillos(self) -> set[Casquillo]:
        return self.__casquillos.copy()
    
    def poner(bombilla: Bombilla):
        for casquillo in self.__casquillos:
            if bombilla.tamanyo == casquillo.tamanyo and \
               casquillo.esta_vacio():
                ...
                