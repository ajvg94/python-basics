##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Files 
f = open('workfile', 'w')
"""
The first argument is a string containing the filename. 
The second argument is another string containing a few characters describing the way in which the file will be used.
'r' when the file will only be read
'w' for only writing (an existing file with the same name will be erased)
'a' opens the file for appending; any data written to the file is automatically added to the end
'r+' opens the file for both reading and writing
The mode argument is optional; 'r' will be assumed if it’s omitted
"""
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
"""
It is good practice to use the with keyword when dealing with file objects. 
The advantage is that the file is properly closed after its suite finishes, even if an exception is 
raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:
"""
with open('workfile') as f:
    read_data = f.read()
# Methods
f.read()        #reads all the file
f.readline()    #reads the file by line
f.write('This is a test\n') #writes the contents of string to the file, returning the number of characters written
f.closed
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
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
