#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import timeit

# Measure the execution time of each statement.

tt = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tt)

tt = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tt)

tt = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tt)

# https://docs.python.org/2/library/timeit.html
