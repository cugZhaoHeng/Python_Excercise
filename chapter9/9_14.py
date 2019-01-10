from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides=sides
	
	def roll_die(self):
		self.sides=randint(1,6)
		print(self.sides)

	def roll_die_10(self):
		self.sides=randint(1,10)
		print(self.sides)
	def roll_die_20(self):
		self.sides=randint(1,20)
		print(self.sides)
die = Die()
for i in range(0,5):
	die.roll_die()

print("========")

for i in range(0, 5):
	die.roll_die_10()

print("========")

for i in range(0, 5):
	die.roll_die_20()

