"""
125. Dado el documento XML del ejercicio anterior, escribir un
programa que elimine al socio cuyo id sea 51 y guarde los
cambios en el mismo archivo.
"""

import xml.etree.ElementTree as ET
arbol = ET.parse('club.xml')
raiz = arbol.getroot()

socios = raiz.find("socios")
socio = raiz.find("socios/socio[@id='51']")
socios.remove(socio)
ET.dump(raiz)