"""

In case an area of the code can fail,
we can add "Try" and then "except"
to define what we want to do in case 
the code fails.

"""

#In case we know exactly the possible error that can happen

try:
	div = 15 / 0
except ZeroDivisionError:
	div = 15/2

print(div)

#In case it is not known what error can happen

try:
	div = int("Hey")
except:
	div = 15/3

print(div)

#"finally" is added so that a code is executed in case of error or not

try:
	div = int("15")
except:
	div = 15/4
finally:
	print("other")

print(div)