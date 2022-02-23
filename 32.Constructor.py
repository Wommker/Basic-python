"""

A constructor is a special kind of method 
that Python calls when it instantiates an 
object using the definitions found in your class. 
Python relies on the constructor to perform 
tasks such as initializing (assigning values to) 
any instance variables that the object will 
need when it starts.

"""

class rectangle():

	#Constructor
	
	def __init__(self,side_x):
		self.side_x = side_x

new_rectnagle = rectangle(10)
print(new_rectnagle.side_x)