"""
Módulo que implementa las pilas con una clase Pila.
"""

class Pila:
    """
    Una pila, es decir, una estructura LIFO.
    """
    
    def __init__(self):
        self.lista = []
        
    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.lista == otro.lista        
    
    def comprobar_vacia(self) -> None:
        if self.es_vacia():
            raise ValueError('La pila está vacía.')
    
    def apilar(self, elem) -> None:
        """Apila un nuevo elemento en la cima."""
        self.lista.append(elem)
        
    def cima(self):
        """
        Devuelve el elemento situado en la cima.
        Lanza un ValueError si la pila está vacía.
        """
        self.comprobar_vacia()
        return self.lista[-1]
    
    def es_vacia(self) -> bool:
        """Comprueba si la pila es vacía."""
        return len(self.lista) == 0
    
    def desapilar(self):
        """Saca de la pila el elemento situado en la cima y lo devuelve."""
        self.comprobar_vacia()
        return self.lista.pop()
        