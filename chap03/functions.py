#!/usr/bin/python3

def funct1(x, y, z):
    value = x + 2*y + z**2
    if value > 0:
        return x + 2*y + z**2
    else:
        return 0

u, v = 3, 4
o = funct1(u, v, 2)
print(o)
p = funct1(u, z=v, y=2)
print(p)


def funct4(x, y=1, z=1, **dictionary):
    print(x, y, z, dictionary)

funct4(1, 2, m=5, n=9, z=3)
