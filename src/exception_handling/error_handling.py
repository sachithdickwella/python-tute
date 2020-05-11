#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def add(n1, n2):
    print(n1 + n2)

# add(10, 20)             
# No need to try-except ↑

try: 
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
    
except:
    print("Hey, It looks like aren't adding correctly!")
else:   # Only execute when no error.
    print("Add went well!")
    print(result)
finally:
    print("I/finally always happens after else")

try:
    with open('../../out/testfile.txt', 'w+') as f:
        f.write('Write test line!')

except TypeError:
    print('There is a type error')
except IOError as ex:
    print('Hey, you have a OS error/IO error', ex)
except:
    print('All other exceptions')
finally:
    print('I always run')