import sys


def print_items(items):
    for i in items:
        print(i)


if __name__ == '__main__':
    value = sys.argv[1]
    print(value)
    print_items(value)
