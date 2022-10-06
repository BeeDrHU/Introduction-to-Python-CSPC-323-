##########################################
###     Dictionaries                   ###
###     Updated: 10/03/22              ###
##########################################

######################
### What's a dictionary?
######################

#A generalized list, but in a dictionary the indices can be almost any
#type not just integers.
# 
#Dictionary consists of indices= Keys and a set of values that maps to
#each key.
#
#Example: english to spanish dictionary

eng2sp= dict()

print(eng2sp)

#curly brackets represent the empty dictionary. Use square brackets to
#add to the dictionary.

eng2sp["one"]= 'uno'

print(eng2sp)

#We can use a different notation as an input format

eng2sp= {'one': 'uno', 'two':'dos', 'three': 'tres'}

print(eng2sp)

#Notice that the order of the dictionary changes. This is unpredictable.
#Important part is that the key-value pairs are unchanged.

print(eng2sp['two'])

#can use same methods/functions on this data type as others.

len(eng2sp)

'one' in eng2sp

'dos' in eng2sp

######################
### Dictionary as a counter
######################

#There are a million ways to do the same thing with coding.
#Reminder: we're at the intersection of knowledge, problem solving, and
#coding. The computer only knows what you tell it.

#Implementation: different ways to perform the same calculation. 
#*try to be efficient to save memory*

#make a counter for a word; counts every letter occurence
#(frequency histogram)

word= 'brontosaurus'
d= dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]= d[c] +1
print(d)

#another one

word= 'dictionary'
d= dict()
for c in word:
    if c not in d:
        d[c]=1
    else:
        d[c]= d[c] +1
print(d)

#using the get method: built-in 

counts= {'evelyn':7, 'anna': 4, 'juan': 5, 'robert': 12, 'mayra':40}

print(counts.get('evelyn'))

print(counts.get('mayra', 0))

print(counts.get('Paul', 0))

#using gets to make loop more computationally efficient

word= "brontosaurus"
d= dict()
for c in word:
    d[c]= d.get(c, 0) +1
print(d)

######################
### Dictionaries and Files
######################

#count the occurence of words in a file of text
#Logic
#1. open file
#2. break each line into a list of words
#3. loop through each word in line and count for dict

fname= input('Enter the file name: ')
try:
    fhand= open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
counts= dict()
for line in fhand:
    words= line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word] +=1 #counts[word]= counts[word] +1
print(counts)

######################
### Looping and Dictionaries
######################

#for loop to traverse keys in dictionary

counts= {'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    print(key, counts[key])

#now add in some specifics
counts= {'chuck':1, 'annie':42, 'jan':100}
for key in counts:
    if counts[key]>10:
        print(key, counts[key])

#specify order: print alphabetical
counts= {'chuck':1, 'annie':42, 'jan':100}
lst=list(counts.keys())
print(lst)
lst.sort()
for key in list:
    print(key, counts[key])


######################
### Advanced text parsing
######################

import string

string.punctuation

fname= input('Enter the file name: ')
try:
    fhand= open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
counts= dict()
for line in fhand:
    line= line.rstrip()
    line= line.translate(line.maketrans('', '', string.punctuation))
    line= line.lower
    words= line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word] +=1 #counts[word]= counts[word] +1
print(counts)