#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Hexadecimal representation.
print(hex(12))
print(hex(256))
# Binary representation.
print(bin(10))
print(bin(64))
# Octal-decimal representation. 
print(oct(34))
print(oct(458))

power = 2 ** 4
print(power)

power = pow(2, 4)    # Efficient.
print(power)  

power = pow(2, 4, 3) # Efficient and third argument for modulus(%).   
print(power)  

absolute = abs(-5)   # Return absolute value.
print(absolute)

rounded = round(10.45678, 2)    # Round the number with given precision points.
print(rounded)