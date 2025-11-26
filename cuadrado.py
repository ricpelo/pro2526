def cuadrado(n: int) -> list[list[int]]:
    """
    >>> cuadrado(4)
    [[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]]
    >>> cuadrado(3)
    [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    >>> cuadrado(2)
    [[1, 2], [2, 1]]
    >>> cuadrado(1)
    [[1]]
    """
    def primera(tam: int) -> list[int]:        
        p = []
        i = 1
        while i <= tam:
            p.append(i)
            i += 1
        return p
    def rotar(lst: list) -> list:
        return [lst[-1]] + lst[:-1]
    p = primera(n)
    res = [p]
    i = 2
    while i <= n:
        p = rotar(p)
        res.append(p)
        i += 1
    return res
