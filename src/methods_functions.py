#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

my_list = [1, 2, 3, 4]
print(help(my_list.insert))     # Inbuilt 'help()' function to see help.

def name_function():
    '''
    DOCSTRING: Information about the function.
    INPUT: No input
    OUTPUT: Hello
    '''
    print('Hello')

name_function()
print(help(name_function))

def say_hello(name='Name'):     # Default parameter value is 'Name'.
    print(f'Hello {name}')
    return 'Hello {}'.format(name)

result = say_hello("Sachith")
print(result)

def add(n1, n2):
    return n1 + n2

result = add(10, 20)
print(result)

def dog_check(text):
    return 'dog' in text.lower()

print(dog_check('Cat ran away!'))

def pig_latin(word):
    if (word[0].lower() in 'aeiou'):
        return f"{word}ay" 
    else:
        return f'{word[1:]}{word[0]}ay'

print(pig_latin('Apple'))
print(pig_latin('Orange'))
print(pig_latin('Mango'))

# Functions with *args and **kwargs
def my_func(a, b):  # These are positional arguments
    # Return 5% of the sum of 'a' and 'b'
    return sum((a, b)) * 0.05

print(my_func(10, 5))

def my_func2(*args):    # Similar to var args in Java.
    print(type(args))
    print(args) # Print a tuple
    for num in args:
        print(num)

my_func2(10, 12, 40, 30, 25)

def my_func3(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
    
    print(kwargs)   # Print a dictionary here.

my_func3(fruit='apple', veg='lettuce')

def my_func4(*args, **kwargs): # Should follow the this order even if the paramater 
                               # positions are switched.
    print("I would like {} {}s".format(args[0], kwargs["food"]))

my_func4(10, 30, 40, 50, fruit='apple', food='orange', animal="dog")

print(str(['a', 'b', 'c']))

# Task #1.
def my_func1(text):
    return ''.join([t.upper() if i % 2 == 0 else t.lower() for i,t in enumerate(text)])

print(my_func1("Sachith Dickwella"))

# Task #2
def my_func5(num):
    for i in range(0, len(num)):
        print(num[i:i + 2])
        if num[i:i + 2] == [3, 3]:
            return True
    return False

print(my_func5([1, 3, 3]))