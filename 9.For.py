"""

The loop is a block of code that will
repeat itself as long as the conditions
indicated at the beginning of the loop
are true or some condition causes it to break.

The case of the for loop is different,
since it has the particularity of having
an interer variable that can change 
throughout the execution of the loop.

The for loop can retrieve a variable 
in different ways, here are a series 
of examples

"""

lis = ["cinco","seis","siete"]
dic = {'a':55,'b':33,15:'77'}

#Traverse the list, the iterator variable (i) takes the value of all elements of the list

for i in lis:
	print(i)

#Traverse a range

for i in range(0,10):
	print(i)

#loop through the list with two values, one for index and one for values

for i,v in enumerate(lis):
	print(i,v)

#Traverse a dictionary taking the values of keys and values

for i,v in dic.items():
	print(i,v)

#Show list size

print(len(lis))


"""

Loop through a range that is equal to the size of 
the list without the iterator variable being 
converted to the values of the list

"""

for i in range(0,len(lis)):
	print(lis[i])