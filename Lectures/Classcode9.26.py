##########################################
###     Files Practice and Lists       ###
###     Updated: 9/26/22               ###
##########################################

######################
### Opening files
######################

fhand = open('mbox.txt')
print(fhand)

######################
### Reading Files
######################

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

######################
### searching a file
######################

fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
# Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
# Process our 'interesting' line
print(line)

######################
### User defined name
######################

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

######################
### try, except, open
######################

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

######################
### writing files
######################

fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle,\n"
fout.write(line1)

line2 = 'the emblem of our land.\n'
fout.write(line2)

fout.close()

##################################
##################################
### Chapter 8- LISTS
##################################
##################################


######################
### List as a sequence
######################

## List of integers
ages= [10,14,15,20,20,22,24,26,27]

## List of strings
names= ['Evelyn', 'Juan', 'Anna', 'Paul']

## Different Element Types (nested lists)
project_data= ['science', 2.0, 5, [10,20]]

## Empty List
empty=[]

######################
### Lists are mutable
######################

## Use bracket operator to access an element within a list (same as string)
print(ages[2])

print(names[2])

print(project_data[3])

## Lists can be changes after creation
print(project_data[1])

project_data[1]= 2.75

print(project_data[1])

## In operator

"Paul" in names

"Josue" in names

######################
### Traverse a list
######################

#common practice is to use a for loop *remember this reads everything

for name in names:
    print(names)

#traversing to update a list

for age in ages:
    ages[1]= 17
print(ages)

#nested lists only count as a single element
print(project_data)

len(project_data)

######################
### List Operators
######################

#concatenating strings with +
a= [1,2,3]

b= [4,5,6]

c= a+b

print(c)

# multiply/repeat elements with *
[0]*4

[1,2,3]*3

a*3

######################
### List Slices
######################

#same syntax as we practiced for strings

t= [1,2,4,5,7,9,8,12]

t[1:3]

t[:4]

t[4:]

t[:]

#updating a list with splice operator
t[1:3]= [14,27]

print(t)

t[3:5]= ["Paul", "Colton"]

print(t)

######################
### List methods
######################

#append- add a new element to a list at the end
x= ['a','b','c']
x.append('d')

print(x)

#extend- takes existing list as an argument and appends all lists to 2nd
x1= ['a','b','c']
x2= ['d','e','f']

x1.extend(x2)

print(x1)

#sort- arranges from low to high
print(ages)

ages.sort()

print(ages)

#doesn't work this way
ages= ages.sort()

######################
### Deleting Elements
######################

print(x)

#use pop to delete element based on index
x3= x.pop(1)

print(x)

print(x3)

x4= x.pop()

#complete deletion of an element
x= ['a','b','c']
del x[1]

print(x)

#remove a specific element
x= ['a','b','c']
x.remove("b")

print(x)

#using del to remove multiple elements
x= ['a','b','c']
del x[1:]

print(x)

######################
### Lists and Functions
######################

nums= [3,41,12,9,74,15]

print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

print(sum(nums)/len(nums))

#program to calculate average with a list
numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

#######################
### Lists and Strings
######################

#string= sequence of characters, list= sequence of values

#convert string to list
    #breaks string into individual elements
s= "spam"

t=list(s)

print(t)

#split method to break words into list elements
s= "Paul was here"
t=s.split()

print(t)

#split with delimiter
s="spam-spam-spam"
delimiter='-'
s.split(delimiter)

#joining a list to a string
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
delimiter.join(t)
