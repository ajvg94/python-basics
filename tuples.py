##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Tuples
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
