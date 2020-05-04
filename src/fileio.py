#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


f = open('out/my_file.txt', "w+")                   # mode = 'r' (read-only)
                                                    # mode = 'w' (write-only - create if not exists and write over).
                                                    # mode = 'a' (append-only) - add on to file.
                                                    # mode = 'w+'(writing and reading - create if not exists and write over).
                                                    # mode = 'r+' (reading and writing)
f.write("This is a text file.\n"
        "This is the second line of the file.\n"
        "This is the third line of the file.\n")
f.close()

# File operations.
f = open('out/my_file.txt')
print(f.read())
print(f.read())                 # Nothing return hence cursor moved from first invoke.
f.seek(0)                       # Move the cursor to the beginning of the file.
print(f.read())                 # Then return the file content again entirely.
f.seek(0)

# Read by line.
print(f.readlines())
f.seek(0)

f.close()

# Something similar like Java's try-with-resources.
with open('out/my_file.txt') as my_opened_file:         # Open the file and assign to a variable. 
                                                        # Here it's 'my_opened_file'. 
    print(my_opened_file.read())
    my_opened_file.seek(0)

    print(my_opened_file.readline())
    print(my_opened_file.readline())
    my_opened_file.seek(0)

    content = my_opened_file.readlines()

    # automatically close the file opened after this block.

print(content) # Content available outside of the block.

with open("out/my_new_file.txt", mode='a') as f:
    f.write('NEW LINE\n')
     # print(f.read())  PROHIBITED!

with open('out/my_new_file.txt', mode='r') as f:
    print(f.readlines())
    # f.write() PROHIBITED except 'r+' mode.
