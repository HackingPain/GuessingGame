# lines like this starting with "#" are comments to help explain the code
# this is a number guessing game that can be run from run menu in idle or from 
# the command prompt by typing python guessing_game.py when the command prompt
# is in the same directory as the saved game file.

# gives us access to the random module to generate the computer's number 
import random

# variables needed for game flow
secret = random.randint(1,100)
guess = 0
tries = 0
n = 6

# this is a dict, a type of data storage that allows the game
# to keep track of what the current guess number is and display it
indexer = {0:'first',1:'second',2:'third', 3:'fourth', 4:'fifth', 5:'sixth'}

# game introduction 
print ("\nWelcome to the special number guessing game.")
print ("I am thinking of a number between 1 and 100.")
print ("I will give you six tries to guess my number. Good luck!")

# game loop that let's you guess up to 6 times
# the loop is entered if you have not guessed the number
# and you have guesses left
# pay careful attention to the indents when writing Python
while guess != secret and tries < n:
    guess = int(input("\nWhat is your " + indexer[tries]+ " guess?\n"))

	# test if your guess is higher or lower than the computer number
	# and if you have more guesses
    if guess > secret and tries < n-1:
        print ("That's too high")
    elif guess < secret and tries < n-1:
        print ("That's too low")

    tries = tries + 1    
# tests if you have guessed the number or are out of tries
if guess == secret:
    print( "Holy cow are you lucky, you guessed right!")
else:
    print ("Better luck next time, you are out of tries. The secret number was:",secret)