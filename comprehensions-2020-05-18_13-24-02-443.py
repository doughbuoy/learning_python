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


colors2code = { 'WHITE':'#FFFFFF',
'SILVER':'#C0C0C0',
'GRAY':'#808080',
'BLACK':'#000000',
'RED':'#FF0000',
'MAROON':'#800000',
'YELLOW':'#FFFF00',
'OLIVE':'#808000',
'LIME':'#00FF00',
'GREEN':'#008000',
'AQUA':'#00FFFF',
'TEAL':'#008080',
'BLUE':'#0000FF',
'NAVY':'#000080',
'FUCHSIA':'#FF00FF',
'PURPLE':'#800080',
}

code2color = {code:color for color, code in colors2code.items()}

from pprint import pprint as pp

print(f"g contains:{g}")
print(f" G is of type {type(g)} Note DUPES are eliminated")
