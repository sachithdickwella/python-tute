#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime

# Time
t = datetime.time(5, 25, 5, 200)
print(t)

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

# Date
today = datetime.date.today()
print(today)
print(today.timetuple())
print(f'{today.year}/{today.month}/{today.day}')
print()
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)
print()

d1 = datetime.date(2020, 2, 10)
print(d1)

d2 = d1.replace(1990)
print(d2)

d3 = d1 - d2
print(type(d3))
