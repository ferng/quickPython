#!/usr/bin/python3
l = [1, 2, 3]
print(l)
print(repr(l))
print(str(l))

compound = [1]
compound.append(2)
compound.append([3, 4])
# print("string" +compound)
print("string" + repr(compound))
print("string" + str(compound))

print(repr(len))
print(str(len))
