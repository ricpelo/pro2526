alumnos = ('Manuel', 'Ana', 'Enrique', 'María', 'Jesús', 'Rosa')

hombres = lambda t: t[::2]
mujeres = lambda t: t[1::2]

longitud_es_par = lambda t: len(t) % 2 == 0

hombres_al_reves = lambda t: hombres(t)[::-1]
hombres_al_reves = lambda t: t[-2::-2] if longitud_es_par(t) else \
                             t[-1::-2]

mujeres_al_reves = lambda t: mujeres(t)[::-1]
mujeres_al_reves = lambda t: t[-1::-2] if longitud_es_par(t) else \
                             t[-2::-2]

longitud_es_impar = lambda t: not longitud_es_par(t)

print(hombres(alumnos))

