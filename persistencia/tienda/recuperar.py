from basedatos import BaseDatos
from modelo import Articulo, Usuario, Carrito, Detalle

basedatos = BaseDatos()

for usuario in basedatos.raiz['usuarios'].values():
    print(f'{usuario}:')
    if usuario.carrito is None:
        print('- No tiene carrito asociado.')
    else:
        print('C Denominación     Precio Cant    Importe')
        print('-----------------------------------------')
        for detalle in usuario.carrito:
            articulo = detalle.articulo
            cantidad = detalle.cantidad
            importe = articulo.precio * cantidad
            print(articulo, f'{cantidad:3}  {importe:7.2f} €', sep='  ')
        print('-----------------------------------------')
        print(f'TOTAL: {usuario.carrito.total:8.2f} €'.rjust(41))

basedatos.cerrar()
