import os
import sys
import random


# Simple hangman game
# Tanner Zinck			September 16, 2015


print("======================================")
print("_____________HANG EM HIGH_____________")
print("======================================")

print("The Vigilantes are gonna hang ya without battin' an eye, ")
print("They think you're wranglin stolen cattle!")
print("You best start guessing what word them is thinking of real quick!")
print("\n")

wordsList = []

with open('words.txt', "r") as words:
	wordsList = list(words.read().split(' '))

position = random.randrange(0, len(wordsList))
theWord = wordsList[position]

print("The Vigilantes are ready to start shootin ya!")

displayString = ''
for i in range(len(theWord)):
	displayString += '_'
	displayString += ' '

print('' + displayString)

guessedLetters = ''

while(True):
	print("Make a damn guess!")
	guess = input()
	if guess in guessedLetters.split(' '):
		print("You goofed up! The Vigilantes put a bullet between your eyes!")
		print("It's all over.......")
		sys.exit()
	else:
		guessedLetters += guess
		


