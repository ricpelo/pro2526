"""
Ejercicio 1 de Programación funcional.

Los médicos forenses utilizan la longitud de los huesos para determinar
la altura de una persona, cuando la persona estaba viva.

Por ejemplo, para los varones:
altura (en cm) = 69.089 + 2.232 × longitud de la tibia

Para las mujeres, el valor es el siguiente:
altura (en cm) = 61.412 + 2.317 × longitud de la tibia

A partir de los 30 años (inclusive), la altura de una persona decrece a una
tasa de 0.06 cm por año.

Escribir un programa que, dados los valores de la longitud de la tibia,
el sexo y la edad del paciente, nos calcule la altura aproximada.
"""

# Datos de entrada:
longitud_tibia: float = 38.0
sexo: str = 'M'                # 'V' = Varón, 'M' = Mujer
edad: int = 50

# Datos intermedios:
altura_varon: float = 69.089 + 2.232 * longitud_tibia
altura_mujer: float = 61.412 + 2.317 * longitud_tibia

# Cálculo de la altura previa al decrecimiento por año:
altura_base: float = altura_varon if sexo == 'V' else altura_mujer

# Cálculo de la altura final:
altura: float = altura_base if edad < 30 else altura_base - 0.06 * (edad - 29)
