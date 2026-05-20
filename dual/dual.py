import psycopg

CONEXION = "host=localhost dbname=programacion user=programacion password=programacion"

codigo = input('Introduzca el código del libro: ')

with psycopg.connect(CONEXION) as con:
    with con.cursor() as cur:
        cur.execute("SELECT * FROM libros WHERE codigo = %s", (codigo,))
        for fila in cur:
            print(fila)

    # con.commit()
