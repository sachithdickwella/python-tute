#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# https://docs.python.org/3.8/library/collections.html

print("""
# #################################################################################################
# Counter class
# #################################################################################################
""")

from collections import Counter

l = [1, 2, 3, 4, 5, 6, 7, 8, 4, 6, 8,  8, 8,
     9, 9, 10, 7, 7, 1, 6, 6, 7, 12, 7, 7]
c = Counter(l) # Count the duplicate elements from the list and re-order them as a dictionary.
print(c)

s = "sdfgfe sfhsgsdfsgdhfshdg fsgdfsjd"
c = Counter(s)
print(c)

sentence = "How many times does each word show up in this sentence word word shoe up up"
words = sentence.split()
c = Counter(words)
print(c)

print(c.most_common(2)) # Get 2 most common words as Tuple list.
print(sum(c.values()))  # Total of all values.
print(list(c))          # List of unique elements.
print(set(c))           # Set of elements (unique hence set has o duplicates).
print(dict(c))          # Convert to a dictionary. 
print(c.items())        # List of (element, count) tuple.
print(c.most_common()[:-2-1:-1])    # 'n' number of Least common element, 'c.most_common()[:-n-1:-1]'.

c = Counter(dict([('S', 2), ('a', 1), ('c', 10), 
                  ('d', 0), ('e', -5)]))            # Convert from list of (element, count) pairs.
                                                    # Syntax - 'Counter(dict(list_of_pairs))'.
print(c)

c += Counter()  # Remove zero(0) and negative(-4) counts from preceding assignment.
print(c)

print("""
# #######################################################################################
# defaultdict class
# #######################################################################################
""")

from collections import defaultdict

# Regular dictionary
d = {'k1': 1}

# print(d['k2'])  # 'KeyError' throws hence 'k2' is not available in 'd' dictionary.

# Default dictionary - create the key, if that key is not available.
d = defaultdict(object)
d['one']          # Since key is not available, key access here will be created in the dictionary.

for k, v in d.items():
    print(f'{k}:{v}')   # Key 'one' is available here and value is an 'object' by default. 

# OR

def f(): return 0

d = defaultdict(f)
d['one']
d['two'] = 10

for k, v in d.items():  # Both values are available, if a value is not assigned to the key, 
                        # default object assign. In this case 'f()' function and return value 
                        # of the function will be assigned unless a value assigned to the key.
    print(f'{k}:{v}')

# OR just use lambda expression to assign a value.
d = defaultdict(lambda: 0) # Lambda takes no paramtere.
d['one']
d['two'] = 20

for k, v in d.items():
    print(f'{k}:{v}')

print("""
# #################################################################################################
# OrderedDict class
# #################################################################################################
""")

from collections import OrderedDict

# Regular dictionary.
d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10

for k, v in d.items():
    print (f'{k}:{v}')
print()

# OrderedDict class
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
d['h'] = 8
d['i'] = 9
d['j'] = 10

for k, v in d.items():
    print (f'{k}:{v}')

# Two regular dictionaries that have similar key-value pairs are equals with == operator despite the order.
# Two OrderedDict that have similar key-value pairs but not match the order, do not equals.

print("""
# #################################################################################################
# namedtuple
# #################################################################################################
""")

# Regular tuple
t = (1, 2, 3)
print(t[0])     # Need to know exact index.

from collections import namedtuple

# 'namestuple' class
Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Husky', name="Sammy")

print(sam.age)
print(sam.breed)
print(sam[2])       # Index also can use if knows the index id.
