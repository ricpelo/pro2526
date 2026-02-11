"""
Módulo que saluda.
"""

_nombre = 'Pepe'

def hola():
    """Saluda al usuario."""
    print('Hola', _nombre)
    
print(hola.__globals__)

print(globals() is hola.__globals__)
