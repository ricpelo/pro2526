
def fact(n: int) -> int:
    def fi(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return fi(n - 1, acc * n)

    return fi(n, 1)

print(fact(4))