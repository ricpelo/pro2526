def word_builder(ltr: list[str], pos: list[int]) -> str:
    """
    >>> word_builder(["g", "e", "o"], [1, 0, 2])
    'ego'
    >>> word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])
    'test'
    >>> word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])
    'edabit'
    """
    res: str = ''
    i = 0
    while i < len(pos):
        res += ltr[pos[i]]
        i += 1
    return res
    
    
    return res