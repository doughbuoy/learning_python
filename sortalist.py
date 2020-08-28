

words = "Sometimes I look like Jesse James".split()
words.sort()
print(words)

numbs = [12, 14,44,3]
numbs.sort()
print(numbs)

#
# REVERSE SORT
#
numbs.sort(reverse=True)
print(numbs)

#
#  SORT by Length
#
words.sort(key=len)
print(words)


