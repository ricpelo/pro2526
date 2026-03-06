

class Persona:
    """
    Inv:
        - self.get_nombre() != ''
        - self.get_apellidos() != ''
        - self.get_dni() != ''
    """
        
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.set_nombre(nombre)
        self.__apellidos = apellidos
        self.__invariante()

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.__dni == otro.__dni
    
    def __hash__(self):
        return hash(self.__dni)

    def __repr__(self):
        dni = self.__dni
        nom = self.__nombre
        ape = self.__apellidos
        return f'Persona({dni!r}, {nom!r}, {ape!r})'

    def __str__(self):
        dni = self.__dni
        nom = self.__nombre
        ape = self.__apellidos
        return f'Esta persona tiene el DNI {dni} y se llama {nom} {ape}.'

    def __invariante(self):
        inv = self.get_nombre() != '' and
              self.get_apellidos() != '' and
              self.get_dni() != ''
        assert inv, "Violación del invariante."

    def __comprobar_vacio(self, valor):
        if valor == '':
            raise ValueError('El valor no puede ser vacío.')

    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_nombre_completo(self):
        return f'{self.__nombre} {self.__apellidos}'
    
    def __set_dni(self, dni):
        self.__comprobar_vacio(dni)
        self.__dni = dni
        assert self.get_dni() == dni
        self.__invariante()

    def set_nombre(self, nombre):
        self.__comprobar_vacio(nombre)
        self.__nombre = nombre
        assert self.get_nombre() == nombre
        self.__invariante()
        
    def set_apellidos(self, apellidos):
        self.__comprobar_vacio(apellidos)
        self.__apellidos = apellidos
        assert self.get_apellidos() == apellidos
        self.__invariante()
