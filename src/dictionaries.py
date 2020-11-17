#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

prices_lookup = {"apple": 2.99, "oranges": 1.99, 'milk': 5.99}
print(prices_lookup)
print(prices_lookup["apple"])

d = {"k1": 127, "k2": [1, 2, 3], "k3": {"ik1": 100, "ik2": ['a', 'b', 'c', 'd']}}
print(d)
print(d["k1"])
print(d["k2"][1])
print(d["k3"]["ik1"])
print(d["k3"]["ik2"][2].upper())

# Update dictionary values.
d["k1"] = "NEW VALUE"
print(d)

# Dictionary functions.
print(d.keys())     # Get all the keys as a list.
print(d.values())   # Get all the values as a list.
print(d.items())    # Get all the items (key: value) as a tuple.

print('apple' in prices_lookup)

d["k4"] = "New Key Value"
print(d) 
