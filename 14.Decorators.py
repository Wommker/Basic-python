"""

Decorator functions work to add extra 
code to other functions, receive as 
parameter a function and execute code 
before and after it runs.

"""

#Fecorator function

def	deco_function(para_function):
	def end_fuc():
		print("Calculation start")
		para_function()
		print("End of calculation")
	return end_fuc

#Function call, along with a line of code
#Which allows I will add the decorator function.

@deco_function
def sum():
	print(7+6)

#Decorated function call

sum()