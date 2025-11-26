
def suma2(lst: list[int], total: int) -> tuple[int, int]:
    """
    >>> suma2([1, 3, 5], 6)
    (1, 5)
    >>> suma2([2, 3, 4, 1, 5], 6)
    (2, 4)
    >>> suma2([1, 3, 5], 14)
    ()
    """
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == total:
                return (lst[i], lst[j])
            j += 1
        i += 1
    return ()
