"""

A static method belongs to a class; 
still, it is not bound to the object 
of that class. Therefore, it can be 
called without creating an instance 
of the class in which it resides.

"""

class rectangle():

	#Static method

	@staticmethod
	def r_side_y():	
		return 5

	def __init__(self,side_x):
		self.side_x = side_x

	#Instance method

	def area(self):	
		self.area = rectangle.r_side_y()*self.side_x
		return self.area

n_rectangle = rectangle(10)
print(n_rectangle.r_side_y())
print(rectangle.r_side_y())