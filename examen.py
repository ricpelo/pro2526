def secuencia_consecutiva(lst1, lst2):
    """
    >>> secuencia_consecutiva([1, 4, 5, 7], [2, 3, 6])
    True
    >>> secuencia_consecutiva([1, 4, 5, 6], [2, 7, 8, 9])
    False
    >>> secuencia_consecutiva([1, 4, 5, 6], [2, 3, 7, 8, 10])
    False
    >>> secuencia_consecutiva([44, 46], [45])
    True
    """
    if len(lst1) == 0 and len(lst2) == 0:
        return True
    if len(lst1) == 0 and len(lst2) == 1:
        return True
    if len(lst1) == 1 and len(lst2) == 0:
        return True
    if len(lst1) > 0 and len(lst2) > 0 and lst1[0] == lst2[0] + 1:
        return secuencia_consecutiva(lst1[1:], lst2[1:])
    if len(lst1) > 0 and len(lst2) > 0 and lst2[0] == lst1[0] + 1:
        return secuencia_consecutiva(lst1[1:], lst2[1:])
    if len(lst1) > 1 and lst1[0] == lst1[1] + 1:
        return secuencia_consecutiva(lst1[2:], lst2)
    if len(lst2) > 1 and lst2[0] == lst2[1] + 1:
        return secuencia_consecutiva(lst1, lst2[2:])
    return False

    # [7]  []