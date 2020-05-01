#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

name = "Python 'strings' program"

print(type(name))   # Type of the reference.
print(len(name))    # Length of the string value.

# Get the character from the index out of string.
hello = "Hello, World"

print(hello[0])     # First letter of the string(H).
print(hello[10])    # 11th letter of the string(l).
print(hello[-2])    # 2nd letter from the end(l)
print(hello[-1])    # 1st letter from the end [last letter](d).

# String slicing (substring).
chars = "abcdefghijk"
print(chars[2:])    # 3rd letter to end of the string.
print(chars[:3])    # Beginning to 4th letter (4th letter not included). 
print(chars[3:6])   # From 4th(index 3) up to 7th(index 6) letter(7th letter not included).
print(chars[1:3])   # From 2nd(index 1) up to 4th(index 3) letter(4th letter not included).

# String steps.
print(chars[:])     # All the way to the end.
print(chars[::])    # All the way to the end with steps.
print(chars[::1])   # All the way to the end with steps 1 (default value is 1).
print(chars[::2])   # All the way to the end with steps 2 (skip 1 by 1 from start).
print(chars[::3])   # All the way to the end with steps 3 (skip 2 by 2 from start).
print(chars[2:7:2]) # From 3rd letter(index 2) to 8th letter(index 7) by two steps.
print(chars[::-1])  # Reverse the string with -1 steps (Interview question).
print(chars[::-2])  # Reverse the string with -2 steps (skip 1 by 1 backward).
print(chars[-2:-7:-2])  # Reverse the string from -2nd index to -7th index by 2 steps. 
                        # (+ start and end indexes doesn't work with - (backward) steps.)

# String properties and methods.
name = "Sam"

# name[0] = 'P' ; String in python is immutable. Cannot modify unless creating a new string.
print('P' + name[1:])       # String concatenation
print((name + " ") * 10)    # String multiplication to append a string specific number of times.
# print(2 + "5") ; This is prohibited in python unlike java unless parse one of each value to other 
# value's type.
print(str(2) + "5")         # Parse 'int' to 'string'.
print(2 + int("5"))         # Parse 'string' to 'int'.


prop = "Hi, This is a String in Python"
print(prop.upper())     # To upper case.
print(prop.lower())     # To lower case.
print(prop)             # Doesn't change the 'prop' variable value hence string immutable.
print(prop.upper)       # This is valid. Instead of executing the function, just return the function 
                        # instance.
# Split string.
print(prop.split())     # 'split()' return a list base on the parameter letter. 
                        # (Default whitespace if no letter passed.)
print(prop.split("i"))  # 'split()' by 'i' character/letter.
