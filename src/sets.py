#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Unordered collections with unique elements.
my_set = set()      # Initialize with iterable object like list or tuple.

# 'Set' operations.
my_set.add(1)
my_set.add(2)
print(my_set)

my_set.add(1)       # Adding 1 again to be duplicate. This throws no error nither add.
print(my_set)

l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
my_set = set(l)
print(my_set)

str_set = set('Mississippi')    # Unique values only.
print(str_set)
