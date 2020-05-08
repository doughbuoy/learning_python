import math
import datetime
s11 = "{0} is the new {1} !".format("green", "black")
print(s11)
s12 =  "{} is the new {} !".format("green", "black")
print(s12)

s13 = "{name} is {age} years old".format(name="JIM", age="55")
print(s13)

s14 = "Math Constants pi={m.pi} and e={m.e} are fun to extract from math object ".format(m=math)
print(s14)

s15 = "Math Constants pi={m.pi:.3f} and e={m.e:.3f} are fun to extract from math object ".format(m=math)
print(s15)

s16 = f"one plus one is {1+1}"
print(s16)

s17 = f"The Curent Time is : {datetime.datetime.now().isoformat()}"
print(s17);

s18 = f"pi is {math.pi} and e is {math.e}"
print(s18);

s19 = f"pi is {math.pi:.3f} and e is {math.e:.3f}"
print(s19);

string = "freeCodeCamp"
substring = (string[0:5])

print(substring)


print(string[-1])