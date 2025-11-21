def factorial(n: int) -> int:
    """
    Devuelve el factorial de un número entero.

    >>> factorial(4)
    24
    >>> factorial(5)
    130
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
