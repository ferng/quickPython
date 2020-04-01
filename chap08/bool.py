#!/usr/bin/python3

x = 5
y = 15

print(x > 0 and x < 10)
print(0 < x < 10)
print(0 < y < 10)

print([] and 5)
print([] or 5 and {})


x = [0]
y = [x, 1]
print(x is y[0])

x = [0]
print(x is y[0])

print(x == y[0])

