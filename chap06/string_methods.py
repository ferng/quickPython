#!/usr/bin/python3

import string

x = "Hello"
print(x.upper())

print("=".join(["hello", "how", "are", "you", "today"]))

y="This\t\t string has a whole\nbunch of whitespace"
print(y.split())
print(y.split("e"))

z="a b c d e "
print(z.split(' ', 1))
print(z.split(None, 2))

print (float('123.456'))
# print (float('ff'))

print(int('1234'))
# print(int('1234.432'))

print(int('10000', 8))
print(int('101', 2))
print(int('ff', 16))
print(int('12345', 6))
print(int('fg', 17))

white = "  Hello,    World\t\t "
print("[" + white + "]")
print("[" + white.strip() + "]")
print("[" + white.lstrip()+ "]")
print("[" + white.rstrip()+ "]")

he = "hello"
print("[" + he.strip('h')+ "]")
print("[" + he.strip('o')+ "]")
print("[" + he.strip('ho')+ "]")

river = "Mississippi"
print(river.find("ss"))
print(river.find("zz"))
print(river.find("ss", 3))
print(river.find("ss", 0, 3))
print(river.rfind("ss"))

print(river.index("ss"))
# print(river.index("zz"))

print(river.count("ss"))
print(river.count("i"))

print(river.startswith("Miss"))
print(river.startswith("Misg"))
print(river.endswith("pi"))
print(river.endswith("ri"))
print(river.endswith(("pi", "oi")))

print(river.replace("ss", "xxx"))

code = "~x ^ (y % z)"
table = "".maketrans("~^()", "!&[]")
print(code.translate(table))

table = "".maketrans("~^()", "!&[]", "%")
print(code.translate(table))

table = "".maketrans("~^()", "!&[]", "~z")
print(code.translate(table))

tx1 = "once upon A time there Was a teddy bear"
print(tx1.upper())
print(tx1.lower())
print(tx1.capitalize())
print(tx1.title())
print(tx1.swapcase())

text = "Hello, World"
wordList = list(text)
wordList[6:] = []
wordList.reverse()
text = "".join(wordList)
print(text)


print("123".isdigit())
print("123".isalpha())
print("M".islower())
print("M".isupper())

print(string.whitespace)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
