##########################################
### Create a Hangman game from scratch ###
### Updated 9/14/22                    ###
##########################################

#############################################################
## Problem:  Figure out how to make hangman from scratch.  ##
## Recipe:                                                 ##
## 1. import need modules/libraries
## 2. create hangman drawing function
## 3. add in the word library
#  4. create the "guessing spaces"
## 7. add in correctly guessed letters to bank and total guesses
## 5. create variables for correct or incorrect responses
## 6. start putting in input to interact with user
## 8. code for game completion both wins & losses
## 9. possible loop to restart code/ restart option
#############################################################

import random
from turtle import goto

def draw(progress):
    if progress==0:
        print('No hanged parts yet! Good Luck!')
        return
    for i in range(0, progress):
        if i == 0:
            print(" O")
        elif i ==1 and progress == 2:
            print( '|')
        elif i == 2 and progress ==3:
            print('/|')
        elif i == 3 and progress == 4:
            print('/|\\')
        elif i == 4 and progress == 5:
            print('/')
            print("Yikes!")
        elif i == 5 and progress == 6:
            print('/ \\')
    return

category= random.choice(["color", "language", "animal", "names"])
print("Category: " + category)

if category == "color":
    word= random.choice(["pink", "yellow", "blue", "red", "tangerine", "magenta", "royal blue"])
elif category == "language":
    word= random.choice(["english", "spanish", "portugeuse", "yakama", "german"])
elif category == "animal":
    word= random.choice (["dog", "cat", "elephant", "snake", "eagle", "black bear"])
else:
    word= random.choice (["paul", "evelyn", "anna", "bethany", "colton", "juan", "josue", "mayra", "robert"])

def play():
    word_progress= ["-"] * len(word)
    guessed= []
    incorrect= 0

    while incorrect< 6 and "-" in word_progress:
        print()
        draw(incorrect)
        print("".join(word_progress))
        print("Guessed Letters: ")
        print("".join(guessed))
        print()

        guess= "0"
        if not guess.isalpha():
            guess= input("Guess a letter or word: ").lower()

        if guess==word.lower():
            break
        elif len(guess)> 1:
            print("Sorry, that's wrong.")
            incorrect+= 1
        elif guess in guessed: 
            print("You've already guessed that letter.")
        elif guess not in word.lower():
            print(guess + "is not in the word.")
            incorrect +=1
            guessed.append(guess)
        else:
            print(guess + "is the word!")
            guessed.append(guess)
            for i in range(len(word)):
                if word_progress[i] == "-" and word[i].lower() == guess:
                    word_progress[i] = word[i]

    print()

    if incorrect == 6:
        print("Haha, you lost!")
        print("The word was: " + word)
    else:
        if "-" in word_progress:
            print("You guessed the word! You win!")
            for i in range(len(word)):
                word_progress[i] = word[i]
        else:
            print("You found the word! Congratulations!")


    draw(incorrect)
    print(" ".join(word))
    print("Guessed Letters: ")
    print(" ".join(guessed))
    print()

def gameplay():
    while True:
        answer= input("Would you like to play a game?")
        if answer=="yes":
            play()
        elif answer== "no":
            print('Cya next time!')
            break
        else:
            print("I don't know what you mean.")
