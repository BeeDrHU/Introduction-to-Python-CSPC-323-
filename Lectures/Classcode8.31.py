##########################################
###     Conditional Execution          ###
###     Updated: 8/31/22               ###
##########################################

#####################
### Boolean Expressions
#####################

5==5

5==6

type(True)

type(False)

x=7

y= 39

x != y

x>y

x<y

x is y

x is not y

#####################
### Logicl Operators
#####################

x > 0 and x< 10

not x > y

#####################
### Conditional Execution
#####################

if x > 0:
    print("x is positive")

#####################
### Alternative Execution
#####################

if x//2==0:
    print('x is even')
else:
    print('x is odd')

#####################
### Chained Execution
#####################

if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x and y are equal')

x=14
y=9

if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
elif x==y:
    print('x and y are equal')

#####################
### Nested Conditionals
#####################

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

#####################
### Alternatives to Nested
#####################

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < y:
    if y < 10:
        print('y is a positive single-digit number.')

#####################
### Watching for Exceptions
#####################

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')