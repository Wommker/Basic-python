"""

The functions do not alter the 
variables defined outside their 
function, for this the simple variable
is converted into a global variable

"""

#Vars

onvar = 'One'
twvar = 'Two'

print(onvar)

#Function that tries to alter the variable without success

def fun():
	onvar = False

fun()

print(onvar)

#Function that can alter the variable by making it global

def cfun():
	global onvar
	onvar = False

cfun()

print(onvar)
