import random

class Dice:
	def __init__(self,dice_id):
		self.dice_id = dice_id

	def roll(self):
		return 1 if random.randint(1,4)<3 else 0

class Dices:
	def __init__(self,number_of_dices):
		self.dices = [Dice(i) for i in range(number_of_dices)]

	def roll(self):
		result = 0
		for dice in self.dices:
			result += dice.roll()
		return result
