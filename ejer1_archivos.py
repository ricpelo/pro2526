"""
1. Crear el archivo de texto «numeros_reales.txt» en el directorio de trabajo actual
que contenga una sola línea de texto con números reales separados por espacios. A
continuación, escribir un programa que abre ese archivo, lea los números que contiene
y calcule la suma y la media aritmética, mostrando los resultados por pantalla.
"""

with open('numeros_reales.txt', 'r') as f:
    linea = f.readline()

lista = linea.split()
suma = 0.0

for n in lista:
    n = float(n)
    suma += n

media = suma / len(lista)

print(f'Suma: {suma}, media: {media}')

