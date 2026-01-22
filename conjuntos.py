def elimina_repetidos(emails: list[str]) -> list[str]:
    """Elimina cadenas repetidas."""
    return list(set(emails))


def elimina_repetidos_ordenados(emails: list[str]) -> list[str]:
    """Elimina cadenas repetidas conservando el orden."""
    res: list[str] = []
    for e in emails:
        if e not in res:
            res.append(e)
    return res


direcciones = [
    "ana@mail.com", "juan@mail.com", "ana@mail.com",
    "luis@mail.com", "juan@mail.com"
]

print(elimina_repetidos(direcciones))
print(elimina_repetidos_ordenados(direcciones))

a = {"ana", "juan", "luis"}       # usuarios que han iniciado sesión en A
b = {"juan", "luis", "carmen"}    # usuarios que han iniciado sesión en B
c = {"luis", "ana"}               # usuarios que han iniciado sesión en C

todos = a & b & c                 # usuarios activos en todos los sistemas
al_menos_uno = a | b | c          # usuarios activos en al menos uno
solo_en_a = a - b - c             # usuarios activos solo en A
solo_en_b = b - a - c             # usuarios activos solo en B
print(todos)
print(al_menos_uno)
print(solo_en_a)
print(solo_en_b)

t1 = "Programar en Python es divertido y educativo"
t2 = "Programar en Python es educativo y muy divertido"

def detectar_plagio(t1: str, t2: str) -> bool:
    """
    Dos textos tienen sospecha de plagio si comparten
    más del 70% del total de palabras de ambos
    (ignorando mayúsculas y minúsculas).
    """
    s1: set[str] = set(t1.lower().split())
    s2: str[str] = set(t2.lower().split())
    total = len(s1 | s2)
    en_comun = len(s1 & s2)
    # (en_comun / total) * 100.0 > 70.0
    return en_comun > 0.7 * total


print(detectar_plagio(t1, t2))


fila = [9, 2, 7, 1, 5, 4, 3, 6, 8, 9]


def comprobar_fila_sudoku(fila: list[int]) -> bool:
    """Comprueba si es una fila válida en el Sudoku."""
    return len(fila) == 9 and set(fila) == set(range(1, 10))
    
    
print(comprobar_fila_sudoku(fila))


password = "abc9x"

def comprobar_password(password: str) -> bool:
    """
    Comprobar si es una contraseña válida:
    - al menos una vocal
    - al menos un dígito
    """
    vocales = set("aeiou")
    digitos = set("0123456789")       # set(range(10))
    letras = set(password)
    
    return len(letras & vocales) > 0 and len(letras & digitos) > 0


print(comprobar_password(password))
