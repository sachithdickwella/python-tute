#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# #############################################################################
# Nested statements and scopes (variables)
# #############################################################################
#
# #############################################################################
# LEGB Rule
# 
# L: Local - Names assigned within a function (def of lambda) and not 
#    decalred global in that function
# E: Enclosing function locals - Names in the local space any and all 
#    enclosing functions (def or lambda), from inner to outer.
# G: Global (module) - Names assign at the top-level of a module file, 
#    or declared global in a def within the file.
# B: Build-in (Python) - Names preassigned in the built-in name module
#    : open, range, SyntaxError, etc..
# #############################################################################

# #############################################################################
# Local namespace
# #############################################################################

lambda num: num + 2     # 'num' belongs to the local namespace

# ############################################################################
# Enclosing function locals namespace
# ############################################################################

# GLOBAL
name = "THIS IS A GLOBAL STRING"

def greet():
    # ENCLOSING
    name = "Sammy"

    def hello():
        # LOCAL
        name = "I'M A NAME"
        print(f'Hello {name}') 

    hello()

greet()

# #############################################################################
# Built-in function namespaces.
# #############################################################################

_, _, _ = len, range, open      # Built-in names (functions in this case)
                                # Careful not ot OVERRIDE one of these

# Update global level names/variable.

x = 50
y = 100

def func():
    global x

    # Now this is a global variable reassignment.
    x = 200
    y = 50

func()

print(x)
print(y)