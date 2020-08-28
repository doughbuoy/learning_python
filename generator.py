def gen123():
    yield 1
    yield 2
    yield 3
g = gen123()
print(f"g = {g}")

for v in gen123():
    print(v)