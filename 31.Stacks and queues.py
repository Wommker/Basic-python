"""

Stacks and Queuese:

Stacks: It is an ordered list or data 
structure that allows storing and 
retrieving data, being the mode of access
to its elements of type last in, first
out

Queuese: It is a data structure, 
characterized by being a sequence of 
elements in which the first to enter 
is the first to leave.

"""

#Stacks:

print("Stacks")
stacks = [1,2,3,4]
print(stacks)
stacks.append(5)
stacks.append(6)
print(stacks)
n = stacks.pop()
print(n)
print(stacks)

#Queuese

print("Queuese")
queuese = [1,2,3,4]
print(queuese)
queuese.append(5)
queuese.append(6)
print(queuese)
n = queuese.pop(0)
print(n)
print(queuese)
