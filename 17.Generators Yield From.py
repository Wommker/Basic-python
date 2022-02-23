"""

the reserved word "Yield" allows us to 
internally traverse a parameter, without
having to use another bugle for

"""

def yieldfrom(*nombres):
	for elemento in nombres:
		#for subelemento in elemento:
			yield from elemento


dev=yieldfrom("carlos","juan","juan carlos")

print(next(dev))
print(next(dev))

#Variables are only created when they are printed