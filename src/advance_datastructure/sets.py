#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

sc = s.copy()   # Create a new set with same data and return.

s.clear()       # Clear out the set.

print(s)
print(sc)

# set1.difference(set2)
s = {1, 2, 3, 4}

print(sc.difference(s))     # Return the difference in a set. ARGUMENT set must be smaller than caller set.

# 'set1.difference_update(set2)'
s1 = {1, 2, 3, 4}
s2 = {1, 5, 6, 3}

s1.difference_update(s2)    # Compare caller set with ARGUMENT set and update the different in caller set. 
                            # Return nothing and just update the caller set. Which means , remove elements 
                            # from caller set which duplicate with argument set's elements.
print(s1)

# 'set.discard(int)'
print(s2)
s2.discard(3)   # Remove the given element from the set if it's a member or do nothing. 
                # 'remove()' throws a 'KeyError' if the elements is not a member.
print(s2)

# 'set1.intersection(set2)'
s1 = {1, 2, 3}
s2 = {1, 2, 4}

print(s1.intersection(s2))  # Opposite of the set1.difference(set2) function. Return the common 
                            # element with set2.

# 'set1.intersection_update(set2)'
s1.intersection_update(s2)  # Instead of returning common element set, update the caller set with 
                            # common elements.
print(s1)

# 'set1.isdisjoint(set2)' - check whether caller and argument sets are intersects at leasts with single 
# member, and if intersects, return False else True.

s1 = {1, 2, 3}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s2)) # This intersects , thus False.
print(s1.isdisjoint(s3)) # This doesn't intersect, thus True.

# 'set1.issubset(set2)' - Check if the caller set is a subset of argument set.
s1 = {1, 2}
s2 = {1, 2, 3, 4}

print(s1.issubset(s2))

# 'set1.issuperset(set2)' - Check if the caller set is a super set of argument set.
# 
#  Opposite of 'subset'.

print(s2.issuperset(s1))

# 'set1.symmetric_difference(set2)'
print(s1.symmetric_difference(s2)) # Similar to 'set1.difference(set2)' functionality, 
                                   # except this is symmetrical. Which means, unlike 'set1.difference(set2)'
                                   # function, ARGUMENT set may or may not be smaller than caller set. Either
                                   # way this function work.

# 'set1.symmetric_difference_update(set2)'
s1.symmetric_difference_update(s2) # # Difference update into caller set.
print(s1)          

# 'set1.union(set2)'
s1 = {1, 2, 3}
s2 = {1, 2, 4, 5, 6}

print(s1.union(s2))     # Put together elements of either sets. No duplicates though (No duplicates in sets). 

# 'set1.update(set2)'
s1.update(s2)           # Update caller set itself with argument set members while UNION.
