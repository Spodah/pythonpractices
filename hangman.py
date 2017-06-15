#Assignment did not specify how to handle multiple attempts to guess the same character
TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'


# DO NOT MODIFY THE initialize function
def initialize(word_list):
    i = 0
    while i < len(word_list) and start_new_game(word_list[i], TRIES):
        i += 1


def obfuscate(word, letters_guessed):
    # replace the pass statement with your code
    obfuscated = ""
    word = word.upper()
    letters_guessed = letters_guessed.upper()
    for x in range(0,len(word)):
    	if word[x].isalpha():
    		for y in range(0, len(letters_guessed)):
    			if(word[x] == letters_guessed[y]):
    				obfuscated = obfuscated + word[x]
    		if (len(obfuscated) == x):
    			obfuscated = obfuscated + "_"
    	else: obfuscated = obfuscated + word[x]
    return obfuscated.upper()
    


def start_new_game(word, max_tries):
    word = word.upper()
    tries = TRIES
    guesses = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while(tries > 0):
    	obfuscated = (obfuscate(word, guesses))
    	if(obfuscated == word):
    		print(GAME_WON_PHRASE)
    		new_game = input(OFFER_NEXT_GAME)
    		if (new_game == "y" or new_game == "Y"):
    			return True
    		elif (new_game == "n" or new_game == "N"):
    			return False
    	print(obfuscated)
    	print(LETTERS_LEFT)
    	print(letters)
    	guess = input(INPUT_PROMPT)
    	guess = guess.upper()
    	if(len(guess)>1):
    		print(INVALID_INPUT)
    	elif(guess.isalpha == False):
    		print(INVALID_INPUT)
    	else:
    		letters = letters.replace(guess, "")
    		guesses = guesses + guess
    		if(word.find(guess) == -1):
    			tries = tries-1
    			print("Tries left:" + str(tries))
    		
    	
    	


# Only one of the following lines is needed:
# Initialize for manufal testing (feel free to change the words in the list)
# Import for automated testing.

initialize(['Obi-Wan Kenobi', 'Alladin'])
#import hangman_test

# ==================================================================
