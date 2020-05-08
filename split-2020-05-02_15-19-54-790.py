
s1 = ["the", "rain", "in", "spain"]
s2 = " ".join(s1)
print(s2)
s3 = '|'.join(s1)
print(s3)
s4,s5,s6,s7,s8 = s3.split('|')
print(s4)
t1 = type(s8)
print(t1)