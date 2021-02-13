# This program promts the user to guess a number. The program keeps prompting to guess the number
# until the user gets the right number. After each guess, the program tells the user whether the guess 
# was too high or too low.
# Author: Stefanie Steffens

numberToGuess = 47

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else: print("Too high")
    guess = int(input("Please guess again:"))

print ("Well done! The correct number was", numberToGuess)