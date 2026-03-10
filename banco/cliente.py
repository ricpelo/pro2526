"""
Modelo de clientes de un banco.
"""

class Cliente:
    """
    Un cliente del banco.
    
    Inv: self.nombre != '' and self.apellidos != '' and self.dni != ''
    """
    
    def __init__(self, dni, nombre, apellidos):
        self.__set_dni(dni)
        self.nombre = nombre
        self.apellidos = apellidos
        self.__invariante()

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.dni == otro.dni
    
    def __hash__(self):
        return hash(self.dni)

    def __repr__(self):
        dni = self.dni
        nom = self.nombre
        ape = self.apellidos
        return f'Cliente({dni!r}, {nom!r}, {ape!r})'

    def __str__(self):
        dni = self.dni
        nom = self.nombre
        ape = self.apellidos
        return f'Esta persona tiene el DNI {dni} y se llama {nom} {ape}.'

    def __invariante(self):
        inv = self.nombre != '' and \
              self.apellidos != '' and \
              self.dni != ''
        assert inv, "Violación del invariante."

    def __comprobar_vacio(self, valor):
        if valor == '':
            raise ValueError('El valor no puede ser vacío.')

    def get_dni(self):
        return self.__dni
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__comprobar_vacio(nombre)
        self.__nombre = nombre
        assert self.nombre == nombre
        self.__invariante()    

    def get_nombre_completo(self):
        return f'{self.nombre} {self.apellidos}'
    
    @property
    def dni(self):
        return self.__dni
    
    def __set_dni(self, dni):
        self.__comprobar_vacio(dni)
        self.__dni = dni
        assert self.dni == dni
        self.__invariante()

    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def set_apellidos(self, apellidos):
        self.__comprobar_vacio(apellidos)
        self.__apellidos = apellidos
        assert self.apellidos == apellidos
        self.__invariante()
    