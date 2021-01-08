##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# Strings
s = 'hi'
print(s[1])         ## i
print(len(s))       ## 2
print(s + ' there')  ## hi there

pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes

raw = r'this\t\n and that'

# this\t\n and that
print (raw)

multi = """It was the best of times.
It was the worst of times."""

# It was the best of times.
# It was the worst of times.
print (multi)
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# String methods
"""
    s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
    s.strip() -- returns a string with whitespace removed from the start and end
    s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
    s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
    s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
    s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
    s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
    s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
"""
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# String slices
"""
    H   e   l   l   o
    0   1   2   3   4
   -1  -2  -3  -4  -5
    
    s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
    s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
    s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
    s[1:100] is 'ello' -- an index that is too big is truncated down to the string length 

    s[-1] is 'o' -- last char (1st from the end)
    s[-4] is 'e' -- 4th from the end
    s[:-3] is 'He' -- going up to but not including the last 3 chars.
    s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string. 
"""
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# String %
"""
Python has a printf()-like facility to put together a string. The % operator takes a printf-type format 
string on the left (%d int, %s string, %f/%g floating point), and the matching values in a tuple on the 
right (a tuple is made of values separated by commas, typically grouped inside parentheses):
"""
text = ("%d little pigs come out, "
    "or I'll %s, and I'll %s, "
    "and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))
##--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--####--##
# i18n Strings (Unicode)
"""
Regular Python strings are *not* unicode, they are just plain bytes. To create a unicode string, 
use the 'u' prefix on the string literal:
"""
ustring = u'A unicode \u018e string \xf1'
print(ustring)



