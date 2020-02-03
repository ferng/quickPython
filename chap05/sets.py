#!/usr/bin/python3

x = set([1, 2, 3, 1, 3, 5, 4, 5])
print(x)

x.add(6)
print(x)

x.remove(5)
print(x)

print(1 in x)

y = set([1, 7, 5, 8, 9])
print(x)
print(y)
print(x|y)
print(x&y)
print(x^y)



m = set([1, 2, 3, 4, 5, 6])
n = frozenset(x)
print(m)
m.add(n)
print(m)
print(n)

