#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class Dog():

    # CLASS OBJECT ATTRIBUTES
    # SAME FOR ANY INSTANCE OF THE CLASS
    species = 'mammel'

    def __init__(self, breed, name):
        self.breed = breed           # These two variables can be any name. By convention,
                                     # they should be same name.
        self.name = name

    # OPERATION/ACTION -> Methods
    def bark(self, number):
        print('Woof! My name is {}, and I\'m a {}. I\'m {} years old.'
              .format(self.name, self.breed, number))


dog1 = Dog('Lab', 'Sammy')
print(type(dog1))

dog2 = Dog('Husky', 'Riley')
print(type(dog2))

dog1.bark(3)
dog2.bark(2)


class Circle():

    # CLASS OBJECT ATTRIBUTE
    PI = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = self.PI * (radius ** 2) # OR 'Circle.PI' syntax to have static access to PI 
                                            # regardless the object reference.

    # METHOD
    def get_circumference(self):
        return  2 * self.PI * self.radius

    def change_pi(self, pi): 
        self.PI = pi

    def change_pi_static(self, pi):
        Circle.PI = pi


my_circle = Circle()
print(my_circle.get_circumference())

my_circle30r = Circle(30)
print(my_circle30r.get_circumference())

print(my_circle.area)

# Static variable test.
my_circle.change_pi(30)
print(my_circle.PI)

print(my_circle30r.PI)

print("=============================================================")
# Using class reference.
my_circle.change_pi_static(100)    # This wouldn't affect this/self object but the rest of the instances.
print(my_circle.PI)

print(my_circle30r.PI)
print(Circle().PI)

# Callable class references.
class Super():

    def __call__(self, x):
        print(f"Do low level process with {x}")


class Model(Super):

    def __init__(self, y):
        print("Hello" + str(y))

    def f(self, x):
        print(x)


m = Model(0)
m(20)   # Execute class object reference (Could be own or super class).
