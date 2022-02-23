"""

Some string methods used to edit text 
variables

"""

var_string = "Hello Wolrd"

#Returns the string with all its characters to lowercase

print(var_string.lower())

#Returns the string with all its characters in uppercase

print(var_string.upper())

#Returns the string with the first character of each word capitalized

print(var_string.title())

#Returns the string with its first character uppercase

print(var_string.capitalize())

#Returns a count of the times a substring appears in the string

print(var_string.count('o'))

#Returns the first index in which the substring appears (-1 if it does not appear)

print(var_string.find('o'))

#Separate the string into substrings based on their spaces and return a list

print(var_string.split())

#Replace a substring of a string with another and return it

print(var_string.replace('o','0'))

#We can indicate a limit of times to replace

print(var_string.replace('o','0',1))