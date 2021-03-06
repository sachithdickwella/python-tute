#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

my_list = [1, 2, 3]
my_list = ["STRING", 100, 23.2]

# OR

my_list = [0] * 3
print(my_list)

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
print(my_list[-2:-1:-1])

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

# OR

print(sorted(new_list))       # Build-in function 'sorted()'

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

# List comprehensions (flatten the for loop).
my_string = 'hello'
my_list = []

for letter in my_string:
    my_list.append(letter)

print(my_list)

my_list = [letter for letter in "Hello, World"]
print(my_list)

my_list = [num for num in range(0, 10)]
print(my_list)

my_list = [num ** 2 for num in range(0, 11)]
print(my_list)

# With other flow controls, like 'if'.
my_list = [num ** 2 for num in range(0, 11) if num % 2 == 0]
print(my_list)

my_list = [num if num % 2 == 0 else 'ODD' for num in range(0, 11)]
print(my_list)

# Nested 'for' loops.
my_list = []
for x in [2, 4, 6]:
    for y in [4, 40, 100]:
        my_list.append(x * y)

print(my_list)

my_list = [x * y for x in [2, 4, 6] for y in [4, 40, 100]]
print(my_list)
