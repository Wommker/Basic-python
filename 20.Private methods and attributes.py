"""

Private methods can limit the visibility
of a function or variable to a certain 
extent. Declaring your function or variable
as private limits access to only the class 
that encapsulates it.

the private method init is used as a class 
constructor for a class object. This method 
is called when an object of a class is instantiated, 
based on the method's arguments.

"""

#Class

class n_user():

	#Method init

	def __init__(self,user,email,password):
		self.user = user
		self.email	= email
		self.__password = self.__s__password(password)

	#Private method

	def __s__password(self,password):
		return password.upper()

	def g_password(self):
		return self.__password

n_user = lapiz("Juan","Juan@3m.com","anuj321")
print(mypencil.g_password())