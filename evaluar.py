from operator import add, sub, mul, truediv, pow
sub(add(mul(-4, 7), truediv(pow(2, 3), 4)), 5)
-4 * 7 + 2 ** 3 / 4 -5

(año % 4 == 0) and ((año % 100 != 0) or ((año % 100 == 0) and (año % 400 != 0)))
(año % 4 == 0) and ((año % 100 != 0) or (not (año % 100 != 0) and (año % 400 != 0)))
A                        B                           B                    C

A and (B or ((not B) and C))
A and (B or C)

(año % 4 == 0) and ((año % 100 != 0) or (año % 400 != 0))

(año % 4 == 0) and not ((año % 100 == 0) and (año % 400 == 0))



'Menor' if edad < 18 else 'Adulto'    

edad = 15

'benjamín' if edad < 8  else \
'alevín'   if edad < 12 else \
'juvenil'  if edad < 18 else \
'adulto'



