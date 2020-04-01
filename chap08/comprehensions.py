#!/usr/bin/python3

x = [1, 2, 3, 4]
x_sq = []

for item in x:
    x_sq.append(item * item)

print(x_sq)

x_sq_comp = [item * item for item in x]
print(x_sq_comp)

x_sq_comp_filter = [item * item for item in x if item > 2]
print(x_sq_comp_filter)


x_sq_comp_dict = {item: item * item for item in x}
print(x_sq_comp_dict)
