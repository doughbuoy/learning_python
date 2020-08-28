words = "I still feel 25 Most of the time I still raise a little Cain with the boys Honky Tonks and pretty women But Lord I'm still right there with'em Singing above the crowd and the noise".split()
word_cnt = len(words)
print(f"Word Count is {word_cnt}")
del words[7]
word_cnt = len(words)
print(f"Word Count is {word_cnt}")
print(words)

# Now use REMOVE to remove a match .... this however will raise error if not there so use in conjunction with count or in


words.remove('little')
word_cnt = len(words)
print(f"Word Count is {word_cnt}")