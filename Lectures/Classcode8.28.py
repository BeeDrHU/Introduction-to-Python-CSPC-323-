##########################################
###     Basics of python variables     ###
###     expressions, and statements    ###
###     Updated: 8/29/22               ###
##########################################

######################
### Values and type
#####################

### print integer ###

from turtle import distance


4

print(4)

### print string ###

"Hello World!"

print("hello world!")

print('Hello World!')

### check value type ###

type(374)

type('Hello World!')

type(3.2)

type('3.2')

### let's think about big numbers ###

print(1,000,000)

print('1,000,000')

print(1000000)

##################
### Variables
##################

n = 1995

message = "When was Paul born?"

print (message)

print(n)

print(message + n) ###why is this an error?

type(message)

type(n)


clock_17= "12:25pm"

#####################
### Operators
### Reminder: PEMDAS
#####################

20+32

20 + 32

(5+9) * (15-7)

### note: division in python 3.0 requires //

### why does this cause an error? ###

hour-1


#######################
### Expressions
#######################

x = 42

x + 74

meaning= x + 74

print(meaning)

#################
### Strings
#################

first= 10
second= 15
print(first+second)

first_1= "100"
second_1= "150"
print(first_1+second_1)

first_2="dog"
second_2= 11
print(first_2*second_2)

######################
### getting input
######################

inp= input()

print(inp)


name= input('What is your name?\n')

print(name)

###########################
#### practice program #####
###########################
### lets use the speed of a vehicle to
### calculate travel time from yakima to seatac

speed= input("How fast were you driving?\n")

dist= input("How far away were you from seatac?\n")

print("Calculating...\n")

time= int(dist)//int(speed)

time_1=str(time)

remainder= int(dist)%int(speed)

remainder_1= str(remainder)

print(time_1 + "hours and " + remainder_1 + "minutes to get to Seatac")

