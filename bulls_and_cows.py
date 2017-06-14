import random


def generate_cipher():
    """
    returns a random sequence of 4 unique digits as python list
    e.g.
    print(generate_cipher()) -> [5, 2, 7, 3]
    print(generate_cipher()) -> [5, 0, 3, 9]
    print(generate_cipher()) -> [3, 4, 8, 6]
    """
    # remove the pass statement and put your code here
    a1 = random.randint(0, 9)
    a2 = (a1 + random.randint(1, 9))%10
    a3 = (a1 + random.randint(1, 8))%10
    a4 = (a1 + random.randint(1, 7))%10
    if((a3>=a2) or (a3<a1 and a1<a2)): a3 = (a3+1)%10
    if((a4>=a2) or (a4<a1 and a1<a2)): a4 = (a4+1)%10
    if((a4>=a3) or (a4<a1 and a1<a3)):
    	a4 = (a4+1)%10
    	if(a4==a2): a4 = (a4+1)%10
    cipher = [a1, a2, a3, a4]
    return cipher


def get_bulls_and_cows(cipher, guess):
    assert len(cipher) == len(guess) == 4, 'cipher and guess must be lists of length 4'
    # remove the pass statement and put your code here
    bulls = 0
    cows = 0
    for x in range(0, 4):
    	if(cipher[x] == guess[x]): bulls+=1
    	else:
    		for y in range(0, 4):
    			if(cipher[x] == guess[y]): cows+=1
    return (bulls, cows)


def play_game():
    cipher = generate_cipher()
    output_string = ""
    while True:
    	guess = str(input("Enter your guess without spaces: \n"))
    	guess_array = [int(guess[0]), int(guess[1]), int(guess[2]), int(guess[3])]
    	bulls, cows = get_bulls_and_cows(cipher, guess_array)
    	output_string = output_string + str(guess) + " bulls: " + str(bulls) + ", cows: " + str(cows) + "\n"
    	print(output_string)
    	if(bulls == 4): break
    print("Congrats, You win")

play_game()
