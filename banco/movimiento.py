"""
Movimientos de una cuenta de un banco.
"""

class Movimiento:
    """
    Representa un movimiento dentro de una cuenta del banco.
    Los movimientos son inmutables.
    
    Inv: self.concepto != ''
    """
    
    def __init__(self, concepto: str, cantidad: float) -> None:
        self.__set_concepto(concepto)
        self.__cantidad = cantidad
        
    @property
    def concepto(self) -> str:
        return self.__concepto
    
    def __set_concepto(self, concepto) -> None:
        if concepto == '':
            raise ValueError('El concepto no puede ser vacío.')
        self.__concepto = concepto
        assert self.concepto == concepto
        
    @property
    def cantidad(self) -> float:
        return self.__cantidad