################################
### Guided Program 2         ###
### Updated: 9/7/22          ###
################################

################################
# Problem 1:
# Write a program to ask the user to provide their
# first and last name to the computer. After giving their name,
# have the computer greet them with a "Hello, first name and last name".
# Define a function to do the greeting based on the first and last name.
################################

################################
# Recipe
# 1. Write input what is your first name? What is your last name?
# 2. Define a function called greet
# 3. Function call the greet
################################

first= input('What is your first name?\n')

last= input('What is your last name?\n')

def greet(first, last):
    print('Hello,', first, last )

greet( first, last)

################################
# Problem 2:
# Define a function that turns a lowercase word into uppercase.
################################

################################
# Recipe
# 1. Create input for our string
# 2. Define the function to convert
# 3. Call on new function to convert
################################

def convert():
    print(string.upper())

string= input("what can I help you with?\n")

convert()
