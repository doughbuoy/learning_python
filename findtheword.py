words = "Chordie features. Search the Internet for guitar chords and tabs/tablatures. Transpose to another key. Graphical chord grids. High quality formatting. Mobile browsing - when you are on the road. High print quality. Unique songbook feature.".split()
i = words.index('Mobile')
print(f"value found at {i}")
print(f"value found was {words[i]}")

# looking for a word not in list creates an error and scripts abends
#t = words.index('Rabbit')
#print(f"value found at {t}")
#SO best to find out first

RABBIT_COUNT = words.count('rabbit')
print(RABBIT_COUNT)
if RABBIT_COUNT > 0:
    print("rabbit found")
    i = words.index('rabbit')
    print(i)
else:
    print("rabbit not found")

#---------------------------------------
#  ok lets try again
#---------------------------------------
words.append("rabbit")

RABBIT_COUNT = words.count('rabbit')
print(RABBIT_COUNT)
if RABBIT_COUNT > 0:
    print("rabbit found")
    i = words.index('rabbit')
    found = words[i]
    print(i)
else:
    print("rabbit not found")
    found = None
print(f"found word  {found} !")

#-----------------------------------------#
# ANOTHER WAY to find out 
#-----------------------------------------#

if 'rabbit' in words:
    print("rabbit found")
else:
    print("rabbit Not Found")


if 'fox' in words:
    print("fox found")
else:
    print("fox Not Found")