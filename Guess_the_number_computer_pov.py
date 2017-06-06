def game():
	number_range = input('What range is your number in?')
	low, high = number_range.split(',')
	low = int(low)
	high = int(high)
	while True:
		guess = int((high + low)/2)
		check = input("Is your number " + str(guess) + "?")
		if(check == 'y'): break
		if(check == 'h'): low = guess
		elif(check == 'l'): high = guess
		else: print('Input either y, l or h')
	print ('Woah, that was tricky!')
	play = input('Play again?`y/n')
	if(play == 'y'): game()
	
game()
