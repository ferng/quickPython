#!/usr/bin/python3

def fact(local_n):
    local_r = 1
    while local_n > 0:
        local_r = local_r * local_n
        local_n = local_n - 1
    return local_r

print(fact(4))



def fun():
    global a
    a = 1
    b = 2

a = "one"
b = "two"
print("{0},{1}".format(a, b))

fun()
print("{0},{1}".format(a, b))




global_var = 0
non_local_var = 0
print("top level -> global: {0}, non_local: {1}".format(global_var, non_local_var))

def test():
    non_local_var = 2
    print("in test -> global: {0}, non_local: {1}".format(global_var, non_local_var))
    def inner_test():
        global global_var
        nonlocal non_local_var
        global_var = 1
        non_local_var = 4
        print("in inner test -> global: {0}, non_local: {1}".format(global_var, non_local_var))

    inner_test()
    print("in test -> global: {0}, non_local: {1}".format(global_var, non_local_var))

test()
print("top level -> global: {0}, non_local: {1}".format(global_var, non_local_var))
