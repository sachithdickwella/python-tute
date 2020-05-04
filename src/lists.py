#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

my_list = [1, 2, 3]
my_list = ["STRING", 100, 23.2]

print(len(my_list)) # Just like string. 'len()' function to get the size.

my_list = ['one', 'two', 'three']
print(my_list)
print(my_list[0])

# List append.
another_list = ['four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
my_list = my_list + another_list
print(my_list)

# Slicing and indexing are just like String.
print(my_list[3:])
print(my_list[-1])
print(my_list[::-1])    # Reverse the list just like strings.
print(my_list[2::2])
print(my_list[-2::-2])

# Mutate lists.
my_list[0] = "ONE All Caps"
print(my_list)

# Add new elements to end of the list.
my_list.append("eleven")
my_list.append("twelve")
print(my_list)

# Get and remove element from end of the list.
print(my_list.pop())
print(my_list.pop())
print(my_list)

# Get and remove element from specific index.
print(my_list.pop(0))  # ['ONE All Caps', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
print(my_list.pop(4))  # ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
print(my_list.pop(-2)) # ['two', 'three', 'four', 'five', 'seven', 'eight', 'nine', 'ten']
print(my_list)         # ['two', 'three', 'four', 'five', 'seven', 'eight', 'ten']

# Sorting and reverse.
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

print(type(new_list.sort()))  # 'sort()' returns nothing except 'NoneType'.
print(new_list)               # Sorted list.

num_list.sort()               # Does not return anything but sort.
print(num_list)

num_list.reverse()            # Doesn't return anything but reverse the list. 
print(num_list)

# Make the list multiply in size.
print(num_list * 2)

# num_list[100]     Throw and error if an element is out of range.
# Nesting lists.

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

# Multi-dimensional array.
matrix = [list_1, list_2, list_3]
print(matrix)
print(matrix[0])        # Grab an exact list from matrix.
print(matrix[1][1])     # Grab an exact item.

# List comprehensions (Advanced)
# Build a list comprehension by deconstructing a for loop within a []
first_column = [row[0] for row in matrix]   # Iterating list by list and return 0th element.
print(type(first_column))
print(first_column)
