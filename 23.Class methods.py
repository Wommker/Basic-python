"""

Class methods belong to the class without
being part of the object, so they can be
used without having to access the object.

The difference is that class methods can 
access the methods and attributes of the 
classes they are inheriting.

"""


class geometrica():
	squina = True

class rectangle(geometrica):

	def __init__(self,side_x):
		self.side_x = side_x

	#Class method

	@classmethod
	def new(cls,side_x):	
		cls.squina = False
		return rectangle(side_x)
		
n_rectangle = rectangle.new(10)
print(n_rectangle.side_x)
print(n_rectangle.squina)

