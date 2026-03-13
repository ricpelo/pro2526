from bombilla import Bombilla

class Casquillo:
    """
    Un casquillo de una lámpara.
    """
    
    def __init__(self, tamanyo: str) -> None:
        self.__set_tamanyo(tamanyo)
        self.__bombilla: Bombilla | None = None

    def __repr__(self) -> str:
        return f'Casquillo({self.tamanyo!r})'

    @property
    def tamanyo(self) -> str:
        return self.__tamanyo
    
    def __set_tamanyo(self, tamanyo: str) -> None:
        if tamanyo not in ('P', 'M'):
            raise ValueError('El tamaño es incorrecto.')
        self.__tamanyo = tamanyo
        
    @property
    def bombilla(self) -> Bombilla | None:
        """
        Devuelve la bombilla que hay en el casquillo, si la hay.
        Si no la hay, devuelve None.
        """
        return self.__bombilla
    
    def poner(self, bombilla: Bombilla) -> None:
        """Pone una bombilla en el casquillo."""
        if self.tamanyo != bombilla.tamanyo:
            raise ValueError('El tamaño de la bombilla no es el correcto.')
        self.__bombilla = bombilla
        
    def quitar(self) -> None:
        """Quita la bombilla del casquillo, caso de haberla."""
        self.__bombilla = None
    
    def esta_vacio(self) -> bool:
        return self.bombilla is None