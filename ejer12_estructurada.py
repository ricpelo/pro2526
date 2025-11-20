"""
12. Escribir un programa que gestione datos almacenados en una lista, de forma que
muestre un menú con las siguientes opciones:

1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.

El programa deberá pedir la información necesaria para cada opción elegida por el
usuario.
"""

OPCIONES: str = """
1. Añadir un elemento a la lista.
2. Cambiar el valor de un elemento de la lista.
3. Eliminar un elemento de la lista.
4. Eliminar todos los elementos de la lista.
5. Mostrar los elementos de la lista.
0. Salir del programa.
"""


def imprimir_menu(opciones: str) -> None:
    print(opciones)


def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            opc: int = int(input(mensaje))
            return opc
        except ValueError:
            print('El valor introducido no es correcto.')


def pedir_opcion() -> int:
    return pedir_entero('Introduzca una opción: ')


def anyadir(lst: list[str]) -> None:
    valor = input('Introduzca un valor: ')
    lst.append(valor)
    

def pedir_posicion(lst: list) -> int:
    while True:
        i = pedir_entero('Introduzca la posición a cambiar (contando desde 0): ')
        if i >= 0 and i < len(lst):
            return i
        print('La posición debe ser válida')


def cambiar(lst: list[str]) -> None:
    if len(lst) == 0:
        print('No se puede cambiar una lista vacía.')
        return
    i = pedir_posicion(lst)
    nuevo = input('Introduzca el valor nuevo: ')
    lst[i] = nuevo


def mostrar(lst: list[str]) -> None:
    print(lst)


lista: list[str] = []

while True:
    imprimir_menu(OPCIONES)
    opc: int = pedir_opcion()

    if opc == 1:
        anyadir(lista)
    elif opc == 2:
        cambiar(lista)
    elif opc == 3:
        eliminar()
    elif opc == 4:
        eliminar_todos()
    elif opc == 5:
        mostrar(lista)
    else:
        break
