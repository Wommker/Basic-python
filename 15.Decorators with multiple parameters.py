"""

Normally decorators are added to
different functions, so it is unknown
number of arguments that may be needed
during the performance of the decorated function, for
it is written this way to avoid
possible errors that occur during the
program execution

"""


def	deco_function(para_function):
	def end_fuc(*args):
		print("Calculation start")
		para_function(*args)
		print("End of calculation")

	return end_fuc

@deco_function
def sum(x,y):
	print(x+y)


print("Let's add two values")
x = float(input("Type the first value: "))
y = float(input("Enter the second value: "))
sum(x,y)