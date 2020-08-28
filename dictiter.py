colors = { 'WHITE':'#FFFFFF',
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

for key in colors:
    print(f"key-{key} is {colors[key]}")

print("Just the values")
 # list the keys
for value in colors.values():
     print(value)

 #List the keys
print("Just the keys")
for key in colors.keys():
     print(key)

# extract by items [returns a tuple] and then Tuple extract
print("Use item")
for key, value in colors.items():
    print(f"{key} => {value}")


if 'BLUE' in colors:
    print("Yes Blue is there")
else:
    print("NOPE")


if 'BROWN' not in colors:
    print("Yes Brown is not here")
else:
    print("yes")