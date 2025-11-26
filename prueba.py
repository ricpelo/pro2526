def arbol(n: int) -> None:
    """Dibuja un árbol con un determinado número de líneas."""
    def ancho(num_lineas: int) -> int:
        """Calcula el ancho del dibujo a partir del número de líneas."""
        return 2 * num_lineas - 1
    def imprime_linea(num_ast: int, anch: int) -> None:
        """Imprime la línea indicada con el ancho indicado."""
        print(('*' * num_ast).center(anch, '·'))
    if n > 0:
        an = 2 * n - 1
        i = 1
        while i < n:
            imprime_linea(2 * i - 1, an)
            i += 1
        imprime_linea(1, an)   # La última línea es igual que la primera
