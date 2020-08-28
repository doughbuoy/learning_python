def gen246():
    print("I am about to yield 2")
    yield 2
    print("I am about to yield 4")
    yield 4
    print("I am about to yield 6")
    yield 6

k = gen246()
next(k)

d = gen246()
for c in d:
    print(c)
