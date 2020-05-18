
month = { 1:"Jan",
           2:"Feb",
           3:"Mar",
           4:"Apr",
           5:"May",
           6:"Jun",
           7:"Jul",
           8:"Aug",
           9:"Sep",
           10:"Oct",
           11:"Nov",
           12: "Dec"
           }
i = 5
print(f"its {month[i]} and its snowing")


#Convert into disctionary using dict
namelist = [ ("bob", 45) , ("sue",23) , ("kim", 55) ]
namedic = dict(namelist)
print(namelist)
print(namedic)


# Copying dictionary
#OPtion 1
mn = month.copy()
print(mn)
# Option 2
m = dict(month)
print(m)


# Update Dictionary
#Add a new
upd = { 2020:"Sucks" }
m.update(upd)
print(m)

#Update existing Value
JAN = {1:"JAN"}
m.update(JAN)
print(m)