"""

Practice block of:

*Variable types and assignments
*Print or display text in console variables
*Concatenate text variables with other text variables
*Concatenate any type of variable

"""

#Variable types and assignments

#Only text or string

var_string = "Hello Wolrd"
text_one = "Hello "
text_two = "Wolrd "

#Numeric variables or int

var_numero = 10

#Numeric variables with decimals or float

var_decimal = 3.1415

#true or false variables, Booleans

var_bol = True

#Print or display text in console

print("Hello")

#Print a Text Variable

print(var_string)

#Concatenate text variables with other text variables

print(text_one + text_two)

#Concatenate any type of variable

#Method 1

print("{b}{a}".format(a=text_two,b=text_one))

#Method 2

print("{}{}".format(text_one,text_two))

#Method 3

print(f"{text_one}{text_two}")

#Method 4

print(text_one,text_two,var_decimal)

#Method 5

#% s for string% i for integers% f for numbers with decimals or floats

print("%s %s %i" % (text_one,text_two,var_numero))

#Method 6

print(text_one + text_two + str(var_numero))