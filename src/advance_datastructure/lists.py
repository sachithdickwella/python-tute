#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

l = [1, 2, 3, 4, 5]
print(l)
print(l.count(1))   # Count number of occurrences.

# 'list1.extend(list2)' -  Add argument list elements to caller list. 
x = [6, 7, 8]
print(x)

x.extend(l)         # Add argument list to caller list (flatmap extend), instead of adding argument 
                    # list as element of caller list. 
print(x)

# 'list.index(element)' - Return the given element's index in the list.
print(l.index(2))   # Return the index of given member of the list. Throw error, if element is not 
                    # available.

# 'list.insert(int, element)' - Insert element into given index and update the subsequent list.
print(l)
l.insert(2, 'inserted')
print(l)

# 'list.remove(int)' - Remove first occurrence of given value. Raise 'ValueError' if value is not available.
# 'list.pop(int)' function expect for the index when 'list.remove(object)' expect an element.
l.remove('inserted')
print(l)
