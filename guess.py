import random
# Limit number of guesses



def game():
	secret_num = random.randint(1, 50)
	bad_guesses = []
	print("I'm thinking of a number between 1 and 50!")
	print("Guess the number!")

	
	while len(bad_guesses) < 10:
		try:
			guess = int(input("> "))
		except ValueError:
			print("That's not a number!")
		else:
	
			if guess == secret_num:
				print("You guessed it! My number was {}!".format(secret_num))
				break
			elif guess < secret_num:
				print("My number is higher than {}!".format(guess))
			elif guess > secret_num:
				print("My number is lower than {}!".format(guess))
		
			bad_guesses.append(guess)
	else:
		print("Oh no - you didn't guess my number!")
		print("My secret number was {}!".format(secret_num))
	play_again = input("Would you like to play again? Y/n ")
	if play_again.lower() != 'n':
		game()
	else:
		print("Bye!")
		
game()