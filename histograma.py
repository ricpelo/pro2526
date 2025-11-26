def histogram(lst: list[int], char: str) -> str:
    """
    >>> histogram([1, 3, 4], "#")
    '#\n###\n####'
    >>> histogram([6, 2, 15, 3], "=")
    '======\n==\n===============\n==='
    >>> histogram([1, 10], "+")
    '+\n++++++++++'
    """
    res: list[str] = []
    i = 0
    while i < len(lst):
        res.append(char * lst[i])
        i += 1
    return '\n'.join(res)
