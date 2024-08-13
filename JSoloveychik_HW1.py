# Jackie Soloveychik
# September 8, 2021
# COMP112-01


# 1: Recipe

'''
Writing an algorithm.  Algorithms are a set of instructions to follow to
achieve a specific outcome.  In Python, we often write a set of instructions
for the computer to carry out. This is the computer code.  However, algorithms
are not specific to computer programs; recipes are an example of another
algorithm.  The instructions must specify exactly what must be done. Write an
algorithm for making Jello or some other simple food to prepare.(Your response
should detail about 10-12 steps as a comment in your Python script.)

~Brownies~

Step 1: Preheat oven to 335 degrees Farenheit.
Step 2: Take dry mix out of box and open into a bowl.
Step 3: In seperate bowl, whisk together two eggs, 2 tablespoons of water,
        and 1/2 cup of vegetable oil.
Step 4: Combine together wet bowl with dry.
Step 5: Whisk until batter is smooth, thick, but still liquid .
Step 6: Grease baking tray with butter or oil.
Step 7: Line baking tray (3 by 3) with parchment paper.
Step 8: Cook in oven for 35-50 minutes (depending on oven, tray size,
        and mixture consistency".
Step 9: Let cool for 10-15 minutes.
Step 10: Serve with whipped cream, icecream, or toppings of choice. Enjoy.
'''




# 2: GCD ***

'''
Euclid’s Greatest Common Devisor Algorithm
Shown is a flow chart illustrating Euclid’s GCD algorithm to determine the
greatest common devisor between two numbers. Following the flow chart,
compute the GCD of 9 and 6. Write down the steps required to get the GCD.
Keep track of the current  value of the variables A and B in the variable
table by crossing out the value and updating it as the values change as
you work through the chart. A variable table and the steps are started for
you on the next page. 

~ Variable Table ~
A= 9  3  3  3
B= 6  6  3  0


~ Algorithm Trace ~
Steps to get GCD:
Step 1: Input = A, B = 9,6 (given)
Step 2: Is B = 0? No, B = 6. therefore going to step 3
Step 3: Is A > B? Yes, 9 is greater than 6. Therefore going to step 6.
Step 6: Change the value of A to equal the value of A-B; 9-6=3.
Step 7: Go back to step 2
Input = A, B = 3,6
Step 2: Is B = 0? No, B = 6. therefore going to step 3
Step 3: Is A > B? No, 3 is not greater than 6. go to step 4
Step 4: Change the value of B to equal the value of B-A; 6-3=3.
Step 5: Go back to step 2
Input = A, B = 3,3
Step 2: Is B = 0? No, B = 3. therefore going to step 3
Step 3: Is A > B? No, 3 is equal to 3. go to step 4
Step 4: Change the value of B to equal the value of B-A; 3-3=0.
Step 5: Go back to step 2
Input = A, B = 3,0
Step 2: Is B = 0? Yes. go to step 8
Step 8: Print A -> A = 3
print (3)
END
'''




# 3: Imperative Programming Languages **

'''
A. Compare imperative programming  with declarative programming.
How do they work and what are they used for?

> Imperative programming is a a type of way to program computers using
statements, telling the computer how to carry out a task. Declarative
programming refers to a programming that expresses the logic of a
computation withoiut describing its flow. 

B. What are three examples of imperative programming languages and
three examples of declarative programming languages?(You may wish to Google
this.)

> Imperative: Java, C, Python
  Declarative: Lisp, ML, Prolog

C. Why do imperative programming languages require algorithms?

> They require algorithms in order to achieve solutions. This can also make
them much more efficient.
'''



# 4: Parsing *

'''
Parse the following mathematical statements using parentheses to show
order of operation one step per line. Then evaluate the answer. (The
important thing here is not the algebra, but determining what happens next
step by step according to a set of predefined rules.)
'''

'''
example a
2 + 5 * 3  - 7
2 + (5 * 3)  - 7
2 + 15 - 7
(2 + 15) - 7
17 - 7
10
'''


'''
example b
3 * 2**3 / 12
3 * (2**3) / 12
3 * 8 / 12
3 * 8
24 / 12
2
'''


# 5: Printing to Screen

'''
To your script, add some Python code which will print out
the following message.(Feel free to customize with your name, date, and
section.)Note this response should be executable code.
'''

print ('Jackie Soloveychik')
print ('September 8, 2021')
print ('COMP112-01')
print ('')
print ('I <3 Python!')

















