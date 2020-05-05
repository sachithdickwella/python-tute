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