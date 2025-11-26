def es_harshad(n: int) -> bool:
    """
    Devuelve True si n es un número de Harshad.
    
    Un número entero es un número de Harshad si es divisible
    por la suma de sus dígitos.
    
    >>> es_harshad(75)
    False
    >>> es_harshad(171)
    True
    >>> es_harshad(481)
    True
    """
    suma = 0
    m = n
    while m > 0:
        suma += m % 10
        m //= 10
    return n % suma == 0


def es_harshad2(n: int) -> bool:
    """
    Devuelve True si n es un número de Harshad.
    
    Un número entero es un número de Harshad si es divisible
    por la suma de sus dígitos.
    
    >>> es_harshad2(75)
    False
    >>> es_harshad2(171)
    True
    >>> es_harshad2(481)
    True
    """
    suma = 0
    m = str(n)
    i = 0
    while i < len(m):
        suma += int(m[i])
        i += 1
    return n % suma == 0
