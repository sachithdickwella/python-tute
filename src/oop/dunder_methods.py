#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Special (Magic/Dunder) methods to work with own Class objects.
# Methods starts with __ and ends with __.

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special method for string (Equivalent to Java's toString())
    def __str__(self):
        return 'Book[title={}, author={}, pages={}]'.format(self.title, self.author, self.pages)

    # Special method for length
    def __len__(self):
        return self.pages

    # Special method to trigger when object remove from memory.
    def __del__(self):
        print (f'{self} is deleted')


b1 = Book('Theory of Everything', 'Stephen Hawking', 230)
print(b1)                           # __str__ triggers from the class.
print(len(b1))                      # __len__ triggers from the class.
del b1                              # __del__ triggers from the class.

# After 'del b1', 'b1' variable no longer available below.