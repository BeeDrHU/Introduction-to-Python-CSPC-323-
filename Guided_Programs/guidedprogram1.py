##########################################
###     Python Guided project 1        ###
###     Updated: 8/31/22               ###
##########################################

###########################################################
# Write a program to prompt the user for hours 
# and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the 
# hourly rate for all hours worked above 40 hours. Use 45 hours and 
# a rate of 10.50 per hour to test the program 
# (the pay should be 498.75). You should use input to read a 
# string and float() to convert the string to a number.
############################################################

############################################################
#           The Recipe
# 1. ask the user for the amount of hours
# 2. ask the user for rate/hr
# 3. make a variable to convert user input to *functional* rate (to do math convert to float)
# 4. make a variable to convert user input to *functional* hours (to do math convert to float)
# 5. if/else for calculating hours over 40
# 6. calculate regular pay
# 7. calculate overtime pay
# 8. print results

hrs= input("Please enter your hours.")

rate= input("Please enter your pay rate.")

h= float(hrs)

r= float(rate)

if h > 40:
    OTR= r*1.5
    OTH= h-40
    OT= OTH * OTR
    h=40
else:
    OT= 0

reg= h*r

pay= reg + OT

print(pay)

