#!/usr/bin/python3

def fact(n):
    """Return factorial."""
    r = 1
    while n > 0:
        r = r * n
        n = n -1
    return r

print(fact(4))

print(fact.__doc__)
