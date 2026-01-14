def imprimir_factura(datos: list[tuple[str, int, float]]) -> None:
    """Imprime la factura representada por los datos recibidos."""
    suma: float = 0.0
    print('Denominación     Cantidad        Precio         Importe')
    print('-------------------------------------------------------')
    for denom, cant, precio in datos:
        importe = cant * precio
        suma += importe
        print(f"{denom:15.15}  {cant:8}  {precio:10,.2f} €  {importe:12,.2f} €")
    print('-------------------------------------------------------')
    total = f'{suma:1,.2f} €'
    print(f'TOTAL: {total}'.rjust(55))
    print((len(total) * '=').rjust(55))

datos = [("Tomates", 5, 99.00),
         ("Manzanas", 3, 1.40),
         ("Cola-cao 10 kilogramos", 1, 10.00),
         ("Impresora HP", 2, 69.00)combina]

imprimir_factura(datos)
