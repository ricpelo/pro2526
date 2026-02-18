"""
El mapeado del juego.
"""

Lugar = tuple[str, str]

vestibulo: Lugar = (
    'VESTÍBULO',
    'Estás en el vestíbulo del castillo. El ambiente es muy húmedo y frío. Un pasillo se extiende hacia el norte. Al sur queda la puerta de entrada al castillo.'
)

pasillo: Lugar = (
    'PASILLO',
    'Te encuentras en medio del pasillo principal de este piso. Al oeste está la cocina y al este la biblioteca. El pasillo sigue hacia el norte.'
)


def describir(l: Lugar) -> None:
    """Describe un lugar."""
    print(l[0])
    print(l[1])
