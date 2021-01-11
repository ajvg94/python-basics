
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
#Dicts
#They're like objects in python
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print (dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print (dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print dict['z']                  ## Throws KeyError
if 'z' in dict: print (dict['z'])     ## Avoid KeyError
print (dict.get('z'))  ## None (instead of KeyError)
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Dictionaries (like objects)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print (tel)             # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print (tel['jack'])     # 4098
del tel['sape']
tel['irv'] = 4127
print (tel)             # {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)               # ['jack', 'guido', 'irv']
sorted(tel)             # ['guido', 'irv', 'jack']
print ('guido' in tel)  # True
print ('jack' not in tel)# False
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict: print key
## prints a g o

## Exactly the same as above
for key in dict.keys(): print key

## Get the .keys() list:
print dict.keys()  ## ['a', 'o', 'g']

## Likewise, there's a .values() list of values
print dict.values()  ## ['alpha', 'omega', 'gamma']
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Del
"""
Deletes a variable
"""
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print list      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print dict      ## {'a':1, 'c':3}
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Files 
"""
 The special mode 'rU' is the "Universal" option for text files where it's smart about 
 converting different line-endings so they always come through as a simple '\n'.
"""
# Echo the contents of a file
f = open('foo.txt', 'rU')
for line in f:   ## iterates over the lines of the file
print line,    ## trailing , so print does not add an end-of-line char
                ## since 'line' already includes the end-of-line.
f.close()
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
#Files Unicode
"""
The "codecs" module provides support for reading a unicode file.
"""
import codecs
f = codecs.open('foo.txt', 'rU', 'utf-8')
for line in f:
# here line is a *unicode* string






