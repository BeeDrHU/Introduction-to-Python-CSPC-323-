##########################################
###     Strings and Files              ###
###     Updated: 9/19/22               ###
##########################################

######################
### what is a string
######################

fruit = 'banana'
letter = fruit[1]

print(letter)

letter = fruit[0]
print(letter)

letter = fruit[1.5]

######################
### Working with str
######################

len(fruit)

length= len(fruit)
last= fruit[length]

last= fruit[length-1]
print(last)

### traversing
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for char in fruit:
    print(char)

### slicing
s = 'Monty Python'
print(s[0:5])

print(s[6:])

fruit = 'banana'
fruit[:3]
fruit[3:]

######################
### Strings are immutable
######################

greeting = 'Hello, world!'
greeting[0] = 'J'

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

type(new_greeting)

######################
### Looping
######################

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


######################
### in operator
######################

'a' in 'banana'

'seed' in 'banana'

'banana' in "there are seeds in bananas"
######################
### String comparison
######################

word= 'pineapple'

### designed to check for the alphabetical comparison to banana
if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

######################
### string methods
######################

stuff= 'Hello world!'

type(stuff)

dir(stuff)

help(str.capitalize)

help(str.rsplit)

######################
### Parsing Strings
######################

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

######################
### Opening files
######################

fhand = open('mbox.txt')
print(fhand)

######################
### text file and lines
######################

stuff= "Hello\nworld"
stuff

print(stuff)

len(stuff)

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