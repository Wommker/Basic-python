#Sets

#Variables

a = {1,2,3,4,5,6}
b = {3,5,6,7,8,9}

print(a)
print(b)

#Sum of sets

print(a|b)

#Numbers they have in common

print(a&b)

#Elements of a that are not in b

print(a-b)

#Elements that are in a and b but not in both

print(a^b)

#Separator

print("-----")

#If a is a subset of b

print(a.issubset(b))

#If a is a superset of b

print(a.issuperset(b))

#If the sets are unconnected

print(a.isdisjoint(b))

#Separator

print("------")

#Converts to immutable sets, not if you can alter

c=frozenset({11,12,13})
print(c)