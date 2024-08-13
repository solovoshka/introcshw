# Jacqueline Soloveychik
# Homework 6 Lists
# COMP 112 
# Prof. Thayer

# Instructions
'''
Please answer all the questions in a single python script.
Please include the problem numbers as comments.
Please include a header with your name, section, assignment and the date at
the top of your work as a comment.
Put all your answers in a file labeled hw5_<your_name>.py.
Please use signatures at the top of your functions.
The functions in this assignment should not use the print function;
they should return the result.
Submit your answer to Moodle in the section in which you are registered.
'''

# Question 1
'''
1. (20 points) Write a function named indices that takes
two parameters: x, a value; and xs, which will be a list of values.
The function should return a list of indices into xs where that element is
equal to x. For example:
>>> indices (5, [1, 5, 20, 100 , 5, 5])
[1, 4, 5]
>>> indices (" dog ", [" dog ", "dog ", "cat ", " chinchilla ", " zebra "])
[0, 1]
>>> indices ("?" , ["a", "b", "c"])
[]
'''


def indices(x, xs):
    '''
    sig: (any value, list) → list of ints
    return a list of indices into xs where that element is
    equal to x
    '''
    
    index_list = []
    for i in range(len(xs)):
        if x == xs[i]:
            index_list.append(i)
    xs.insert(len(xs), index_list)
    return xs[len(xs)-1]

print(indices(5, [1, 5, 20, 100 , 5, 5]))
print(indices("dog", ["dog", "dog", "cat", "chinchilla", "zebra"]))
print(indices ("?" , ["a", "b", "c"]))


# Question 2
'''
2. (20 points) Given a non-empty list of floats, write a
function named avg to calculate and return their average.
>>> avg ([0.0 , 10.0])
5.0
>>> avg ([ -1.5 , 3.4 , 20.1])
7.333333333333333
>>> avg ([60.0 , 60.0 , 80.1 , 95.0])
73.775
'''

def avg(numberlist):
    '''
    sig: (float list) → float
    calculate and return the average for a non-empty list of floats
    '''
    
    num = 0
    for x in numberlist:
        num += x
    averagenums = num/len(numberlist)
    return averagenums
    
print(avg ([0.0 , 10.0]))
print(avg ([ -1.5 , 3.4 , 20.1]))
print(avg ([60.0 , 60.0 , 80.1 , 95.0]))



# Question 3
'''
3. (20 points) Write a function named sum_some that returns the sum of all
positive integers in a given list. If 0 occurs in the list, all subsequent
values are not counted toward the sum.
For example:
>>> sum_some ([1 ,2 , -3 ,4 ,5])
12
>>> sum_some ([1 ,2 , -3 ,4 ,5 ,0 ,100 ,200])
12
'''


def sum_some(numlist):
    '''
    sig: (int list) → int
    returns the sum of all positive integers in a given list
    If 0 occurs in the list, all subsequent
    values are not counted toward the sum
    '''
    
    posint = 0
    for num in numlist:
        if num > 0:
            posint += num
        elif num == 0:
            break
    return posint

print(sum_some ([1 ,2 , -3 ,4 ,5]))
print(sum_some ([1 ,2 , -3 ,4 ,5 ,0 ,100 ,200]))


# Question 4
'''
4. (a) (20 points) Write a function dedup to remove duplicates from a list and
return the result. Your strategy should include building up a new list that
gets returned.
>>> dedup ([" eggplant ", " chicken ", " tomato ", " chicken ", " television "])
[' eggplant ', 'chicken ', 'tomato ', 'television ']
>>> dedup ([5 , 10, 20, 10, 90, 20, 20, 20, 4, 3, 5])
[5, 10, 20, 90, 4, 3]
'''

def dedup(xs):
    '''
    sig: list -> list
    remove duplicates from a list and return the result by building a new list,
    which is the thing getting returned
    '''
    
    new_list = []
    for x in xs:               
        if x not in new_list:
            new_list.append(x)
    return new_list

print(dedup (["eggplant", "chicken", "tomato", "chicken", "television"]))
print(dedup ([5 , 10, 20, 10, 90, 20, 20, 20, 4, 3, 5]))


'''
(b) (20 points) Modify your dedup function so it modifies the list that it
is given. Call this version dedup mut. The strategy should include mutating
the original list without making a copy of it.
>>> some_list = [" eggplant ", " chicken ", " tomato ", " chicken ",
" television "]
>>> dedup_mut ( some_list )
>>> some_list
[' eggplant ', 'chicken ', 'tomato ', 'television ']
'''

def dedup_mut(xs):
    '''
    sig: string list -> string list
    modifies a string list by removing duplicated elements; iterating backwards
    '''
    k = len(xs)
    for i in range(k - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if xs[i] == xs[j]:
                del xs[i]
    return xs


'''
iterate I backwards !!!
basically, i goes backwards and so does j, but one index ahead of i
and no need to think about the length this way(thinking backwards).
'''


some_list = ["eggplant", "chicken", "tomato", "chicken", "television"]
print(dedup_mut(some_list))


some_list2 = [5 , 10, 20, 10, 90, 20, 20, 20, 4, 3, 5]
print(dedup_mut(some_list2))


'''
a cool way to do it:
return list(set(xs))

'''

