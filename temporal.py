def maximo_no_adyacente(lista: list[int]) -> int:
    """
    que devuelva el mayor valor de la lista tal que ningún otro elemento igual esté adyacente a él.
    Ejemplo:
    >>> maximo_no_adyacente([4, 4, 2, 4])
    2 # Porque los 4 están adyacentes
    >>> maximo_no_adyacente([3, 5, 3])
    5
    """
    i = 0
    while i < len(lista):
        n = lista[i]
        if i > 0 and lista[i - 1] == n or i < len(lista) - 1 and lista[i + 1] == n:
            while lista.count(n) > 0:
                lista.remove(n)
        else:
            i += 1
    return max(lista)