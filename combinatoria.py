def fact(n: int) -> int:
    """Devuelve el factorial de n."""
    return medio_fact(n, 0)


def medio_fact(n: int, k: int) -> int:
    """Devuelve 𝑛(𝑛−1)···(𝑘+1)."""
    i = k + 1
    prod = 1
    while i <= n:
        prod *= i
        i += 1
    return prod


def comb_iter(n: int, k: int) -> int:
    """Devuelve n sobre k."""
    return medio_fact(n, k) // fact(n - k)


def comb(n: int, k: int) -> int:
    """Devuelve n sobre k."""
    if k == 0 or n == k:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


def triangulo(num_lineas: int) -> None:
    """
    Imprime el triángulo de Tartaglia con el número de líneas indicado.
    """
    n = 0
    while n < num_lineas:
        k = 0
        while k <= n:
            print(comb_iter(n, k), end=' ')
            k += 1
        print()
        n += 1
    
    
def matriz_identidad(n: int) -> list[list[int]]:
    """Devuelve la matriz identidad de tamaño n x n."""
    ...
    
    
def imprimir_matriz(m: list[list]) -> None:
    """Imprime una matriz."""
    fila = 0
    while fila < len(m):
        col = 0
        while col < len(m[fila]):
            print(m[fila][col], end=' ')
            col += 1
        fila += 1
        print()

