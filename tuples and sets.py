##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# TUPLES
"""
A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. Tuples are like lists, 
except they are immutable and do not change size (tuples are not strictly immutable since one of 
the contained elements could be mutable).
"""
tuple = (1, 2, 'hi')
print (len(tuple))  ## 3
print (tuple[2])   ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# SETS
"""
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print (a)                                    # unique letters in a

print (a - b)                              # letters in a but not in b
print (a | b)                              # letters in a or b or both
print (a & b)                              # letters in both a and b
print (a ^ b)                              # letters in a or b but not both
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##





