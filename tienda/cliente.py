class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.__set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)

    def __eq__(self, otro) -> bool:
        if type(self) != type(otro):
            return NotImplemented
        return self.dni == self.otro
    
    def __hash__(self) -> str:
        return hash(self.dni)

    @property
    def dni(self) -> str:
        return self.__dni
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def apellidos(self) -> str:
        return self.__apellidos
    
    def __set_dni(self, dni):
        self.__dni = dni
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos