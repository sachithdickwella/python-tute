#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# #####################################
# 'map' function
# #####################################
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]

my_map = map(square, numbers)
print(my_map)

for item in my_map:
    print(item)

# OR 

my_map = map(square, numbers)       # Reassign the map here hence, with the first iteration, 
                                    # 'my_map' cleared up.
print(list(my_map))

# 'map' with strings

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

# #####################################
# 'filter' function
# #####################################

def check_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4 , 5, 6, 7, 8, 9, 10]

filtered = filter(check_even, numbers)
print(filtered)
print(list(filtered))

# #####################################
# Lambda expressions - step by step
# #####################################
def square1(num):
    return num ** 2
print(square1(2))

# Equivalent to above function declaration

def square2(num): return num ** 2
print(square2(2))

# enforce with lambda expression

square = lambda num: num ** 2
print(square(2))

# #####################################
# Lambda - Where it shines
# #####################################
print(list(map(lambda num: num ** 2, numbers)))
print(list(filter(lambda num: num % 2 == 0, numbers)))

# EXTRA LAMBDA with if-else
func = lambda num: 'EVEN' if num % 2 == 0 else 'ODD'
print(func(10))
