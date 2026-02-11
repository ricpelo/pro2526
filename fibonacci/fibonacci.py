"""
Módulo que implementa varias funciones que calculan el enésimo
término de la sucesión de Fibonacci, usando diversas técnicas.
"""


def fib(n: int) -> int:
    """
    Calcula el enésimo término de la sucesión de Fibonacci
    de forma recursiva.
    """
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    """
    Calcula el enésimo término de la sucesión de Fibonacci
    de forma iterativa.
    """
    return _fib_aux(n)


def _fib_aux(n: int) -> int:
    """
    Lleva a cabo las iteraciones necesarias para calcular
    la sucesión de Fibonacci de forma iterativa.
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


if __name__ == '__main__':
    _correcto = lambda n, v: '(correcto)' if n == v else '(incorrecto)'
    f7 = fib(7)
    f8 = fib(8)
    fit8 = fib_iter(8)
    print('fib(7) vale', f7, _correcto(f7, 13))
    print('fib(8) vale', f8, _correcto(f8, 21))
    print('fib_iter(8) vale', fit8, _correcto(fit8, 21))
