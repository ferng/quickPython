#!/usr/bin/python3

x = [1.0, 2.0, 3.0]
for n in x:
    print(1 / n)

y = [1, 3, -7, 4, 9, -5, 4]
for i in range(len(y)):
    if y[i] < 0:
        print("Found negative at index ", i)



for i in range(10):
    print(i)
print("---")

for i in range(3, 7):
    print(i)
print("---")

for i in range(7, 3, -1):
    print(i)
print("---")

for i in range(0, 12, 2):
    print(i)
print("---")



t = [(1, 2), (3, 4), (5, 6)]
result = 0
for val in t:
    result = result + (val[0] * val[1])
print(result)

result = 0
for x, y in t:
    result = result + (x * y)
print(result)
print("---")



y = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(y):
    if n < 0:
        print("Negative at ", i)
print("---")

x = [1, 2, 3, 4]
y = ['a', 'b', 'c']
z = zip(x, y)
print(list(z))
print("---")
