from urllib.request import urlopen

def fetchwords():
    story = urlopen('http://sixty-north.com/c/t.txt')
    swords = []
    for l in story:
        lw = l.decode('utf8').split()
        for x in lw:
            swords.append(x)
            print(x)
        story.close()
        return swords

def print_items(items):
    for i in items:
        print(items)

def main():
    words = fetchwords()
    print_items(words)

if __name__ == '__main__':
    main()
