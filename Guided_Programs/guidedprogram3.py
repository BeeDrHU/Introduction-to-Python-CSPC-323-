################################
### Guided Program 3         ###
### Updated: 9/12/22         ###
################################

#####################################
# Problem:
# Write a for loop to print everyones name in our class
# Recipe: 
# 1. create l,ist of names
# 2. start writing the for loop
# 3. write the print statement in the for loop
#####################################

lst= ['Anna', "Josue", 'Mayra', 'Juan', 'Evelyn', 'Colton', 'Bethany', 'Robert', 'Paul']

for x in lst:
    print(x)

#####################################
# Problem: "Butterfinger"
# Write code so that a counter variable is increased by one
# each time the loop iterates over a letter in the string. 
# Print the result.
# Recipe:
# 1. write the code for our string 
# 2. set counter to zero
# 3. start the for loop
# 4. write code for increasing the counter
# 5. print the final count
#####################################

s= "Butterfinger"
c= 0

for i in s:
    c= c +1
print(c)

##################################
# Problem:
# Write some code to print 0-15 in reverse (start with 15 and end with 0)
# Recipe:
# 1. counter= 15
# 2. start while loop
# 3. display the counter value
# 4. decrease the value of the counter
###################################

c= 15

while c>=0:
    print(c)
    c= c-1
print("Blastoff!")