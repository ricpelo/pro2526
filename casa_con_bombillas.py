"""
Ejercicio 11 de POO (II):
-------------------------
Modelar una casa con muchas bombillas, de forma que cada bombilla se puede
encender o apagar individualmente. Para ello, hacer una clase Bombilla con
una variable privada que indique si está encendida o apagada, así como un
método que nos diga el estado de una bombilla concreta. Además, queremos
poner un interruptor general, de forma que si este se apaga, todas las
bombillas quedan apagadas, según estuvieran antes. Cada bombilla se
enciende y se apaga individualmente, pero sólo responde que está encendida
si su interruptor particular está activado y además hay luz general.
"""

class Casa:
    """
    Una casa.
    """
    
    def __init__(self):
        self.__interruptor = True     # Interruptor general
        
    def esta_activado(self) -> bool:
        return self.__interruptor
    
    def activar(self) -> None:
        self.__interruptor = True
        
    def desactivar(self) -> None:
        self.__interruptor = False


class Bombilla:
    """
    Una bombilla.
    """
    
    def __init__(self, casa = None):
        self.__encendida = False
        self.__casa: Casa | None = casa
        
    def esta_encendida(self) -> bool:
        return self.__encendida and \
               self.__casa is not None and \
               self.__casa.esta_activado()
    
    def encender(self) -> None:
        self.__encendida = True
        
    def apagar(self) -> None:
        self.__encendida = False

    def set_casa(self, casa: Casa | None) -> None:
        self.__casa = casa


if __name__ == '__main__':
    pepe = Casa()
    b1 = Bombilla(pepe)
    b2 = Bombilla(pepe)
    b3 = Bombilla()
    assert not b1.esta_encendida()
    assert not b2.esta_encendida()
    assert not b3.esta_encendida()
    b1.encender()
    assert b1.esta_encendida()
    pepe.desactivar()
    assert not b1.esta_encendida()
    assert not b2.esta_encendida()