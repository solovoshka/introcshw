# Homework 8: Files
# Jacqueline Soloveychik 
# Jacqueline Soloveychik
# Prof. Thayer
# Homework 8: Files 
# Problem 1
'''
Write a function called print_dir_contents that takes a string representing a
path to a directory and prints the following:

• the total number of ordinary files (i.e. non-directories) contained in the
given directory,
• a list of those files in alphabetic order,
• the total number of subdirectories contained in the given directory,
• a list of those subdirectories in alphabetic order.

You may assume the precondition that the argument string represents a valid
path to a directory. The output of your function should be formatted like this:
>>> print_dir_contents ( ’sample’ )
Contents of directory sample
4 files:
    file_1
    file_2
    file_3
    file_4
2 subdirectories:
    dir_1
    dir_2
'''
import os
os.getcwd()

def print_dir_contents(dirname):
    '''
    sig: string -> int, list, and list
    desc: prints the number of files, a list of them in alphabetical order,
    the total number of subdirectories, and a list of them in alphabetical
    order using looping.
    '''
    ordinary_files = []
    subdirectiories = []
    for item in os.listdir(dirname):
        path = os.path.join(dirname, item)
        if os.path.isfile(path):
            ordinary_files.append(item) 
        if os.path.isdir(path):
            subdirectiories.append(item)
    ordinary_files.sort()
    subdirectiories.sort()
    print('files: ', len(ordinary_files))
    for thing in ordinary_files:
        print(thing)
    print('subdirectories: ', len(subdirectiories))
    for otherthing in subdirectiories:
        print(otherthing)

print_dir_contents('C:/Users/solov/OneDrive/Wesleyan/FR-SEM1/COMP-IntroProgramming')

# output:
'''
files:  51
CS Lecture 04 Flow COntrol.docx
CS Lecture 05 String Processing.docx
CS Lecture 06 Lists.docx
CS Lecture 08 File Input and Output.docx
CS-9.5 notes Lecture 1.docx
Course_Calendar_COMP112_F23 (2).xlsx
Exam I S19.docx.pdf
HW1.py
HW4 and HW5 solutions.docx
HW4 and HW5 solutions.pdf
JSoloveychik HW2.py
JSoloveychik_Exam1_Part2_and_3.py
JSoloveychik_HW1.py
JSoloveychik_HW3.py
JSoloveychik_HW3.txt
JSoloveychik_HW4.py
JSoloveychik_HW5.py
JSoloveychik_HW6.py
JSoloveychik_HW7.py
JSoloveychik_HW8.py
JSoloveychik_Lab 2.py
JSoloveychik_Lab3.py
JSoloveychik_Lab5.py
JSoloveychik_Lab6.py
JSoloveychik_Lab7.py
JSoloveychik_Lab8.py
...
subdirectories:  0
'''

# Problem 2
'''
Use your solution to problem 1 to write a function called
checked_print_dir_contents that takes a string
argument and prints the contents if that string represents a path to a
directory, or prints a helpful error message otherwise.

For example:
>>> checked_print_dir_contents ( ‘sample/ non_existent_subdir’ )
sample/ non_existent_subdir is not a valid path .
>>> checked_print_dir_contents ( ’sample/file_1’ )
sample/ file_1 is not a directory.


Hint: you may find Python’s exception handling mechanism (try and
except blocks) useful for this task.
'''
print("           ")
def checked_print_dir_contents(dirname):
    '''
    sig: str -> str
    desc: prints the contents if string represents a path to a
    directory, or prints a helpful error message otherwise
    '''
    try:
        ordinary_files = []
        subdirectiories = []
        for item in os.listdir(dirname):
            path = os.path.join(dirname, item)
            if os.path.isfile(path):
                ordinary_files.append(item) 
            if os.path.isdir(path):
                subdirectiories.append(item)
        ordinary_files.sort()
        subdirectiories.sort()
        print('files: ', len(ordinary_files))
        for thing in ordinary_files:
            print(thing)
        print('subdirectories: ', len(subdirectiories))
        for otherthing in subdirectiories:
            print(otherthing)
    except FileNotFoundError:
        print("Sorry, that is not valid.")
    
checked_print_dir_contents("C:/Users/solov/OneDrive/Wesleyan")
checked_print_dir_contents("C:/Users/solov/OneDrive/Wesleyan/cat")

'''
files:  3
Conway's Game of Life
desktop.ini
resume 2023.pdf
subdirectories:  1
FR-SEM1
Sorry, that is not valid.
'''


# Problem 3
'''
Write a function called file_stats that takes a string representing a path
to a text file. Your function should print the number of words and the number
of lines occurring in the file. If the argument string is not a valid path or
represents a directory instead of a file, your function should print a helpful
message.

Example:
>>> file_stats ( ’sample/file_1’ )
the file sample/file_1 contains 83 words on 12 lines.
>>> file_stats ( ’ sample/dir_1 ’ )
sample/dir_1 is not a file.
>>> f i l e _ s t a t s ( ’ sample/ does_not_exist ’ )
sample/ does_not_exist is not a valid path .

Hint: you may find the str.split function helpful.
'''
print("           ")
def file_stats(file):
    '''
    sig: str -> int, int
    desc: function prints the number of words and the number
    of lines occurring in the file; if the argument string is not a valid path,
    then prints a helpful message
    '''
    try:
        wordcount = 0
        linecount = 0
        f=open(file, 'r')
        for line in f:
            linecount+= 1
            wordcount+= len(line.split())
        print("Line count: ", linecount)
        print("word count: ", wordcount)
    except FileNotFoundError:
        print("file not valid")

file_stats("C:/Users/solov/OneDrive/Wesleyan/FR-SEM1/COMP-IntroProgramming/some_poemlol.txt")

'''
Line count:  7
word count:  51
'''

# Problem 4
'''
Write a function called find_in_file that takes a string representing
a path to a text file and a search string. Your function should return the
list of line numbers (in order) on which the search string appears
(where the first line in a file is line 1, not line 0). Even if the search
string appears more than once on a given line, the line number should be
listed only once. You may assume the precondition that the first argument
represents a valid path to a file.

For example, if the file hi.txt contains the lines:
hi
ho
hihi
ho
your function should report:
>>> find_in_file ( ’ hi . txt ’ , ’ hi ’ )
[ 1 , 3 ]
'''

print("           ")

def find_in_file(file, searchstr):
    '''
    sig: str -> list 
    desc: return the list of line numbers (in order) on which the search
    string appears
    '''
    f=open(file, 'r')
    linenums = []
    counter = 0
    for line in f:
        counter +=1
        if searchstr in line:
            linenums.append(counter)
    print(linenums)
    f.close()

find_in_file("C:/Users/solov/OneDrive/Wesleyan/FR-SEM1/COMP-IntroProgramming/some_poemlol.txt", "say")


'''
[1, 4]
'''



