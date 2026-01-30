"""
126. Dado el documento XML del ejercicio anterior, escribir
un programa que añada el teléfono del socio cuyo id sea 1
creándole al socio un nodo hijo que sea
<telefono>666555444</telefono> y guarde los cambios en el
mismo archivo.
"""

import xml.etree.ElementTree as ET
arbol = ET.parse('club.xml')
raiz = arbol.getroot()

socio = raiz.find("socios/socio[@id='1']")
telefono = ET.SubElement(socio, 'telefono')
telefono.text = '666555444'

ET.dump(raiz)
