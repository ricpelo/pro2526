"""
Escribir en Python una función shows() sin parámetros que cargue el archivo «shows.xml» y que
devuelva un diccionario donde:
Las claves serán los títulos de todas las películas y series (no los episodios) que tengan género
«Fantasía».

Los valores asociados a cada clave serán el número de episodios que tiene la serie (si es una
serie) o None si es una película.

Tests:
"Star Wars" in shows() == False
shows()['Cristal oscuro'] is None == True
shows()['Juego de tronos'] == 1
"""

import xml.etree.ElementTree as ET

def shows() -> dict[str, int | None]:
    arbol = ET.parse('shows.xml')
    raiz = arbol.getroot()
    res = {}
    
    for pelicula in raiz.iterfind('pelicula'):
        if pelicula.find('genero').text == 'Fantasía':
            res[pelicula.find('titulo').text] = None

    for serie in raiz.iterfind('serie'):
        if serie.find('genero').text == 'Fantasía':
            episodios = 0
            for episodio in serie.iterfind('temporada/episodio'):
                episodios += 1
            res[serie.find('titulo').text] = episodios
        
    return res

print(shows())

assert "Star Wars" not in shows()
assert shows()['Cristal oscuro'] is None
assert shows()['Juego de tronos'] == 1
    