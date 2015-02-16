# Petals around the rose game
import random

def rollDice():
#Rolls 5 dice using the random function and stores the values
	arDice = []
	for i in range(6):
		arDice.append(int(random.random()*6 + 1))
	return arDice

def prDice(dice):
	for i in dice:
		if i == 1:
			print("---------\n|       |\n|   *   |\n|       |\n---------")
		elif i == 2:
			print("---------\n|*      |\n|       |\n|      *|\n---------")
		elif i == 3:
			print("---------\n|*      |\n|   *   |\n|      *|\n---------")
		elif i == 4:
			print("---------\n|*     *|\n|       |\n|*     *|\n---------")
		elif i == 5:
			print("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
		else:
			print("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

def answer(dice):
	ans = 0
	for i in dice:
		if i == 3:
			ans += 2
		elif i == 5:
			ans += 4
	return ans
		
#What round it is at
rnd = 1
wins = 0
loses = 0
#Consecutive wins
consWins = 0





print("Petals around the rose. There are three rules:")
print("1. The name of the game is important \n2. The answer is always even \n3. If you figure it out, do not let anyone else know")

while True:
	print("Here is the Round " + str(rnd) + " :")

	dice = rollDice()
	prDice(dice)
	answers = answer(dice)

	print("")
	guess = input("What is your guess?: ")

	while guess.isdigit() is False:
		guess = input('Please enter a number: ')

	guess = int(guess)

	if guess == answers:
		print("Hooray!")
		wins += 1
		consWins += 1
	else:
		print("Sorry that's wrong")
		print('The answer is: ' + str(answers))
		loses += 1
		consWins = 0
	print("Wins: " + str(wins) + " Loses: " + str(loses))
	rnd += 1

	if consWins == 6:
		print("You have figured it out, congrats!")
		break

	prompt = input("Would you like to play again?[Y/n]: ")

	if prompt.lower() == 'y' or prompt == '':
		continue
	else:
		break




