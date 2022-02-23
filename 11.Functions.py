"""

Functions are blocks of code that can 
be reused simply by calling the function.

Below are different functions with 
their respective calls

"""

#Simple function

def fun():
	print("I am a function")

fun()

#Function with parameter

def suma(num):
	print(5+num)

suma(5)

#Function with parameter that returns value

def suma(num):
	return(5+num)

print(suma(10))

#Function with double parameter

def rest(num1,num2):
	return(num1-num2)

result = rest(num2 = 25, num1 = 10)
print(result)

#Function with double parameter and with backup in case of not passing the value of the necessary parameter

def mul(num1=1,num2=1):
	return(num1*num2)

resultdom = mul(5,2)
print(resultdom)

#Function that returns multiple values

def mulvalues():
	return"sttr",False,573.2

print(mulvalues())
