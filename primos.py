def es_primo(n: int) -> bool:
    """
    Comprueba si un número entero es primo o compuesto.
    
    Args:
        n (int): El número a comprobar.
        
    Returns:
        True si es primo, o False si es compuesto.
        
    >>> es_primo(4)
    False
    >>> es_primo(17)
    True
    """
    def divisores(n: int) -> list[int]:
        res = []
        i = 1
        while i <= n:
            if n % i == 0:
                res.append(i)
            i += 1
        return res

    return len(divisores(n)) == 2
