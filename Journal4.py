class Orangutan:

	def __init__(self):
		self.arm_length = 2.1
		self.leg_length = 1.0
		self.eyes = 2
		self.tail = False
		self.furry = True

	def printOrangutan(self):
		print("My favorite animal is an orangutan")
		print(f"Its arms are {self.arm_length} meters long")
		print(f"Its legs are {self.leg_length} meters long")
		print(f"It has {self.eyes} eyes")
		print("Does it have a tail?", self.tail)
		print("Is it hairy?", self.furry)


animal = Orangutan()
animal.printOrangutan()
