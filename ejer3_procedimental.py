def cuadrado(n: int) -> None:
    """
    Imprime un cuadrado usando asteriscos con el número de líneas y columnas indicado.
    
    Args:
        n (int): El número de líneas (y columnas) deseado.
        
    Returns:
        None
    
    >>> cuadrado(0)
    >>> cuadrado(1)
    *
    >>> cuadrado(2)
    **
    **
    >>> cuadrado(3)
    ***
    ***
    ***
    >>> cuadrado(5)
    *****
    *****
    *****
    *****
    *****
    >>>
    """
    i = 0
    while i < n:
        print('*' * n)
        i += 1
        
        
def diagonal(n: int) -> None:
    """Dibuja una diagonal."""
    i = 0
    while i < n:
        print(' ' * i, '*')
        i += 1


def arbol(n: int) -> None:
    """Dibuja un árbol con un determinado número de líneas."""
    def ancho(num_lineas: int) -> int:
        """Calcula el ancho del dibujo a partir del número de líneas."""
        return 2 * num_lineas - 1
    def imprime_linea(num_linea: int, anch: int) -> None:
        """Imprime la línea indicada con el ancho indicado."""
        print(('*' * ancho(num_linea)).center(anch, '·'))
    if n > 0:
        an = ancho(n)
        i = 1
        while i < n:
            imprime_linea(i, an)
            i += 1
        imprime_linea(1, an)   # La última línea es igual que la primera

    
    
    
    
    
    