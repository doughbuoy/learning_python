from urllib.request import urlopen

def fetchwords():
    story = urlopen('http://sixty-north.com/c/t.txt')
    swords = []
    for l in story:
        lw = l.decode('utf8').split()
        for x in lw:
            swords.append(x)
            story.close()
            for word in swords:
                print(word)
if __name__ == '__main__':
    fetchwords()
