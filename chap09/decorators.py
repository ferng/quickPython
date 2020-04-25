#!/usr/bin/python3

def decorate(func):
    print("in decorate function, decorating", func.__name__)
    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)
    return wrapper_func

def mydecorate(func):
    print("in decorate function, decorating", func.__name__)
    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)
    return wrapper_func

def myfunction(param):
    print(param)

myfunction = decorate(myfunction)

myfunction("hello")


@decorate
def myfunction2(parameter):
    print(parameter)

myfunction2("hello")

@mydecorate
def myfunction3(parameter):
    print(parameter)

myfunction3("hello")
