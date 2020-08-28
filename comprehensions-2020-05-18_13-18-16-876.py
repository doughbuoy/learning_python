words = "On a dark desert highway Cool wind in my hair Warm smell of colitas Rising up through the air".split()
lengths = [len(word) for word in words]
print(words)
print(lengths)

# ALTERNATIVLY

lengths2 = []
for item in words:
    lengths2.append(len(item))
print(lengths2)

from math import factorial

# creates a list of the factorals of valies 1 to 19

f = [len(str(factorial(x))) for x in range(20)]

print(f"F contains:{f}")
print(f" F is of type {type(f)} ")

g = {len(str(factorial(x))) for x in range(20) }
print(f"g contains:{g}")
print(f" G is of type {type(g)} Note DUPES are eliminated")


h = {len(str(factorial(x))) for x in range(20) }
print(f"g contains:{g}")
print(f" G is of type {type(g)} Note DUPES are eliminated")
