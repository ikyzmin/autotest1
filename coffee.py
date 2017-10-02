class Machine(object):

	def __init__(self, coffeeCount):
		self.coffeeCount = coffeeCount
		self.payed = False
		self.money = 0
		self.change = 0
		self.drink = "empty"

	def pay(self,money):
		self.payed = True
		self.money= money
	
	def makeDrink(self):
		if self.coffeeCount > 0 and self.payed:
			self.coffeeCount-=1
			self.drink = "coffee"
		else:
			self.drink = "empty"
			if self.payed:
				self.change = self.money
				self.money = 0
			
