#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'range()' function.
my_list = [1, 2, 3]
for num in range(0, 10):
    print(num)

for num in range(1, 10, 2):
    print(num)

print(range(0, 10, 2))
print(list(range(0, 10, 2)))        # 'range()' is a generator.

list_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(list_count, letter))
    list_count += 1

# 'enumerate()' function.
for item in enumerate('abcde'):
    print(item) # 'item' is a tuple with (index, value)

for index, letter in enumerate('abcde'):    # With tuple unpacking.
    print(index)
    print(letter)
    print("\n")

# 'zip()' function.
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1, my_list2):
    print(item)

# Zip 2 or more lists together as a tuple list. Zipped content would be 
# as long as its shotest lists.
print(list(zip(my_list1, my_list2)))            # Tuple list print here.

my_list1 = [1, 2, 3, 4, 5]
my_list3 = [100, 200, 300]

print(list(zip(my_list1, my_list2, my_list3)))  # Tuple list only would 
                                                # have 3 elements hence 
                                                # it's the shortest size.

for a, b, c in zip(my_list1, my_list2, my_list3):   # Tuple unpacking.
    print("a: {}, b: {}, c: {}".format(a, b, c))

# Boolean operation to see contains.
print(1 in my_list1)
print('a' in my_list2)
print(10 in my_list3)

# With strings.
print('a' in 'a world')
print('world' in 'Hello World')         # String case sensitive.
print('World' in 'Hello World')

# With dictionaries, only with keys by default.
my_dict = {"k1": 10, "k2": 20, "k3": 30}
print('k1' in my_dict)
print('k4' in my_dict)

print(20 in my_dict.values())
print('k3' in my_dict.keys())
print(('k1', 10) in my_dict.items())    # Entire tuple match.

# Mathematical functions - Basics.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(min(my_list))
print(max(my_list))

# Random library.
from random import shuffle

shuffle(my_list)
print(my_list)          # Shuffle/scramble the list itself.

from random import randint

print(randint(0, 100))  # Random number in between 0 and 100.

# Accept user inputs.
name = input('What is your name? ')
print(name)
