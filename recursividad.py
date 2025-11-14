factorial = lambda n: 1 if n == 0 else \
                      n * factorial(n - 1)

potencia = lambda a, b: 1 if b == 0 else a * potencia(a, b - 1)

digitos = lambda n: 1 if n < 10 else 1 + digitos(n // 10)

suma_digitos = lambda n: n if n < 10 else (n % 10) + suma_digitos(n // 10)

longitud = lambda s: 0 if s == "" else 1 + longitud(s[1:])

fib = lambda n: 0 if n == 0 else \
                1 if n == 1 else \
                fib(n - 1) + fib(n - 2)

hanoi = lambda a, b, c, n: "" if n == 0 else \
                           hanoi(a, c, b, n - 1) + \
                           "muevo de " + str(a) + " hacia " + str(b) + " un disco; " + \
                           hanoi(c, b, a, n - 1)

max2 = lambda a, b: a if a >= b else b
mayor = lambda t: t[0] if len(t) == 1 else max2(t[0], mayor(t[1:]))

invertir = lambda s: "" if s == "" else invertir(s[1:]) + s[0]

inv_tupla = lambda t: () if t == () else inv_tupla(t[1:]) + (t[0],)

# palindromo = lambda s: s == invertir(s)

primero = lambda s: s[0]                                          # len(s) > 0
ultimo = lambda t: t[0] if len(t) == 1 else ultimo(t[1:])         # len(s) > 0
medio = lambda s: "" if len(s) == 2 else s[1:][0] + medio(s[1:])  # len(s) >= 2

palindromo = lambda s: True if len(s) <= 1 else \
                       palindromo(medio(s)) and primero(s) == ultimo(s)

enesimo = lambda n, t: t[0] if n == 0 else enesimo(n - 1, t[1:])
