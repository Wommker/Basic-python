"""

A list is a collection of ordered elements
in a specific way, to create the list
these elements are surrounded by "[]"

"""

lis = [1,2,3,4]
lis_tw = ["cinco","seis","siete"]

#Lists have a number of functions

#among which are:

print(lis)

#Add a specific item to the list

lis.append(6)

print(lis)

#Add an item to the list at a specific index

lis.insert(0,0)

print(lis)

#Remove the last item from the list

lis.pop()

print(lis)

#Remove a specific item from the list

lis.remove(0)

print(lis)

#Sort list items

lis.sort()

print(lis)

#Reverse sort list items

lis.sort(reverse=True)

print(lis)

#add another list to the list

lis.extend(lis_tw)

print(lis)

#Show a specific item in the list

print(lis[0])

#Print a specific character of the variable from right to left

print(lis[-3])

#Prints two specific characters of the variable

print(lis[0],lis[-3])

#Print the characters from 0 to 3

print(lis[0:4])

#Print characters from 0 to 3 every 2 characters

print(lis[0:4:2])

#Print the entire variable backwards

print(lis[::-1])