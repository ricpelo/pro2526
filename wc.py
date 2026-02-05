#!/usr/bin/env python

"""
Simulación del comando wc de Unix, que cuenta líneas, palabras y caracteres en
un archivo de texto.
"""

import sys

opcion: str = ''

match sys.argv:
    case [programa, archivo]:
        pass
    case [programa, opcion, archivo]:    
        if opcion not in ('-l', '-m', '-w'):
            print(f"{programa}: opción incorrecta -- '{opcion}'")
            sys.exit(1)
    case _:
        print("""
        Uso: {programa} [-l|-m|-w] <archivo>
        """)
        sys.exit(1)

lineas: int     = 0
palabras: int   = 0
caracteres: int = 0

try:
    with open(archivo, 'r') as f:
        for linea in f:
            lineas += 1
            palabras += len(linea.split())
            caracteres += len(linea)
    d = {'-l': lineas, '-w': palabras, '-m': caracteres}
    contadores = d.get(opcion, f'{lineas} {palabras} {caracteres}')
    print(f' {contadores} {archivo}')
except FileNotFoundError:
    print(f'{programa}: {archivo}: No existe el fichero o el directorio')
    sys.exit(2)
