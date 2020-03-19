#!/usr/bin/python3

matrix = {(0, 0): 3, (0, 2): -2, (0, 3):11,
        (1, 1): 9, (2, 1): 7, (3, 3): -5}

if (0, 0) in matrix:
    print(matrix[(0, 0)])
else:
    print('no')

if (0, 1) in matrix:
    print(matrix[(0, 1)])
else:
    print('no')

print(matrix.get((0, 0), 'no'))
print(matrix.get((0, 1), 'no'))
