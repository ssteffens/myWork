# This program promts the user to guess a number. The program keeps prompting to guess the number
# until the user gets the right number.
# Author: Stefanie Steffens

numberToGuess = 15

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! The correct number was", numberToGuess)