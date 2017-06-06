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
		die = 0
		for y in dice_tuples:
			die = die +(roll(y))
		dice_total.append(die)
	return dice_total

def get_stats(results):
	maximum_result = max(results)
	dicetionary = {}
	dicetionary2 = {}
	for i in range(1, maximum_result+1):
		temp = results.count(i)
		if (temp>0):
			dicetionary.update({i:temp})
	for x in range(1, maximum_result+1):
		z = 0
		temp = 0
		for y in results:
			if(y==x):
				z=z+1
			else:
				if(z>temp):
					temp = z
					z = 0
		dicetionary2.update({x:temp})
	average = sum(results)/len(results)
	statistics = {'count' : dicetionary, 'sequence' : dicetionary2, 'average' : average}
	return statistics

die = get_stats(test("1d6", 2000))
print(die)
