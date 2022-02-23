"""

It is the same as a function only it 
has the advantage that it does not 
return all the result in the first call,
but returns it different on every call

It is more efficient than the traditional 
function

"""

def generatepairs(limit):
	num = 1
	while num < limit:
		yield (num*2)
		num+=1

dev=generatepairs(10)

#a new parameter is only created inside
#dev when the for loop goes through it

for i in dev:
	print(i)

