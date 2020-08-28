blue_eyes = {"bob", "sue", "jim", "lily", "jack"}
blond = {"harry", "sue", "pat", "tom", "mia", "josh"}
smell = {"tom", "mia"}
taste = { "jim", "lily", "lola"}
oblood = {"mia", "josh" }
bblood = {"sue", "jim", "pat"}
ablood = {"tom"}
abblood = {"harry", "jack", "lily", "bob"}

#find all with blond and or blue eyes
a = blue_eyes.union(blond)
print(f"people with blond hair and or blue eyes: {a}")

#Find all with blond AND blue eyes
b = blue_eyes.intersection(blond)
print(f"people with blond hair AND blue eyes: {b}")

# compare lists and determine deltas

c = blue_eyes.difference(blond)
print(f"people with blue eyes but dont have blond hair: {c}")

d = blond.difference(blue_eyes)
print(f"people with blond but dont have blue eyes: {d}")

# blond hair or blue eyes but not both
e = blond.symmetric_difference(blue_eyes)
print(f"blond hair or blue eyes but not both: {e}")


#SUBSET
# are all people in smell in blond list
f = smell.issubset(blond)
print(f"all people who smell are blond? : {f}")

# all members of smell also in taste ?
g = taste.issuperset(smell)
print(f"all people who taste a superset of those that smell ? : {g}")

#test to see if no members are in each

h = abblood.isdisjoint(oblood)
print(f"all people who have ab blood should not be in same set as people with o blood ? : {h}")
