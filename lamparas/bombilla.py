class Bombilla:
    """
    Una bombilla.
    """
    
    def __init__(self, potencia: float, tamanyo: str) -> None:
        self.__set_potencia(potencia)
        self.__set_tamanyo(tamanyo)
    
    def __eq__(self, otro) -> bool:
        if type(self) != type(otro):
            return NotImplemented
        return (self.potencia, self.tamanyo) == (otro.potencia, otro.tamanyo)
    
    def __hash__(self) -> int:
        return hash((self.potencia, self.tamanyo))
    
    @property
    def potencia(self) -> float:
        return self.__potencia
    
    def __set_potencia(self, potencia: float) -> None:
        if potencia < 0:
            raise ValueError('La potencia no puede ser negativa.')
        self.__potencia = potencia
        
    @property
    def tamanyo(self) -> str:
        return self.__tamanyo
    
    def __set_tamanyo(self, tamanyo: str) -> None:
        if tamanyo not in ('P', 'M'):
            raise ValueError('El tamaño es incorrecto.')
        self.__tamanyo = tamanyo
    