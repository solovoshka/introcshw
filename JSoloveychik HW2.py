# Jackie Soloveychik
# Homework 2: Expressions, Variables, and Programs
# COMP 112
# Prof. Thayer

# Problem 1. (24 points total, 4 points per part)
'''
Predict what Python will return. Then,
try it out in the Python interpreter and paste the actual answers.
(The response to this problem will be a comment and should include
the predicted and Python produced response.)

7 % 3
Prediction: 1
Actual: 1

7 // 3
Prediction: 2
Actual: 2

7.0 / 3.0
Prediction: 2.33...
Actual: 2.3333333333333335

7 * 3 < 10 * 2
Prediction: false
Actual: False

'wes' + 'leyan'
Prediction: 'wesleyan'
Actual:

'hi' + 'there' == 'hi there'
Prediction: false
Actual: False
'''


# Problem 2. (32 points total, 4 points per part)
"""
Replace the ? with an operator from the list in order to make the
expression evaluate to True. Please rewrite the complete expression as
valid Python code that evaluates to True.

Operators: (+, -, *, **, %, //, /, > <, and, or, not).

9 > 4
>>> 9 > 4
True

not (9<4)
>>> not (9<4)
True
    
(9<4) or (9>4)
>>> (9<4) or (9>4)
True

9 // 4 == 2
>>> 9 // 4 == 2
True

9 % 4 == 1
>>> 9 % 4 == 1
True

2 ** 3 == 8
>>> 2 ** 3 == 8
True

not (True and False)
>>> not (True and False)
True

'oo' + (2 * 'la') == 'oolala'
>>> 'oo' + (2 * 'la') == 'oolala'
True
 """

# Problem 3.  (44 points total)
"""
(The response to this question should be valid executable Python code.)
The volume of a cylinder is given by the equation 
V=πr2h 
where
	V = volume
	r = radius
	h = height
	π = 3.14


A typical soda can has a radius of 1.3 inches and a height of 4.83 inches.

    a. Write Python assignment statements for the variables radius and height,
    referring to the dimensions of a soda can. (10 points)
    
    b. Write a Python assignment statement for the variable pi, referring to the
    approximation noted above. (10 points)
    
    c. Write a Python expression for the volume of a soda can, assuming it is a
    perfect cylinder, in cubic inches.  Note that this expression should contain
    only variables, specifically the ones defined in the steps above. (12 points)
    
    d. Write a statement that will display the volume of the can when your script
    file is run. The output should be formatted as follows: (12 points)
    Volume of a soda can in cubic inches: <volume>
"""


# a. variable assignments 

r  = 1.3
h = 4.83

# b. pi assignment statement 
π = 3.14

# c. expression for volume of a soda can 
soda_can_Vol = π * r * 2 * h

# d. print statement strings together text from end statement and
# result of can volume; use str method on soda_can_Vol method in order to concatenate
# in Python'''
print ('Volume of a soda can in cubic inches: ' + str(soda_can_Vol))






















