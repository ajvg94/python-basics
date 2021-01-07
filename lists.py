colors = ['red', 'blue', 'green']
print (colors[0])   ## red
print (colors[2])   ## green
print (len(colors)) ## 3
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
#Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables 
# point to the one list in memory.

b = colors   ## Does not copy the list
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Go through a list
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print (sum)  ## 30
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Test for element in list
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print ('yay')
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# List Methods
"""
Here are some other common list methods.

    list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
    list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
    list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
    list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
    list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
    list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
    list.reverse() -- reverses the list in place (does not return it)
    list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
"""
list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print (list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print (list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print (list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Sorting lists 
a = [5, 1, 4, 3]
print (sorted(a))  ## [1, 3, 4, 5], returns sorted list, but original remains untouch
print (a)  ## [5, 1, 4, 3]

# reverse=True
strs = ['aa', 'BB', 'zz', 'CC']
print (sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print (sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

# sorting with keys
strs = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# List Comprehensions (optional)
"""
List comprehensions are a more advanced feature which is nice for some cases but is not needed 
for the exercises and is not something you need to learn at first (i.e. you can skip this section). 
A list comprehension is a compact way to write an expression that expands to a whole list. 
Suppose we have a list nums [1, 2, 3, 4], here is the list comprehension to compute a list of 
their squares [1, 4, 9, 16]:
"""
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]
  
strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ] ## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']


