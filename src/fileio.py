#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


f = open('out/my_file.txt', "w+")                   # mode = w+ (create if not exists and write over), 
                                                    # r+ (read-only) and a+ (append new content, ratianing 
                                                    # the old content of the file).
f.write("This is a text file.\n"
        "This is the second line of the file.\n"
        "This is the third line of the file.\n")
f.close()

# File operations.
f = open('out/my_file.txt')
print(f.read())
print(f.read())                 # Nothing return hence cursor moved from first invoke.

