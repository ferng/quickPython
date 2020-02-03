#!/usr/bin/python3

def compare_num_of_chars(string1):
    return len(string1)

word_list = ['Python', 'is', 'better', 'than', 'java']
word_list.sort()
print(word_list)

word_list = ['Python', 'is', 'better', 'than', 'java']
word_list.sort(key=compare_num_of_chars)
print(word_list)

word_list = ['Python', 'is', 'better', 'than', 'java']
word_list.sort(reverse=True)
print(word_list)

x = (4, 3, 1, 2)
y = sorted(x)
print(y)
