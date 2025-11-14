"""
Escribir una función que implemente la siguiente especificación:
Pre : len(𝑐) = 1
es_vocal(𝑐: str) -> bool
Post : es_vocal(𝑐) = 𝑐 es una vocal, acentuada o no
Dar un ejemplo de uso.
"""

# quita_acentos = lambda s: s.translate(''.maketrans('áéíóúÁÉÍÓÚ', 'aeiouAEIOU'))
# es_vocal = lambda c: 'aeiou'.find(quita_acentos(c.lower())) != -1

es_vocal = lambda c: 'aeiouAEIOUáéíóúÁÉÍÓÚ'.find(c) != -1

salida = es_vocal('E')
