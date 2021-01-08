##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# For Range
"""
    The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) 
    returns a, a+1, ... b-1 -- up to but not including the last number. 
    The combination of the for-loop and the range() function allow you to build a traditional 
    numeric for loop:
"""
## print the numbers from 0 through 99
for i in range(100):
    print (i)
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
#While
## Access every 3rd element in a list
i = 0
a = [1,2,3,4,5,6,7,8,9]
while i < len(a):
    print (a[i])
    i = i + 3
