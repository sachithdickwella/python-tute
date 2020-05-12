#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

d = {'k1': 1, 'k2': 2}

# Dictionary comprehension.
d1 = {x:x ** 2 for x in range(10)}
print(d1)

d1 = {val:idx ** 2 for idx, val in enumerate(['a', 'b', 'c', 'd'])}
print(d1)

d1 = {k:v ** 2 for k, v in zip(['a', 'b', 'c', 'd'], range(4))}
print(d1)
