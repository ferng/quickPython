#!/usr/bin/python3

import obj
c1 = obj.Circle()
c2 = obj.Circle(5, 15, 20)
print(c1)
print(c2)
c2_area = c2.area()
print(c2_area)
c2.move(5,6)
print(c2)
