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
        
    def __eq__(self, otro) -> bool:
        if type(self) != type(otro):
            return NotImplemented
        return self.cantidad == otro.cantidad and \
               self.concepto == otro.concepto

    def __hash__(self):
        return hash((self.cantidad, self.concepto))
    
    def __repr__(self) -> str:
        return f'Movimiento({self.concepto!r}, {self.cantidad!r})'

    def __str__(self) -> str:
        return f'Movimiento de tipo {self.concepto} por importe de {self.cantidad:.2f} €.'

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