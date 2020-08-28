#Nested list

a = [ [1,1] ] * 5
print(a)
print(f"3rd entry is {a[2]}" )
#lets append 7 to the 3rd nested entity
a[2].append(7)
# Note that since the each of the nested lists are pointing to same object 7 is added to all
print(a)
print(f"3rd entry is {a[2]}" )

