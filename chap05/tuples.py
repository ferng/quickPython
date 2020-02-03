#!/usr/bin/python3

x = ('a', 'b', 'c')
print(x[2])
print(x[1:])
print(len(x))
print(max(x))
print(5 in x)
print(2 * x)


print((5+7))

print((5+7,))

print (())


(one, two, three, four) = (1, 2, 3, 4)
print(one)
print(two)

five, six, seven = 5, 6, 7
print(five)
print(seven)

y = 8, 9, 10
print(y)

m, n = 44, 45
print (m, n)
m, n = n, m
print (m, n)

x = (1, 2, 3, 4)
a, b, *c = x
print(a)
print(b)
print(c)
print(a, b, c)
print((a, b, c))


print(list((1, 2, 3, 4)))
print(tuple([1, 2, 3, 4]))
print(list("Hello"))
