#!/usr/bin/python3
import copy

print('\n-----------------\nnested lists\n---------------')
m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
print(m[0])

print(m[0][1])


nested = [0]
original = [nested, 1]
print(original)

nested[0] = 'zero'
print(original)

original[0][0] = 0
print(nested)
print(original)

nested = [2]
print(original)



print('\n-----------------\nshallow and deep copies\n---------------')
original2 =[[0], 1]
shallow2 = original2[:]
deep2 = copy.deepcopy(original2)

print(shallow2)
shallow2[1] = 2
print(shallow2)
print(original2)
shallow2[0][0] = 'zero'
print(original2)

deep2[0][0] = 5
print(deep2)
print(original2)
