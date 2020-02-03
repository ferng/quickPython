#!/usr/bin/python3

print("\n-----------------------\nlist membership\n-----------------------")
a = [1, 3, 4, 5]
print(3 in a)
print(3 not in a)

print("\n-----------------------\nlist concatenation\n-----------------------")
b = a + [9, 8, 7]
print(b)

print("\n-----------------------\nlist initialization (no memory realloc)\n-----------------------")
print([None] * 4)

print("\n-----------------------\nlist min max\n-----------------------")
print(min(b))
print(max(b))

print("\n-----------------------\nlist index\n-----------------------")
if(9 in b):
    print(b.index(9))

if(20 in b):
    print(b.index(20))
