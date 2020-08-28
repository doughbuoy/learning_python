x = [4,9,2,1]
print(x)
y = sorted(x)
print(y)
# Next line creates an reference
z = reversed(y)
# convert the reference to a list
a= list(z)
print(a)

# Or do it all as one function
b = list(reversed(a))
print(b)