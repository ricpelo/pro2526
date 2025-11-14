a = 76
b = 44
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
mcd = b
