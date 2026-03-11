"""
Cuentas del banco.
"""

from cliente import Cliente
from movimiento import Movimiento

class Cuenta:
    """
    Una cuenta del banco.
    
    Inv:
        - Un número de cuenta no puede ser negativo ni tener más
          de 20 dígitos.
        - El saldo debe ser igual a la suma de las cantidades de
          todos sus movimientos.
    """
    
    def __init__(self, numero: int, titular: Cliente) -> None:
        self.__set_numero(numero)
        self.titular = titular
        self.__movimientos: list[Movimiento] = []
        self.__saldo: float = 0.00

    def __iter__(self):
        return iter(self.__movimientos)

    def __str__(self) -> str:
        return f'La cuenta número {self.numero} tiene {self.saldo:.2f} €.'

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numero == otro.numero
    
    def __hash__(self):
        return hash(self.numero)

    def __invariante(self):
        assert self.saldo == sum(m.cantidad for m in self.__movimientos)

    @property
    def numero(self) -> int:
        return self.__numero
    
    def __set_numero(self, numero) -> None:
        """
        Un número de cuenta no puede ser negativo ni tener más
        de 20 dígitos.
        """
        if numero < 0 or len(str(numero)) > 20:
            raise ValueError('El número de cuenta es incorrecto.')
        self.__numero = numero
        assert self.numero == numero
        
    @property
    def titular(self) -> Cliente:
        return self.__titular
    
    @titular.setter
    def titular(self, titular: Cliente) -> None:
        self.__titular = titular
        assert self.titular == titular
        
    @property
    def saldo(self) -> float:
        return self.__saldo
    
    def agregar_movimiento(self, concepto: str, cantidad: float) -> None:
        self.__movimientos.append(Movimiento(concepto, cantidad))
        self.__saldo += cantidad
        self.__invariante()
        