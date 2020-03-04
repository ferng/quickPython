#!/usr/bin/python3

x = "{0} is the {1} of {2}".format("Ambrosia", "food", "the gods")
print(x)

y = "{food} is the {what} of {who}".format(food="Ambrosia", what="food", who="the gods")
print(y)

print("{0:10} is the food of".format("Ambrosia"))
print("{0:{1}} is the food of".format("Ambrosia", 12))
print("{food:{width}} is the food of".format(food = "Ambrosia", width = 12))
print("{0:>10} is the food of".format("Ambrosia"))
print("{0:=>10} is the food of".format("Ambrosia"))

print("%s in the %s" % ("hat", "cat"))

num_dic = {'e': 2.718, 'pi': 3.14159 }
print("%(pi).2f - %(pi).4f - %(e).2f"% num_dic)

print("a", "b", "c")
print("a", "b", "c", end="\n\n\n")
print("a", "b", "c", sep="|")
