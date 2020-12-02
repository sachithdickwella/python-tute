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
print(f'P{name[1:]}')       # String concatenation
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

# Print formatting with "placeholders".
print("I'm going to inject %s here" % "something")
print("I'm going to inject %s text here, and %s text here" % ("some", "more"))

x, y = "some", "more"
print("I'm going to inject %s text here, and %s text here" % (x, y))

# %s and %r represent 'str()' and 'repr()' functions respectively.
print("He said, his name was %s" % "Fred")
print("He said, his name was %r" % "Fred")      # %r takes the string representation with quotes.

print("I once caught a fish %s" % "this \tbig")
print("I once caught a fish %r" % "this \tbig") # %r does not render escape characters. 

print("I wrote %s programs today" % 3.75)
print("I wrote %d programs today" % 3.75)   # %d converts numbers to integer without rounding.

# Padding and precision of floating point numbers.
print("Floating point number : %5.2f" % 13.144)  
print("Floating point number : %1.0f" % 13.144)
print("Floating point number : %1.5f" % 13.144)
print("Floating point number : %0.5f" % 13.144)
print("Floating point number : %10.5f" % 13.144)

print("First : %s, Second : %5.2f, Third : %r, Fourth : %d" % ("Hi", 3.1415, "Bye!", 3.1415))

# Print formatting with strings "format()" function.
print("This is a string {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {0} {1} {2}".format("fox", "brown", "quick"))        # Repeat by refering same index.
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))  # Assigning variable to index.
print("The {q} {q} {q}".format(f="fox", b="brown", q="quick"))  # Repeat by refering same index variable.

# Float formatting "{value:width.precision f}" with "format()" function.
result = 100/777
print(result)
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))      # Float formatting while roundup.
print("The result was {r:10.3f}".format(r=result))     # width=10 add preceding 10 spaces.

result = 100 / 0.245
print(result)
print("The result was {r:1.4f}".format(r=result))      # Value keep the length even width=1.

# Alignment, padding and precision with 'format()'.
print("{0:8} | {1:9}".format("Fruit", "Quantity"))
print("{0:8} | {1:9}".format("Apples", 3.))
print("{0:8} | {1:9}".format("Oranges", 10))

print("{0:<8} | {1:^8} | {2:>8}".format("Left", "Centre", "Right"))
print("{1:<8} | {2:^8} | {0:>8}".format(11, 22, 43))

# Precede the alignment operator with padding character.
print("{0:-<8} | {1:=^8} | {2:.>8}".format("Left", "Centre", "Right"))
print("{0:-<8} | {1:=^8} | {2:.>8}".format(11, 22, 43))

# Print formatting with string "f-strings".
name = "Jose"
print(f"Hello, his name is {name}")

name = "Sam"
age = 30
print(f"{name} is {age} years old")
print(f"{name!r} is {age} years old") # !r function to 'repr()' string.

# Float formatting "{value:{width}.{precision}}"
num = 24.45678
print(f"My 10 character, four decimal number is:{num:{10}.{6}}") # Precision refers to total number 
                                                                 # of digits.
print(f"My 10 character, four decimal number is:{num:10.4f}")    # Equivalent to 'format()' function.

import string

print(string.ascii_uppercase)

print('A'.isupper())    # Supplementary functions.
print('a'.islower())

# Find string in a larger string content.
hello = 'Hello, World!'
idx = hello.find('Wor') # Return the index or -1 if not found.
print(idx)

# OR

idx = hello.index('lo') # Return the index or throws an error -> ValueError: substring not found. 
print(idx)
