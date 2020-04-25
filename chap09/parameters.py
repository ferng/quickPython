#!/usr/bin/python3

def positional_power(x, y):
    r = 1
    while y > 0:
        r = r * x
        y = y -1
    return r

print(positional_power(3, 4))
# print(positional_power(3))



def default_power(x, y = 3):
    r = 1
    while y > 0:
        r = r * x
        y = y -1
    return r

print(default_power(3, 4))
print(default_power(3))


print(default_power(x=4, y=5))
print(default_power(y=5, x=4))
print(default_power(y=4, x=5))



def use_default_and_named_as_builder(size=False, create_date=False, mod_date=False):
    #get file names
    if size:
        print("Getting size info")    
    if create_date:
        print("Getting create_date info")    
    if mod_date:
        print("Getting mod_date info")
    return 0

print(use_default_and_named_as_builder(size=True, mod_date=False))
print(use_default_and_named_as_builder(size=True, create_date=True))




def positional_indefinite_args_maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum

print(positional_indefinite_args_maximum(3, 2, 8))
print(positional_indefinite_args_maximum(1, 5, 9, -2, 2))




def by_keyword_indefinite_args(x, y, **other):
    print("x: {0}, y: {1}, keys in other: {2}".format(x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]

    print("The total of values in other is {0}".format(other_total))

by_keyword_indefinite_args(2, y="1", foo=3, bar=4, boing=77)




def mutables_are_changed_in_function(n, list1, list2):
    list1.append(3)
    list2 = [4, 5, 6]
    n = n + 1

x = 5
y = [1, 2]
z = [4, 5]
print("x: {0}, y: {1}, z:{2}".format(x, y, z))
mutables_are_changed_in_function(x, y, z)
print("x: {0}, y: {1}, z:{2}".format(x, y, z))



