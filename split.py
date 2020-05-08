
s1 = ["the", "rain", "in", "spain"]
s2 = " ".join(s1)
print(s2)
s3 = '|'.join(s1)
print(s3)
s4,s5,s6,s7 = s3.split('|')
print(s4)
t1 = type(s7)

s0 = ''.join(["new" , "found", "land"])
print(s0)

tu1 = 'unforgetable'.partition('forget')
#returns a TUPLE
print(tu1)
#
s8,s9,s10 = tu1
print(s10)

