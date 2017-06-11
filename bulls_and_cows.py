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
    """
    takes 2 python lists of length 4 cipher and guess and computes the number
    of bulls and the number of cows as a 2 element tuple

    in this implementation bulls and cows will be mutually exclusive
    (a digit in the sequence can't be both a bull and a cow) and the sum of
    the two must be <= 4

    bulls: number of digits guessed correctly AND in the correct place
    cows: number of digits guessed correctly NOT in the correct place
    here are some of the test cases:
    print get_bulls_and_cows([1,2,3,4],[1,2,3,4]) -> (4, 0)
    print get_bulls_and_cows([1,2,3,4],[2,1,4,3]) -> (0, 4)
    print get_bulls_and_cows([1,2,3,4],[1,6,2,3]) -> (1, 2)
    print get_bulls_and_cows([1,2,3,4],[5,6,7,8]) -> (0, 0)
    """
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
    # this function should use both generate_cipher and get_bulls_and_cows
    # inside and provide a command-line interface to play the game
    # while keeping the results of previous attempts as described in the pdf
    # there should be some basic validation of the user input
    # (that its a number of 4 unique digits)

    # here's an example of the game played with the cipher being [1, 3, 9, 7]
    # feel free to remove when you understood it if it feels too cumbersome :)
    # you can also play it here: http://www.mathsisfun.com/games/bulls-and-cows.html
    # pick the 0-9, 4 codes option

    # Enter your guess without spaces:
    # 1234
    # 1234 bulls: 1, cows: 1

    # Enter your guess without spaces:
    # 3945
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2

    # Enter your guess without spaces:
    # 1398
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0

    # Enter your guess without spaces:
    # 1298
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0

    # Enter your guess without spaces:
    # 1397
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0
    # 1397 bulls: 4, cows: 0

    # Congrats, You win

    # remove the pass statement and put your code here
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
