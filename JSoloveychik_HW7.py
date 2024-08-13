# Jacqueline Soloveychik
# Homework 7: Dictionary
# 11/3/23

# Question 1
'''
Consider the following dict, which provides a mapping of commonly misspelled
words to their correct spelling.

respellings = {
"teh": "the",
"relevent": "relevant",
"lite": "light",
"lol": "haha",
}

Write a function respell, which takes a str argument and returns a string
with the spelling corrected according to the content of the dict. Your solution
must reference the respellings dictionary as its source of information.
>>> respell ("I ate teh whole thing lol ")
'I ate the whole thing haha'

Hint: use the split function to convert the input string into a list of words:
>>> s = "word0 word1 word2"
>>> s.split()
['word0', 'word1', 'word2']
'''


respellings = {
"teh": "the",
"relevent": "relevant",
"lite": "light",
"lol": "haha",
}

def respell(sentence):
    '''
    sig: str -> str
    desc: takes a str argument and returns a string with the spelling
    corrected according to the content of the dict
    '''
    senlist = sentence.split()
    for i in range(len(senlist)):
        if senlist[i] in respellings:
             senlist[i] = respellings[senlist[i]]
    return " ".join(senlist)
    
print(respell("I ate teh whole thing lol "))


# Question 2
'''
Write a function wordpositions that returns a dict that maps each word
found in the input text into a list of its positions within the text,
according to word number (starting at 0). For example, in the following
execution, the word "he" is a key in the returned dict, and its value
is [0, 5] because that word appears twice in the input text: at position
0 and at position 5.

>>> wordpositions ("he thought a thought that he thought he'd never think")
{'he ': [0, 5], 'think ': [9] , 'thought ': [1, 3, 6], 'that ': [4] ,'a ':
[2] , 'never ': [8] , "he'd": [7]}
'''

def wordpositions(s):
    '''
    sig: str -> dict
    desc: returns a dict that maps each word found in the input text into a
    list of its positions within the text,according to word number
    '''
    sen = s.split()
    newdict = {}
    for i in range(len(sen)):
        if sen[i] not in newdict:
             newdict[sen[i]] = [i]
        else:
            newdict[sen[i]] += [i]
    return newdict


print(wordpositions("he thought a thought that he thought he'd never think"))



# Question 3
"""
Using your wordpositions function, write a function that returns the
most common word in the input text.

>>> most_common ("he thought a thought that he thought he'd never think")
'thought '
"""
def most_common(dictinput):
    '''
    sig: str -> str
    desc: returns the most common word in the input text using wordpositions
    function; has greatestval acc that gets overwritten if the length of the
    dicctionary value at i is greater than greatestval + records the key into
    mostcommonw
    '''
    greatestval = 0
    dictionary = wordpositions(dictinput)
    for i in dictionary:
        if len(dictionary[i]) > greatestval:
            greatestval = len(dictionary[i])
            mostcommonw = i
    return mostcommonw, greatestval

print(most_common("he thought a thought that he thought he'd never think"))


# Question 4
'''
In the building where I work, every office has a phone, and every phone has
a unique number. If you know a person's phone number, you can call them.
For example, my phone number is 53. However, today, my office is being
painted, so I'm going to work in Vivian's office. Her phone number is 97.
I'm going to forward my phone number to hers, so that if anyone calls me on
my phone number, it will ring in her office (where I will be). Meanwhile,
her phone number will continue to work as usual. We can represent
the situation using a dict:

forwards = {53: 97}

The forwards dictionary stores all of the current numbers that are
being forwarded. The key shows that number that is being forwarded, and
the value shows the number that it is being forwarded to. However, it
turns out that Vivian's office is also being painted today, so we're
both going to work in Bob's office, who has phone number 24. If we forward
Vivian's phone number to Bob's, we ensure that both I and Vivian can get
calls in Bob's office. Our updated forwards dictionary looks like this:

forwards = {53: 97, 97: 24}


Now, dialing the number 53, 97, or 24 will cause Bob's phone to ring.

(a) Write a function resolve_phone_number. It takes two parameters: a
dict of forwardings, and a phone number that I dial. It should return the
phone number of the phone where my call will actually ring. If the requested
phone number isn't in the forwards dictionary, you can assume
that the number isn't being forwarded and that the dialed phone will ring.
>>> forwards = {53: 97, 97: 24}
>>> resolve_phone_number ( forwards , 53)
24
>>> resolve_phone_number ( forwards , 97)
24
>>> resolve_phone_number ( forwards , 99)
99
>>> resolve_phone_number ({1:2 , 2:3 , 3:4 , 4:5 , 5:6} , 2)
6
As you can see in the final example above, your function should be able to
handle arbitrarily long chains of forwardings.
'''

forwards = {53: 97, 97: 24}

def resolve_phone_number(forwardings, phonenum):
    '''
    sig: dict,int -> int
    description: returns the phone number of the phone where call will
    actually ring; loops through forwardings and checks if the phonenum is in
    forwardings; overwrites it and keeps it looping through into desired phonenum
    '''
    for i in forwardings:
        if phonenum in forwardings:
            phonenum = forwardings[phonenum]
    return phonenum


print(resolve_phone_number(forwards , 53))
print(resolve_phone_number(forwards , 97))
print(resolve_phone_number(forwards , 99))
print(resolve_phone_number({1:2 , 2:3 , 3:4 , 4:5 , 5:6} , 2))


'''
(b) Consider the following forwardings:
forwards = {53: 97, 97: 24, 24: 53, 62: 63}
Notice that Bob has forwarded his number back to my phone, which is forwarded
to Vivian's phone, which is forwarded to Bob's phone. It's a circular
reference! This situation is not acceptable. Modify your resolve_phone_number
function into a function called resolve_phone_number2 so that it will detect
this situation and return the string "circular" when a circular reference
happens while looking up the given phone number. Non-circular lookups should
behave normally.
>>> forwards = {53: 97, 97: 24, 24: 53, 62: 63}
>>> resolve_phone_number2 ( forwards , 99)
99
>>> resolve_phone_number2 ( forwards , 62)
63
>>> resolve_phone_number2 ( forwards , 24)
"circular"
>>> resolve_phone_number2 ( forwards , 53)
"circular"
'''

forwards = {53: 97, 97: 24, 24: 53, 62: 63}

def resolve_phone_number2(forwards, phonenum):
    '''
    sig: dict,int -> str or int
    description: checks for circular loops and breaks; loops through forwards,
    FIRST checks if phonenum is in forwards, and only then goes in to overwriting
    phonenum (like in last function), and records it into seen acc (to avoid the
    looping); if phonenum was seen, returns 'circular' 
    '''
    seen = []
    for i in forwards:
        if phonenum in forwards:
            if phonenum not in seen:
                phonenum = forwards[phonenum]
                seen.append(phonenum)
            else:
                return "circular"
    return phonenum

print(resolve_phone_number2(forwards , 99))
print(resolve_phone_number2(forwards , 62))
print(resolve_phone_number2(forwards , 24))
print(resolve_phone_number2(forwards , 53))







