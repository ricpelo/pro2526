"""
122. Dado el documento XML del ejercicio anterior, escribir un
programa que cuente cuántos socios tiene el club y lo muestre por
pantalla.
"""

import xml.etree.ElementTree as ET
arbol: ET.ElementTree = ET.parse('club.xml')
raiz: ET.Element = arbol.getroot()

print(len(raiz.find('socios')))
