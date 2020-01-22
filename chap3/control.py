#!/usr/bin/python3

x = 5
if x < 5:
    print("less")
elif x > 5:
    print("more")
else:
    print("just right")


u, v, x, y = 0, 0, 100, 30
while x > y:
    u = u + y
    x = x - y
    if x < y + 2:
        v = v + x
        x = 0
    else:
        v = v + y + 2
        x = x - y - 2
print(u, v)



item_list= [3, "string", 23, 14.0, "string2", 49, 64, 70]
for x2 in item_list:
    if not isinstance(x2, int):
        continue
    if not x2 % 7:
        print("found an integer divisible by seven: %d" % x2)
        break
