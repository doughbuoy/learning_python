seasons = [ 'spring', 'summer', 'fall',  'winter' ]


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterator is empty")


for I in range(10):
    print(I)

