#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Tuples are immutable like string. Tuples are very similar to Lists excepts it's immutable 
# and cannot modify values whatsoever. All the index operations can be applied to tuplese as 
# in strings and lists. 
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[0])
print(t[2:])
print(t[::-1])
print(t[2:9])
print(t[2:9:2])
print(t[-1])

# Tuple functions.
t = ('a', 'a', 'b', 'c', 'b', 'a')
print(t.count('a'))     # Get the count of occurrences of the parameter value.
print(t.index('b'))     # Get the index value of first occurrence of parameter value.

# What makes the tuple is tuple and differ from lists? Tuple is immutable and keep the 
# data integrity throughout the progam therefore. 
