"""
Programar en Python un modelo orientado a objetos del problema de representar puertas y llaves.
Para ello, hay que programar las clases Puerta y Llave. Las puertas y las llaves tienen un color (una
cadena). Una puerta puede estar abierta o cerrada. Una puerta puede tener puesta una llave o ninguna.
Para abrir una puerta, debe tener puesta una llave del mismo color que la puerta. Para cerrar una
puerta no se necesita ninguna llave (si la tiene puesta, da igual).
La clase Puerta debe contar, al menos, con los siguientes métodos además del constructor:
poner(llave): pone una llave en la cerradura de la puerta; devuelve el propio objeto Puerta.
quitar(): quita la llave de la puerta; devuelve la llave que estaba puesta en la puerta, o None si
no tenía ninguna llave puesta.
abrir(): abre la puerta, si es posible; devuelve True si se ha podido abrir (o ya estaba abierta) o
False en caso contrario.
cerrar(): cierra la puerta; no devuelve ningún valor.

La clase Llave debe contar, al menos, con los siguientes métodos además del constructor:
color(): devuelve el color de la llave.

Tests:
Puerta('rojo').poner(Llave('rojo')).abrir() == True
Puerta('rojo').poner(Llave('verde')).abrir() == False
Puerta('rojo').abrir() == False
"""

class Llave:
    def __init__(self, color: str) -> None:
        self.__color = color
        
    @property
    def color(self) -> str:
        return self.__color
    
class Puerta:
    def __init__(self, color: str) -> None:
        self.__color: str = color
        self.__llave: Llave | None = None
        self.__abierta: bool = False

    @property
    def color(self) -> str:
        return self.__color
    
    @property
    def llave(self) -> Llave | None:
        return self.__llave
    
    def poner(self, llave: Llave) -> 'Puerta':
        self.__llave = llave
        return self
        
    def quitar(self) -> Llave | None:
        llave = self.llave
        self.__llave = None
        return llave
        
    def abrir(self) -> bool:
        if self.llave is not None and self.llave.color == self.color:
            self.__abierta = True
            return True
        return False
    
    def cerrar(self) -> None:
        self.__abierta = False

    
assert Puerta('rojo').poner(Llave('rojo')).abrir()
assert not Puerta('rojo').poner(Llave('verde')).abrir()
assert not Puerta('rojo').abrir()
