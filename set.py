p = {20, 30, 40, 50, 60}
print(p)
print (f"{type(p)} ")

# Try to create an empty set
m={}
print(f"{type(m)}")

# oops that created an empty  dictionary

# Use Set constructor
n = set()
print(f"{type(n)}")

#Bingo !

print(" Creating an set named o")
o = set([23,34,99,456,2222])
print(o)
print(" Creating an set named q with values 23,34,99,456,2222,23")
q = set([23,34,99,456,2222, 23])
print(q)
print("Notice there is only one 23? ")
print("that is because sets remove duplicates")

#itterate through


for a in q:
    print(a)

# if
if 45 in q:
    print("True")
else:
    print("false")

#add 45 into q and check again
q.add(45)
if 45 in q:
    print("True")
else:
    print("false")


#Adding a bunch including another set ....
q.update([24, 29, 36, 44,292])

print("UPDATE q with contents of p")
print("Q is :")
print(q)

print("p is :")
print(p)
q.update(p)
print("After Update Q is :")
print(q)

# REMOVE (Be carefull if the key isnt there a error is produced so test it first
print("REMOVE 23")
if 23 in q:
    q.remove(23)
else:
    print("key not found")
print(q)
# if you dont want to test ... you can just use discard
print("DISCARD 292 and 2")
print(q)
q.discard(292)
q.discard(2)
print(q)

