words = "Sometimes I look like Jesse James".split()
words.insert(2,"feel")
print(words)
del words[3]
print(words)
#Join the array with space as delimiter
sentence = ' '.join(words)
print(sentence)