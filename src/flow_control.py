#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# If-else-if flow control.
marks = 84

if 80 < marks and 100 >= marks:
    print("A")
elif 60 < marks and 80 >= marks:
    print("B")
elif 50 < marks and 60 >= marks:
    print("C")
elif 35 < marks and 50 >= marks:
    print("S")
else:
    print("F")

# Iteration/loop flow control.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in my_list:
    print(num)

for num in my_list:
    if num % 2 == 0:
        print(f'Even number: {num}')    # Even numbers.
    else:
        print(f'Odd number: {num}')     # Odd numbers.

list_sum = 0
for num in my_list:
    list_sum += num

print(list_sum)

my_string = "Hello World"
for text in my_string:
    print(text)

for _ in range(10):         # _, if variable has no issue.
    print("Cool!")

# Tuple un-packing.
tup = (1, 2, 3, 4)
for num in tup:
    print(num)

my_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(f'Tuple length: {len(my_list)}')

for item in my_list:
    print(item)

# OR

for a, b in my_list:                    # Tuple unpacking.
    print(f'First: {a}, Second: {b}')

# Iterate through dictionaries.
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}

for item in my_dict:
    print(item)                         # By default iterate through keys only.

for item in my_dict.items():
    print(item)                         # Now its tuple list that iterate.

for key, value in my_dict.items():
    print(f'Key: {key}, Value: {value}') # Tuple unpacking on dictionary.
else:
    print("End")

# Iteration/loop with 'while' loops.
x = 0
while x < 5:
    print(f'Value of x is {x}')
    x += 1
else:
    print("X is not less than five")

# break, continue and pass
for item in range(5):
    pass # Just a placeholder , do nothing.

# break and continue work just like with Java.