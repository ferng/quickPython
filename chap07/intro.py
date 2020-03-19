#!/usr/bin/python3
y = {}
y[0] = 'Hello'
y[1] = 'Goodbye'
print(y)
print(y[0] + ' Friend')

y['two'] = 2
y['pi'] = 3.14159
print(y['two']+ y['pi'])

english_to_french = {'red': 'rouge', 'green': 'vert', 'blue': 'bleu'}
print(len(english_to_french))
print(english_to_french.keys())
print(list(english_to_french.keys()))
print(list(english_to_french.values()))
print(list(english_to_french.items()))
print('kak' in english_to_french)
print(english_to_french.get('red', 'WAH?'))
print(english_to_french.get('pink', 'WAH?'))
print(english_to_french.get('pink'))
print(english_to_french['red'])

# print(english_to_french['oi'])
print('oi' in english_to_french)
print(english_to_french.get('oi', 'default'))
print('oi' in english_to_french)
print(english_to_french.setdefault('oi', 'bah'))
print('oi' in english_to_french)
print(english_to_french.setdefault('oi', 'mah'))
print('oi' in english_to_french)


