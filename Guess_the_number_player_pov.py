import math, random

def game():
	number_range = input('Please enter 2 values for range: ')
	low, high = number_range.split(',')
	low = int(low)
	high = int(high)
	tries = int(math.ceil(math.log((high-low), 2)))
	answer = random.randint(low, high-1)
	print('I have picked a number between %i and %i, what’s your guess?' %(low, high))
	while (tries>0):
		print('You have %i tries left.' %(tries))
		print()
		guess = input()
		guess = int(guess)
		if(guess == answer):break
		elif(guess > answer):
			print('This number is higher than the number I have in mind! Next try?')
			tries = tries -1
		elif(guess < answer):
			print('This number is lower than the number I have in mind! Next try?')
			tries = tries -1
	if(tries >0): print ("That's right! That was my number!")
	else: print("You lost")
	play = input('Play again?`y/n')
	if(play == 'y'): game()
	
game()
