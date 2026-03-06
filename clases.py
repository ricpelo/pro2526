from math import gcd


class Pareja:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.select(0) == otro.select(0) and \
               self.select(1) == otro.select(1)
        # return self.x == otro.x and self.y == otro.y
        # return (self.x, self.y) == (otro.x, otro.y)

    def __hash__(self):
        return hash((self.select(0), self.select(1)))

    def __repr__(self):
        return f'Pareja({self.select(0)!r}, {self.select(1)!r})'

    def __str__(self):
        return f'<{self.select(0)}, {self.select(1)}>'

    def select(self, i: int):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise ValueError('La i sólo puede ser 0 ó 1')


class Racional:
    def __init__(self, num: int, den: int) -> None:
        mcd = gcd(num, den)
        self.pareja = Pareja(num // mcd, den // mcd)
        
    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numer() == otro.numer() and self.denom() == otro.denom()
    
    def __hash__(self):
        return hash((self.numer(), self.denom()))
    
    def __repr__(self):
        return f'Racional({self.numer()!r}, {self.denom()!r})'
    
    def __str__(self):
        return f'{self.numer()}/{self.denom()}'
        
    def numer(self):
        return self.pareja.select(0)
    
    def denom(self):
        return self.pareja.select(1)
    
    
class Deposito:
    def __init__(self, fondos, movimientos = None):
        self.fondos = fondos
        if movimientos is None:
            self.movimientos: list[tuple[str, float]] = [('APERTURA', fondos)]
        else:
            self.movimientos = movimientos
    
    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.movimientos == otro.movimientos
    
    def __repr__(self) -> str:
        return f'Deposito({self.saldo()!r}, {self.movimientos!r})'
    
    def __str__(self):
        mov = len(self.movimientos)
        sal = self.saldo()
        return f'Esta cuenta tiene {mov} movimientos y un saldo de {sal:.2f} €.'
    
    def ingresar(self, cantidad):
        self.fondos += cantidad
        self.movimientos.append(('INGRESO', cantidad))
        
    def retirar(self, cantidad):
        if cantidad > self.fondos:
            raise ValueError('Fondos insuficientes.')
        self.fondos -= cantidad
        self.movimientos.append(('REINTEGRO', -cantidad))
        
    def saldo(self):
        return self.fondos


class Lugar:
    def __init__(self, corta: str, larga: str):
        self.corta = corta
        self.larga = larga
        
pasillo = Lugar('PASILLO', 'Estás en el pasillo del castillo...')
cocina = Lugar('COCINA', 'Estás en la cocina que tiene cacharros...')

class TipoPalabra:
    def __init__(self, tipo: str):
        self.tipo = tipo
        
T_VERBO = TipoPalabra('VERBO')
T_NOMBRE = TipoPalabra('NOMBRE')

class TipoToken:
    def __init__(self, token: str, tipo):
        self.token = token
        self.tipo = tipo
        
T_COGER = TipoToken('COGER', T_VERBO)
T_DEJAR = TipoToken('DEJAR', T_VERBO)

class Palabra:
    def __init__(self, lexema: str, token: TipoToken):
        self.lexema = lexema
        self.token = token
        
COGER = Palabra('COGER', T_COGER)
TOMAR = Palabra('TOMAR', T_COGER)
AGARRAR = Palabra('AGARRAR', T_COGER)
DEJAR = Palabra('DEJAR', T_DEJAR)
