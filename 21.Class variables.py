"""

The class variables correspond to a 
certain class and an object is not
needed to access these variables

"""

class rectangle():

	#Underscore as good practice so that it is not altered by other developers
	#Class variable
	
	_side_y = 5 

	def __init__(self,side_x):
		self.side = side_x

n_rectangle = rectangle(10)
print(rectangle._side_y)

#Returns a dictionary with the instance variables with their value

print(n_rectangle.__dict__) 