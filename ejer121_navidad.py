"""
121. Escribir un programa que muestre los socios del club de forma
similar a la siguiente:
[1] Sherlock Holmes
[51] Winston Churchill
"""

import xml.etree.ElementTree as ET
arbol: ET.ElementTree = ET.parse('club.xml')
raiz: ET.Element = arbol.getroot()

for socio in raiz.iterfind('socios/socio'):
    socio_id = socio.get('id')
    socio_nombre = socio.find('nombre').text
    print(f'[{socio_id}] {socio_nombre}')
