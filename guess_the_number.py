#Guess the number game!

import random
correctNumber = random.randint(1, 50)

print("Pick a number between 1 and 50.")

userGuess = input("My guess is: ")
intGuess = int(userGuess)

#Python automatically converts user input to a str, convert to int
#Check to make sure the user input is an integar
    
while intGuess != correctNumber:
    try:
        if intGuess > 50 or intGuess < 0:
            print("You must pick a number between 0 and 50! Try again.")
            intGuess = int(input("My new guess is: "))
        elif intGuess > correctNumber:
            print("Too high! Try again.")
            intGuess = int(input("My new guess is: "))
        elif intGuess < correctNumber:
            print("Too low! Try again.")
            intGuess = int(input("My new guess is: "))
    except ValueError:
        print("I asked for a number, you dingus! Try again!")
        intGuess = int(input("My new guess is: "))

if intGuess == correctNumber:
    print("You did it! You guessed the correct number: ", correctNumber)