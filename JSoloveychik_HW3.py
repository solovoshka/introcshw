# Homework 3: Functions
# Jacqueline Soloveychik 
# COMP 112 
# Prof. Thayer

# Problem 1.
'''
Consider the following program.
Without using your computer, determine
its output. Then use Python to check your guess. To turn in, write
your guess as a comment, and then illustrate the execution of
the code below. (20 points)
'''

def thriceplusone (x):
    return (x * 3) + 1

def isdifferencesmall (a, b):
    diff = a - b
    sqr = diff * diff
    return sqr < 10

print (thriceplusone (10))
print (thriceplusone ( thriceplusone (3)))
print (isdifferencesmall ( thriceplusone (1) , thriceplusone (2)))
print (isdifferencesmall ( thriceplusone (5) , thriceplusone (10)))


'''
Prediction:
31
31
9 < 10
14 x 14 < 10


Output:
31
31
True
False
'''


# Problem 2.
'''
Using the following functions, write a program to print out the image
below. Your program may call the following functions, but it may not call
the print function directly. (30 points)

def top ( position ):
print ( position * " " + "^")
def middle ( position , width ):
print ( position * " " + "/" + width * " " + "\\")
def bottom ( position , width ):
print ( position * " " + width * "-")
Your program should produce the following image:
'''


def top ( position ):
    print ( position * " " + "^")
    
def middle ( position , width ):
    print ( position * " " + "/" + width * " " + "\\")
    
def bottom ( position , width ):
    print ( position * " " + width * "-")

# variable assignments
top_position = 6

middle_position1 = 4
middle_position2 = 3
middle_position3 = 2
middle_position4 = 1

middle_width1 = 3
middle_width2 = 5
middle_width3 = 7
middle_width4 = 9

bottom_position = 0
bottom_width = 13

# function calls 
top(top_position)
middle(middle_position1, middle_width1)
middle(middle_position2, middle_width2)
middle(middle_position3, middle_width3)
middle(middle_position4, middle_width4)
bottom(bottom_position, bottom_width)




# Problem 3.
'''
(50 points, 10 points per part) The surface area of a cylinder is given by:

A = 2pirh+2pir^2

where A = surface area
r = radius
h = height

In other words, the surface area of a cylinder consists of the area of a
rectangle of height h and of width the circle's circumference, plus the area
of the circular top and bottom parts of radius r, as suggested by the figure.


(a) Define a global variable named pi which contains an approximate value of
π as a float.

(b) Write a function named sqr, which takes a parameter x (of type float)
and returns its square. (Please do not use Python’s Math module but instead
write your own function.)

(c) Write a function named circle_area which takes a parameter r
(of type float) and returns the area of a circle of radius r. This function
should use your function sqr and your pi variable.

(d) Write a function named cylinder_side_area which takes parameters r and
h (both of type float) and returns the surface area of the sides of a
cylinder of height h and radius r (i.e. the rectangular part in the above
diagram). This function should use your pi variable.

(e) Write a function named cylinder surface area which takes parameters r
and h (both of type float) and returns the surface area of a cylinder of
height h and radius r. This function should call cylinder side area and
circle area.
'''


# part a
'''
define global variable named pi
'''
pi = 3.14

# part b:
'''
function definition of sqr, which takes a float paramter x and returns its
square
'''

def sqr(x):
    square = x**2
    return square

# part c
'''
function definition that takes a float parameter r and returns the area of a
circle with radius r; it incorporates function sqr and the global pi variable
'''

def circle_area(r):
    area = pi * sqr(r)
    return area
    
# part d
'''
function definition that takes two paramaters (r and h) of type float and
returns the surface area of the sides of a cylinder of height h and radius r
'''

def cylinder_side_area(r, h):
    surface_area = 2 * pi * r * h
    return surface_area

# part e
'''
function definition of cylinder_surface_area, which takes parameters r
and h (both of type float) and returns the surface area of a cylinder of
height h and radius r
'''
def cylinder_surface_area(r, h):
    a = 2 * circle_area(r)
    b = cylinder_side_area(r,h)
    return a + b


# test
'''
returns: 12.56
actual: 12.56
'''
print(cylinder_surface_area(1.0, 1.0))

'''
returns: 50.24
actual: 50.24 (yay)
'''
print(cylinder_surface_area(2.0, 2.0))

'''
returns: 251.2
actual: 251.2
'''
print(cylinder_surface_area(5.0, 3.0))











