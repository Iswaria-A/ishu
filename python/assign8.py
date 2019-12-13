import random
number=random.randrange(1,10)
guess=0
while guess!=number:
	guess=input("Please enter a number between 1 and 9:")
	guess=int(guess)
	if guess not in range(1,10):
		print("You have to enter a number between 1 and 9")
	elif guess<number:
		print("You have guessed too low")
	elif guess>number:
		print("You have guessed too high")
	