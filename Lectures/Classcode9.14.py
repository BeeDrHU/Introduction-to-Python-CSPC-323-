##########################################
###     Iterations                     ###
###     Updated: 9/12/22               ###
##########################################

#######################
### Updating Variable
######################

x= 12

x= x+ 1
print(x)
x= x-1
print(x)

######################
### While Statements
######################

n= 5
while n>0:
    print(n)
    n= n-1
print('Blastoff!')

######################
### Infinite Loops
######################

#n= 10
#while True:
#    print(n, end='')
#    n= n-1
#print('Done!')

while True:
    line= input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

######################
### Finish with continue
######################

while True:
    line= input('>')
    if line [0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

######################
### for loops
######################

friends= ['Joseph', 'Glenn', 'Sally']
print(friends)

for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')

######################
### Loop patterns
######################

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('Count: ', count)

total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print('Total: ', total)

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

