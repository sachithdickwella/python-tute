#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# IDEA to create a decorator.
# Return functions from a function.
def hello(name='Sachith'):
    print('The hello() function has been executed!')

    def greet():
        return "\tThis is greet() function inside hello()!"

    def welcome():
        return "\tThis is welcome() function inside hello()!"

    print('I am going to return a function!!')

    if name == 'Sachith':
        return greet
    else:
        return welcome


my_new_func = hello()
print(my_new_func())

# Pass functions into a function.
def hello():
    return "Hello, Sachith!"

def other(func):
    print('Other code execute here')
    print(func())

other(hello)


# DECORATOR definition - IMPORTANT and do not change. Invoke using @ operator.
def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the original function!')

        original_func()

        print('Some extra code after original function!')

    return wrap_func()


def func_need_decorator():
    print("I want be decorated!")

new_decorator(func_need_decorator)      # Decoration here.

# Instead, use @ operator to call the decorator.
@new_decorator
def func_need_decorator():
    print("I want to be decorated")
