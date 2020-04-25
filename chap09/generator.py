#!/usr/bin/python3

def four():
    x = 0
    while x < 4:
        print("in generator, x=", x)
        yield x
        x += 1

for i in four():
    print(i)


print(2 in four())

print(5 in four())
