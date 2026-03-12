class Empleado:
    def __init__(self, nombre, apellidos, salario):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__salario = salario
        
    @staticmethod
    def desde_cadena(c: str) -> 'Empleado':
        ...
        