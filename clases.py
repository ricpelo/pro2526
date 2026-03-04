
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

    def select(self, i: int):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise ValueError('La i sólo puede ser 0 ó 1')


class Racional:
    def __init__(self, num: int, den: int) -> None:
        self.pareja = Pareja(num, den)
        
    def __eq__(self, otro):
        if type(self) != type(otro):
            return NotImplemented
        return self.numer() == otro.numer() and self.denom() == otro.denom()
    
    def __hash__(self):
        return hash((self.numer(), self.denom()))
    
    def numer(self):
        return self.pareja.select(0)
    
    def denom(self):
        return self.pareja.select(1)
    
    
class Deposito:
    def __init__(self, fondos):
        self.fondos = fondos
        
    def ingresar(self, cantidad):
        self.fondos += cantidad
        
    def retirar(self, cantidad):
        if cantidad > self.fondos:
            raise ValueError('Fondos insuficientes.')
        self.fondos -= cantidad
        
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
