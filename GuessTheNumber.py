#!/usr/bin/python
import random

min = 1
max = 100
guessedNr = 0;
correctNr = random.randint(min, max);

guessedNr = raw_input("Guess a number between " + str(min) + " and " + str(max)
+ ": ")

while int(guessedNr) != correctNr :
    if int(guessedNr) < correctNr :
        guessedNr = raw_input("Wrong! Searched number is greater than " +
        str(guessedNr) + ". Please try again: ")
    elif int(guessedNr) > correctNr :
        guessedNr = raw_input("Wrong! Searched number is smaller than " +
        str(guessedNr) + ". Please try again: ")

print("\n\nYou guessed the correct number (" + str(correctNr) +
")\n\nCongratulations!\n\n")
