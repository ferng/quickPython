#!/usr/bin/python3

import os

f = open("file", "w")
f.write("hello there\n")
f.write("how are you?\n")
f.close()

f = open("file", "r")
line1 = f.readline()
line2 = f.readline()
f.close()

print(line1, line2)

print(os.getcwd())
