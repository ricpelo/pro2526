

class Persona:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.dni == otro.dni
    
    def __hash__(self):
        return hash(self.dni)
