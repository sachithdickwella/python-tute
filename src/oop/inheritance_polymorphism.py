#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

print('''
# #############################################################################
# INHERITANCE
# #############################################################################
''')

class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


class Dog(Animal):

    def __init__(self):
        super().__init__()      # 'super()' call is NOT MANDATORY
        print('DOG CREATED')

    # METHOD OVERRIDE - Unless this overridden, super class method would be called.
    def who_am_i(self):
        print('I am a dog')


dog1 = Dog()
dog1.eat()
dog1.who_am_i()

print('''
# #############################################################################
# POLYMORPHISM
# #############################################################################
''')

# ABSTRACT class implementation.
class Animal():
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Sub-class must be implemented for this class')


# CONCRETE class implementation.
class Lion(Animal):

    def speak(self):
        return self.name + ' says roar!'


class Cat(Animal):
    
    def speak(self):
        return self.name + ' says meow!'


cindy = Lion('Cindy')
felix = Cat('Felix')

pets = [cindy, felix]

for pet in pets:
    print(pet.speak())
