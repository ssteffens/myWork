# This program creates a random number and prompts the user to guess it. The program keeps prompting to guess the number
# until the user gets the right number. After each guess, the program tells the user whether the guess 
# was too high or too low.
# Author: Stefanie Steffens

import random

numberToGuess = random.randint(1,10)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else: print("Too high")
    guess = int(input("Please guess again:"))

print ("Well done! The correct number was", numberToGuess)