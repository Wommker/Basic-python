#Tuples are very similar to lists but with the difference that they cannot be modified.

tpl = ("One","Two",3,False,"Hello",1,57)

#print the variable

print(tpl)

#Print a specific character of the variable

print(tpl[0])

#Print a specific character of the variable from right to left

print(tpl[-3])

#Prints two specific characters of the variable

print(tpl[0],tpl[-3])

#Print the characters from 0 to 5

print(tpl[0:6])

#Print characters from 0 to 5 every 2 characters

print(tpl[0:6:2])

#Print the entire variable backwards

print(tpl[::-1])

#Change the list to a tuple

lis = [1,2,3,4]
print(type(lis))
lis=tuple(lis)
print(type(lis))