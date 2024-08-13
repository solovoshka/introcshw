# Jacqueline Soloveychik
# Professor Thayer
# Intro to Programming
# Homework 5

# Question 1
'''
1. (25 points) Write a function named remove_spaces that will remove the
spaces from the provided string and return the result. Please remember to put
a signature at the top of your function indicating the types of input and output
, and if any preconditions exist.  Before submitting your work, verify that
your function works correctly by testing it in Python's interactive mode with
the following inputs:
>>> remove_spaces ('hello ')
'hello'
>>> remove_spaces ('I said , hello !')
'Isaid,hello!'
>>> remove_spaces (' is anyone listening ?? ')
' isanyonelistening ??'
'''


# function signature 
# 1. sig: str → str
# 2. precondition: none, but every char execpt spaces is transcribed into new
# 3. description: the function takes a string paramater and rewrites it into
# a variable -new- into which every character of s except the spaces are translated
# into 


def remove_spaces(s):
    new = ""
    for char in s:
        if char != " ":
            new += char
    return(new)

'''
another solution using replace (my initial idea):
        if char == " ":
            char.replace(" ", "")
        else:
            new = new + char
'''

# function calls
print(remove_spaces('hello '))   
print(remove_spaces('I said, hello !'))
print(remove_spaces(' is anyone listening ?? '))


##############################################################################


# Question 2
'''2. (25 points) A palindrome is “a word or phrase that reads the same
backward as forward." For example, “madam" and “a man a plan a canal panama"
are palindromes. Note that spaces are ignored. Write a function
named is_palindrome that will return True when its parameter, a string, is a
palindrome. The function should ignore the presence of spaces in the input.
Your is_palindrome should call your remove_spaces function to ensure that
spaces are not considered. Thus, “a man a plan a canal panama" should be
considered a palindrome because “amanaplanacanalpanama" is. Please include a
signature at the top of your function.  Before submitting your work, verify
that your function works correctly by testing it in Python's interactive mode
with the following inputs:


>>> is_palindrome ('a man a plan a canal panama ')
True
>>> is_palindrome ('moon')
False
>>> is_palindrome ('nurses run')
True
>>> is_palindrome ('tacocat')
True
>>> is_palindrome ('spatula dog')
False
>>> is_palindrome ('never odd or even')
True
>>> is_palindrome ('k')
True
'''

# function signature 
# 1. sig: str → bool
# 2. none
# 3. the function calls remove_spaces(), which removes the spaces in s;
# it then revereses the forwards variable which creates backwards. Then,
# if forwards equals to backwards, it returns that the statement is True; else
# -> False. The function compares if the forwars has the same value as backwards


# parameter: string
def is_palindrome(s):
    forwards = remove_spaces(s)
    backwards = remove_spaces(s[::-1])
    if forwards == backwards:
        return True
    else:
        return False
    
'''
(another) solution -> my initial one that was way too complex:
def is_palindrome(s):
    forwards = remove_spaces(s)
    backwards = remove_spaces(s[::-1])
    for i in range (len(forwards)):
        for j in range (len(backwards)):
            if forwards[i] == backwards[j]:
                return True
            else:
                return False
'''

'''
# question: why is an object of NoneType sometimes ???
# ans: because my other function was not returning val, was just printing, so
# when called from another function it was creating a NoneType variable
'''


# function calls
print(is_palindrome ('a man a plan a canal panama '))
print(is_palindrome ('moon'))
print(is_palindrome ('nurses run'))
print(is_palindrome ('tacocat'))
print(is_palindrome ('spatula dog'))
print(is_palindrome ('never odd or even'))
print(is_palindrome ('k'))

##############################################################################


# Question 3
'''
3. (25 points) Write a function finder that takes two string parameters,
needle and haystack. Your function should find the last occurrence of needle
in haystack and return its position. If needle does not occur in haystack,
your function should return -1. Please include a signature at the top of your
function. Before submitting your work, verify that your function works correctly
by testing it in Python's interactive mode with the following inputs:

>>> finder ('dog', 'dog eat dog world ')
8
>>> finder ('green', 'orange red black ')
-1
>>> finder ('ea', 'heat the tea leaning back ')
14
>>> finder ('he', 'heat the tea leaning back ')
6
>>> finder ('hea', 'heat the tea leaning back ')
0
'''
# function signature 
# 1. sig: (str, str) → int
# 2. precondition: if the first string has an occurence in the seconds string
# 3. the function checks if one string is in another string; then it continues
# to overwrite the index of the first letter of -needle- in the second string
# until it gets to the largest possible index (returns the index of the needle
# in the furthermost position it can be in haystack) 


def finder(needle, haystack):
    if needle in haystack:
        firstindex = haystack.find(needle)
        finalindex = firstindex
        for i in range (len(haystack)):
            if needle == haystack[i:i+len(needle)]:
                finalindex = i
        return finalindex
    else:
        return -1

# function calls
print(finder ('dog', 'dog eat dog world '))
print(finder ('green', 'orange red black '))
print(finder ('ea', 'heat the tea leaning back '))
print(finder ('he', 'heat the tea leaning back '))
print(finder ('hea', 'heat the tea leaning back '))

##############################################################################


# Question 4
'''
4. (25 points) We will call title case the condition when the first
letter of every word in a string is upper case. Write a function named
title_case that will convert a string to title case by capitalizing the first
letter of every word. Non-first letters should be left unchanged.  You may use
the upper() function to convert a character to upper case.
>>> text = "v"
>>> text. upper ()
'V'

Please include a signature at the top of your function.  Before submitting
your work, verify that your function works correctly by testing it in Python's
interactive mode with the following inputs:

>>> title_case ("hello")
'Hello'
>>> title_case ("He ate all the avocados!")
'He Ate All The Avocados !'
>>> title_case ("and the BANANAS?")
'And The BANANAS?'
'''

# function signature 
# 1. sig: str → str
# 2. precondition: none on param; only on i -> must be less than the length of s
# 3. rewrites the string s into a variable -new-; automatically capitalizes
# the first letter of str (index 0); then enters a while loop, and each time
# s at index i has the same value as " " (a space), then it jumps one index
# ahead, capitalizes that character, and transcribes it into new (spaces included)
# -> for this instance, i is then increased by 2 (since two characters are
# transcribed); for other instances, the character is simply written into new and
# i is only increased by 1

def title_case(s):
    new = ""
    new += s[0].upper()
    i = 1
    while i < len(s):
        if s[i] == " ":
            new = new + s[i] + s[i+1].upper()
            i+=2
        else:
            new += s[i]
            i+=1
    return new

'''
### Question -> what if there are numbers in the string?
# -> irrelevant for this problem
'''

# function calls
print(title_case ("hello"))
print(title_case ("He ate all the avocados!"))
print(title_case ("and the BANANAS?"))








