from cliente import Cliente
from articulo import Articulo
from typing import Iterator

class Factura:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self.__set_numero(numero)
        self.__set_cliente(cliente)
        self.__lineas: dict[Articulo, int] = {}
    
    def __iter__(self) -> Iterator[tuple[Articulo, int]]:
        return iter(self.__lineas.items())
    
    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
    
    def __set_numero(self, numero):
        self.__numero = numero
        
    def __set_cliente(self, cliente: Cliente):
        self.__cliente = cliente
        
    def anyadir_linea(self, articulo: Articulo, cantidad: int) -> None:
        self.__lineas[articulo] = cantidad
        
    def eliminar_linea(self, articulo: Articulo) -> None:
        del self.__lineas[articulo]
        
    @property
    def total(self) -> float:
        return sum(articulo.precio * cantidad \
                   for articulo, cantidad in self.__lineas.items())

    def imprimir(self) -> None:
        print(f'Número: {self.numero}')
        print()
        cli = self.cliente
        print(f'DNI: {cli.dni}')
        print(f'{cli.nombre} {cli.apellidos}')
        print()

        print('Cód Denominación         Can   Precio  Importe')
        print('----------------------------------------------')

        for articulo, can in self:
            cod = articulo.codigo
            den = articulo.denominacion
            pre = articulo.precio
            imp = articulo.precio * can
            print(f'{cod} {den:20} {can:3} {pre:.2f} € {imp:.2f} €')
            
        print('----------------------------------------------')
        total = f'TOTAL: {self.total:.2f} €'
        print(f'{total:>46}')

