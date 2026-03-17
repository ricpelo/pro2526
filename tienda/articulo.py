class Articulo:
    def __init__(self, codigo, denominacion, precio):
        self.__set_codigo(codigo)
        self.set_denominacion(denominacion)
        self.set_precio(precio)

    def __eq__(self, otro) -> bool:
        if type(self) != type(otro):
            return NotImplemented
        return self.codigo == self.otro
    
    def __hash__(self) -> str:
        return hash(self.codigo)

    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @property
    def denominacion(self) -> str:
        return self.__denominacion
    
    @property
    def precio(self) -> float:
        return self.__precio
    
    def __set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_denominacion(self, denominacion):
        self.__denominacion = denominacion
        
    def set_precio(self, precio):
        self.__precio = precio
