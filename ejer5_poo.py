"""
Crear la clase Persona con un método compara_edad que compare la edad de una
persona con la de otra.
Ejemplos:
>>> p1 = Persona('Samuel', 24)
>>> p2 = Persona('Jael', 36)
>>> p3 = Persona('Liliana', 24)
>>> p1.compara_edad(p2)
'Jael es más viejo que yo.'
>>> p2.compara_edad(p1)
'Samuel es más joven que yo.'
>>> p1.compara_edad(p3)
'Liliana tiene la misma edad que yo.'
"""

class Persona:
    """
    La clase que representa una persona.
    """
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def compara_edad(self, otra: 'Persona') -> str:
        """Compara la edad de dos personas."""
        if self.edad > otra.edad:
            return f'{otra.nombre} es más joven que yo.'
        if self.edad < otra.edad:
            return f'{otra.nombre} es más viejo que yo.'
        return f'{otra.nombre} tiene la misma edad que yo.'


if __name__ == '__main__':
    p1 = Persona('Samuel', 24)
    p2 = Persona('Jael', 36)
    p3 = Persona('Liliana', 24)
    print(p1.compara_edad(p2)) # 'Jael es más viejo que yo.'
    print(p2.compara_edad(p1)) # 'Samuel es más joven que yo.'
    print(p1.compara_edad(p3)) # 'Liliana tiene la misma edad que yo.'
