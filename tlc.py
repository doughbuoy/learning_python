import math

row1 = 30
row2 = 20
row3 = 13

shoe = row1 / 6
print("Shoe is equal to: " + str(shoe) )
dude = (row2-(2*shoe))/2
print("Dude is equal to: " +str(dude) )
if shoe == dude:
    print("Dude has same value as 1 shoe: Very Sad... is this a cry for help?")
else:
    print("FALSE")

lace = (row3 - dude) / 4
print("Lace is equal to: " + str(lace) )

print('row4 = shoe + ((dude + (lace *2) + (shoe*2)) * lace)')
row4 = shoe + ((dude + (lace *2) + (shoe*2)) * lace)
print("row 4 = " + str(int(row4)) )
total = row1 + row2 + row3 + row4
print("Total: "  + str(row1) + " + " + str(row2) + " + " + str(row3) + " + " + str(int(row4)) + " = " + str(int(total)) )
