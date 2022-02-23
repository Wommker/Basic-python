"""

Dictionaries are very similar to lists 
or but with the difference that they 
present two values called "Key" that 
acts as an index and the value of this 
index, when the dictionary is printed 
it will always do so in a different order

"""

dic = {'a':55,'b':33,15:'77'}
dic2 = {'f':35,'g':35,75:'17'}


print(dic)

#Add key and value

dic['c']="New value"

print(dic)

#Print the specific value using its key

print(dic['a'])

#Search for a specific key and return False if not found

print(dic.get('z',False))

#Delete a specific key with its value

del(dic['c'])

print(dic)

#Show only dictionary keys

print(dic.keys())

#Display only dictionary keys as a list

print(list(dic.keys()))

#Show only dictionary values

print(dic.values())

#Display only dictionary values as a list

print(list(dic.values()))

#Add a dictionary to the dictionary

dic.update(dic2)

print(dic)