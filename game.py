import os
import sys
import random

NUMGUESSES = 10


# Simple hangman game I started working on after watching the classic Clint Eastwood
# western "Hang Em High"
# Tanner Zinck			September 16, 2015

print("======================================")
print("_____________HANG EM HIGH_____________")
print("======================================")

print("The Vigilantes are gonna hang ya without battin' an eye, ")
print("They think you're wranglin stolen cattle!")
print("You best start guessing what word them is thinking of real quick!")
print("\n")

#create array to hold words from input file
wordsList = []

#wordsList is an array of words from the input text file
with open('words.txt', "r") as words:
	wordsList = list(words.read().split(' '))

#generate a random position, set theWord equal to the word in wordsList at that location,
#theWord is the word that must be guessed
position = random.randrange(0, len(wordsList))
theWord = wordsList[position]

print("The Vigilantes are ready to start shootin ya!")

#create the string to be displayed to the user while guesses are being made
displayString = ''
for i in range(len(theWord)):
	displayString += '_'

#print the display string
print('' + displayString)

#create an array of all the guessed letters
guessedLetters = []

counter = 0

#this is the main game loop
while(True):
	#check if the game has been won
	if displayString == theWord:
		print("You pull out both your double action revolvers, and light them\n")
		print("vigilantes up like a christmas tree. You and your cattle are free...\n")
		print("...And Justice For All")
		sys.exit()	
	if counter > NUMGUESSES:
		print("Too much jaw flappin, not enough proof!\n")
		print("It's all over......")
	
	if counter == 2:
		print("The vigilantes are getting impatient...")

	if counter == 4:
		print("Hurry Up!!")
	
	if counter == 6:
		print("You are mighty brave...")

	if counter == 8:
		print("You be diggin your own grave!!")

	guess = input("Make a damn guess! ")
	print(guess)
	counter = counter + 1

	#if the guessed letter has already been guessed, automatically lose
	if guess in guessedLetters:
		print("You goofed up! The Vigilantes put a bullet between your eyes!")
		print("It's all over.......")
		sys.exit()
	
	#otherwise, add the guessed letter to the list of previous guesses
	else:
		guessedLetters.append(guess)
		#and replace the corresponding spaces in the display string
		displayStringList = list(displayString)
		theWordList = list(theWord)
		for i in range(len(theWordList)):
			if guess == theWordList[i]:
				displayStringList[i] = guess
		
	
			
		displayString = ''.join(displayStringList)
		theWord = ''.join(theWordList)		
		print(displayString)
