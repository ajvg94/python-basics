colors = ['red', 'blue', 'green']
print (colors[0])   ## red
print (colors[2])   ## green
print (len(colors)) ## 3

#Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables 
# point to the one list in memory.

b = colors   ## Does not copy the list
