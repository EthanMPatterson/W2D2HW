# Write a program that takes in a user input and prints out how many vowels are in the response
# "Example" -> 3
# "Hello World" -> 3
# "Brian" -> 2
# "This is a longer response" -> 8

# INITIAL THOUGHTS 

#Brute Force option

inputstring = input("Enter a word or phrase to display total vowel count")
x = 0
vcount = 0 
for x in range(len(inputstring)):
    if (
        (inputstring [x] == "a")
        or (inputstring [x] == 'e')
        or (inputstring [x] == 'i')
        or (inputstring [x] == 'o')
        or (inputstring [x] == 'u')
        or (inputstring [x] == 'A')
        or (inputstring [x] == 'E')
        or (inputstring [x] == 'I')
        or (inputstring [x] == 'O')
        or (inputstring [x] == 'U')
    ): 
        count += 1

#Optimized Approach 
inputstring = input("Enter a word or phrase to display total vowel count")

vcount = 0 
vowels = ['a' 'e' 'i' 'o' 'u' 'A' 'E' 'I' 'O' 'U']

for x in range(len(inputstring)):
    if inputstring [x] in vowels:
        vcount += 1
print("There are {count} vowels in your input word/phrase")














# Exercise 2 
#Create a list of names of 4 letters or more and capitalize each name
# Double Bonus* Do it using list comprehension
# Hint: Use help(str) to see methods on string object

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
