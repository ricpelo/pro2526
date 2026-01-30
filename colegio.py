import xml.etree.ElementTree as ET

def agrupar(arbol: ET.ElementTree) -> ET.ElementTree:
    raiz: ET.Element = arbol.getroot()
    alumnos: ET.Element = raiz.find('alumnos')
    grupos: ET.Element = ET.SubElement(raiz, 'grupos')
    
    for alumno in raiz.findall('alumnos/alumno'):
        edad = alumno.get('edad')
        nivel = str(int(edad) - 5)
        grupo = raiz.find(f"grupos/grupo[@nivel='{nivel}']")
        if grupo is None:
            grupo = ET.SubElement(grupos, 'grupo')
            grupo.set('nivel', nivel)
        alumnos.remove(alumno)
        grupo.append(alumno)
    raiz.remove(alumnos)
    return arbol  
    
arbol = ET.parse('colegio.xml')
nuevo_arbol = agrupar(arbol)
ET.dump(nuevo_arbol)


def adn_a_arn(adn: str) -> str:
    trad = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(trad[c] for c in adn)
    return adn.translate(str.maketrans(trad))
