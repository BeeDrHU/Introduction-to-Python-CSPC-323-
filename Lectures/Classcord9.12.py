##########################################
###     Functions                      ###
###     Updated: 9/7/22                ###
##########################################

#####################
###Function Calls
#####################

type(60)

name= input("What is your name?\n")

print(name)
#####################
### Built-In Functions
#####################

dir()

len("string")


range()

print()

#####################
### Conversion
#####################

number= input("tell me your favorite number\n")

number1= int(number)

type(number1)

number2= float(number1)

type(number2)
print(number2)

number3= str(number2)

type(number3)

print(number3)

####################
### Math Functions
####################

import math

degrees= 45

radians= degrees/ 360 * 2 * math.pi

print(radians)

math.sin(radians)

math.sqrt(2)

math.sqrt(2)/2

sq2= math.sqrt(2)

sq2/2

####################
### Random Numbers
####################

import random

for x in range(10):
    x= random.random()
    print(x)

random.randint(5,10)

random.randint(5,150)

t= [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.choice(t)

random.choice(t)

####################
### Create a Function
###################

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

##################
### Function w/ parameter
##################

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice("Paul")

print_twice("spam " *4)

print_twice(math.pi)
