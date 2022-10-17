##########################################
###     Tuples                         ###
###     Updated: 10/17/22               ###
##########################################

######################
### What is a tuple?
#####################

#Tuple is a sequence of values, similar to list
#Can store any type of value, which are indexed by integer

#Tuples are immutable, unlike lists

#Tuples are comparable and hashable so we can sort lists of them and
#use tuples as key values in Python dictionaries

#Syntax: tuple is comma-seperated list of values:
t= ('a', 'b', 'c', 'd', 'e')

#to create a tuple with only 1 element, u have to inlcude a final comma
t1= ('a',)
type(t1)

t2= ('a')
type(t2)

#built-in tuple function
t= tuple()
print(t)

#if you input a sequence like a list or string, tuple breaks it into
#the individual elements of the sequence

t=tuple('lupins')
print(t)

#most list operations work on tuples
t= ('a', 'b', 'c', 'd', 'e')

#bracket operator
print(t[0])

#slice operator
print(t[1:3])

#can't modify elements of tuple
t[0]= "A"

#can replace one element with another
t= ('A',) + t[1:]
print(t)

######################
### Comparing Tuples
#####################

(0,1,2) < (0,3,4)

(0,1,2000000) < (0,3,4)

#sorting function for tuples
#works upsing DSU pattern
    #decorate= sequence building a list of tuples with one or more
        #sort keys preceding the elements from the sequence
    #sort= list of tuples using python buil-in sort
    #undecorate= extracting the sorted elements of the sequence.

#example sort: first loop builds list of tuples by length, second
    #traverses list and builds list of words in descending order
txt= 'but soft what light in yonder window breaks'
words= txt.split()
t=list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)

res=list()
for length, word in t:
    res.append(word)
print(res)

######################
### Tuple Assignment
#####################

#you can assign a tuple as the left side assignment statment
m=['have', 'fun']

x, y=m

#tuple variable assignment essentially works by:
m=['have', 'fun']
x=m[0]
y=m[1]
x
y

#you can include parentheses if you like, but not necessary

#realistic example to split a sequence, i.e, email parsing
add= "monty@python.org"
uname, domain= add.split('@')

print(uname)
print(domain)

######################
### Dictionaries and Tuples
#####################

#dictionaries are programmed basically as tuples (key-value pairs)
#the dictionary can convert to a list of "items", aka tuples, 
    #that represent the key-value pairs

d= {'a':10, 'b':1, 'c':22}
t= list(d.items())
print(t)

#by doing this we can now sort the list and make
    #comparisons to other tuples
d= {'a':10, 'b':1, 'c':22}
t= list(d.items())
print(t)

t.sort()
print(t)

######################
### Multiple Assignment w/ Dictionaries
#####################

#create for loop to sort contents of dictionary into key-value pairs
d= {'a':10, 'b':1, 'c':22}
l= list()
for key, val in d.items():
    l.append((val, key))

l
l.sort(reverse=True)
l

######################
### Finding the most common words in txt file
#####################

#create a dict of the words and times shown in file
from msilib.schema import Directory
import numbers
import string
fhand=open('romeo-full.txt')
counts= dict()
for line in fhand:
    line= line.translate(str.maketrans('', '', string.punctuation))
    line= line.lower()
    words= line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

#sort dict by value
lst=list()
for key, val in list(counts.items()):
    lst.append(val, key)

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)

