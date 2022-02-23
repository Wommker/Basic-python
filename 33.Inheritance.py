"""

Inheritance allows you to define new classes
based on existing ones in order to reuse 
the code, thus generating a hierarchy.

"""


#Parent class

class vehicle():

	def __init__(self,brand,model):
		self.brand = brand
		self.model = model
		self.accelerate = False
		self.moving = False

	def accelerat(self):
		self.accelerate = True

	def dmovin(self):
		self.moving = True

	def state(self):
		print(self.brand,self.model,self.accelerate,self.moving)

#Class that inherits

class motorcycle(vehicle):
	pass

#Object

my_motorcycle=motorcycle("Honda","CBR")
my_motorcycle.accelerat()
my_motorcycle.state()