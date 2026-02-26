
class Pareja:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
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
        
    def numer(self):
        return self.pareja.select(0)
    
    def denom(self):
        return self.pareja.select(1)
    
    
rac = Racional(3, 4)
print(rac.numer(), rac.denom())
