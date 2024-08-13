# Homework 4: Flow Control If and While 
# Jacqueline Soloveychik 
# COMP 112 
# Prof. Thayer

# Problem 1
'''
(20 points) Write a function named abs_val that takes a parameter of type int,
which may be positive, zero, or negative. This function should return the
absolute value of its parameter.  In math, the absolute value function always
returns the positive value of the input number.  For example abs(1)=1,
abs(-1)=1, abs(-2)=2, abs(2)=2, abs(-19904)=19904 and so on. Also abs(0)=0
Your function should use conditionals and arithmetic to get its result. You
may not use Python's math functions. Write a program that uses your function
to print the absolute value for the following inputs: 23, 0, -12, -38813,
100000. The function should return these respective values: 23, 0, 12,
38813, 100000.
'''

def abs_val(x):

    # checking if x is a positive integer
    if x == 0 or x > 0:
        return x
    else:
        return -x
    
abs_val(23)
abs_val(0)
'''
abs_val(23)
returns: 23

abs_val(0)
returns: 0

abs_val(-12)
returns: 12

abs_val(-38813)
returns: 38813

abs_val(100000)
returns: 100000
'''

# Problem 2
'''
(40 points) Write a function named pyramid that will print out a pyramid whose
base is n characters wide. A precondition is that n is positive and odd. For
example, pyramid(5) should give this: [] pyramid(15) should give this: []

Using your pyramid function, write a program that will print out pyramids
of size 5, 15, and 25.
'''

def pyramid(n):

    # checks to see if n is a positive integer greater than 0 and canot evenly
    # be divided by 2 (odd number)
    if n > 0 and n/2!=0:

        # x loops through values 1 through half of n plus 2 
        for x in range(1, int(n/2 + 2)):

            # the number of spaces is determined by half of n minus x plus 1
            # which is concatenated with the number of '-', determined by
            # 2 times x minus 1
            middle = (int(n/2) - x + 1)*' ' + (2*x-1)*'-'
            print(middle)


pyramid(5)
pyramid(15)
pyramid(25)


# Problem 3
'''
3. (40 points) Write a number-guessing game, wherein the computer picks a number
between 1 and 10 (inclusive), and the user tries to guess it. If the user's
guess is too low or too high, the program will display an appropriate
message. When the user guesses the number correctly, the program will
tell the user how many guesses it took. If the user enters an invalid guess
(for example, something that is not a number), the program will display
an appropriate message and that input will not be counted toward the total
number of guesses.
Here is an example run of your program:

I am thinking of a whole number between 1 and 10
Enter your guess
>>> zsfdsvsa
That's not a valid number!
Enter your guess
>>>5
Your number is too low!
Enter your guess
>>>8
Your number is too high!
Enter your guess
>>>7
You guessed correctly in just 3 moves


Some hints:
Use random.randint to ask Python to provide a random integer.
You need to import random first. For example:
>>> import random
>>> random.randint (1, 10)
7
>>> random.randint (1, 10)
1
Use isdigit to make sure the user enters a valid number. For example:
>>> val = "234"
>>> val. isdigit ()
True
>>> val2 = "234 something "
>>> val2.isdigit ()
False
'''

# number guessing game
import random

def random_game():

    # random number is assigned
    random_number = random.randint(1,10)

    # counter for number of attempts from user 
    trialcount = 0
    print ('I am thinking of a whole number between 1 and 10')

    # loop until correct answer is guessed 
    while(True):

        # user enters an answer
        user_input = input('Enter your guess\n')
        guess = user_input
        
        # determines if the given input is a valid digit 
        if guess.isdigit():

            # converts guess to type int in order to do conditional operators
            guess = int(guess)

            # checks to see if guess is within range
            if guess  >= 0 and guess <= 10:

                # checks if guess is greater than the random number  
                if guess < random_number:
                    print ('Your number is too low!')
                    trialcount +=1

                # checks if guess is greater than the random number   
                elif guess > random_number:
                    print ('Your number is too high!')
                    trialcount +=1

               # checks if value aligns with the random number and loop breaks      
                elif guess == random_number:
                    trialcount +=1
                    print ('You guessed correctly in just ' + str(trialcount) + ' moves!')
                    break
            else:
                    print('Thats not a valid number!')
        else:
            print('Thats not a valid number!')

# function call       
random_game()
