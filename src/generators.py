#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# #################################################################################################
# Generators using 'yield' keyword.
# #################################################################################################

def create_cubes(n):
    for x in range(n):
        yield x ** 3


cubes = create_cubes(10)
print(cubes)
print(list(cubes))


def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(10)))

# #################################################################################################
# The next() and iter() function
# #################################################################################################

def simple_gen(n):
    for x in range(n):
        yield x

g = simple_gen(3)

print(g)        # Generator object.
print(next(g))  # Get the next value from the generator though yield until the end.
print(next(g))
print(next(g))
# print(next(g)) 'StopIteration' exception hence last element yielded in precedeing statement.
  
hello = 'Hello, World'

# print(next(hello)) 'TypeError' string is not iterable even though string can directly 
# iterate with 'for' loops. Therefore, should make it iterable before use on 'next()' function.

iterable = iter(hello)
print(iterable)
print(next(iterable))
print(next(iterable))
print(next(iterable))

# #################################################################################################
# Use LIST COMPREHENSION to create GENERATOR.
# #################################################################################################

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 1
generator = (item for item in my_list)  # Use brackets instad of square brackets. This is not a tuple.
print(generator)

for x in generator:
    print(x)

# Example 2
generator = (item for item in my_list if item % 2 == 0)
print(generator)

for x in generator:
    print(x)

# Example 3
generator = (item if item % 2 == 0 else "ODD" for item in my_list)
print(generator)

for x in generator:
    print(x)
    