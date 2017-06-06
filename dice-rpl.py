import random

def roll(dice):
	dice_total = 0
	for i in range(0,dice[0]):
		dice_total = dice_total + random.randint(1, dice[1])
	return dice_total

def test(dice_string, amount):
	dice_list = dice_string.split("+")
	dice_tuples = []
	for x in range(0, len(dice_list)):
		temp = dice_list[x].split("d")
		temp = [int(i) for i in temp]
		dice_tuples.append(tuple(temp))
	dice_total = []
	for i in range(0, amount):
		for y in dice_tuples:
			dice_total.append(roll(y))
	return dice_total

die = test("1d6+1d8", 20)
print(die)
