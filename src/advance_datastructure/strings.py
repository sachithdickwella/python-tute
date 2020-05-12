#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

hello = "Hello World!"

print(hello.count('l')) # Number of occurrences.
print(hello.find('l'))  # Index of first found of given letter.

print(hello.center(40, '-'))

print('Hello\tWorld!')
print('Hello\tWorld'.expandtabs())

print(hello.isalnum())
print(hello.isalpha())
print(hello.islower())
print(hello.istitle())
print(hello.isspace())
print(hello.isupper())
print(hello.endswith('!'))

# Regex on strings.
print(hello.split('e'))
print(hello.partition('e')) # Return a 3-tuple.

