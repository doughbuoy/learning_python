s = [1,2,3,4,5,6,7,8,9]
t = s[2:5]
print(t)

#gets everything but the first and last
u = s[1:-1]
print(u)

# Copying lists into new list with a new identity
a = t
# this just creates a pointer in a to the same object so - a is t should return TRUE
if a is t:
    print("true")
else:
    print("false")
# To create a new list with same values
b = t[:]
# b is t should return false this time
if b is t:
    print("true")
else:
    print("false")
# prove they have same values ... this should return true
if b == t:
    print("true")
else:
    print("false")

# More readable way of copying by using copy method
c = t.copy()
if c == t:
    print("equiv true")
else:
    print("equiv false")
if c is t:
    print("same true")
else:
    print("same false")

#Another way to copy
d = list(t)
if d == t:
    print("equiv true")
else:
    print("equiv false")
if d is t:
    print("same true")
else:
    print("same false")


# lists multiplier
# e is 4 values long
e = [1, 2, 3, 4]
print(f"e is {len(e)} values long")
f = e * 4
# f is 16 values long
print(f"f is {len(f)} values long")
#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(f)
#This is mostly used to create a and initialize a list of known length
g = [0]*12
print(f"g is {len(g)} values long")
print(g)