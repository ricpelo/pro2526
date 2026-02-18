"""
El módulo principal del videojuego Vampiro.
"""

import entrada
import interprete
import mapeado as m

lugar_actual: m.Lugar = m.vestibulo

m.describir(lugar_actual)
entrada.pedir_entrada()
interprete.interpretar()

# Realizar las acciones relacionadas con el verbo y el nombre indicados
