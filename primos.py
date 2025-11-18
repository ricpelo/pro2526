
def es_primo(n: int) -> bool:
    def divisores(n: int) -> list[int]:
        res = []
        i = 1
        while i <= n:
            if n % i == 0:
                res.append(i)
            i += 1
        return res

    return len(divisores(n)) == 2


print(es_primo(4))
