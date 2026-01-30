import xml.etree.ElementTree as ET
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

cont = 0
for e in raiz.iter('alumno'):
    cont += 1

cont = sum(1 for e in raiz.iter('alumno'))

print(cont)
