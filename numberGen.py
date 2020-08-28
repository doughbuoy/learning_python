import sys
from itertools import count, islice

def sequence():
    """"GENERATE RECAMANS SEQUENCE"""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a-n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """Write Seqiene to file"""
    f = open(filename, mode='wt', encoding = 'utf-8')
    f.writelines(f"{r} \n" for r in islice(sequence(), num + 1))
    f.close()


if __name__ == '__main__':
    FILENAME = sys.argv[1]
    HOMEDIR = r'c:\Users\dohbu\batchdata'
    SEP = '\\'
    print(f'DATA HOME DIRECTORY: {HOMEDIR}')
    FQN = HOMEDIR + SEP + FILENAME
    print(f"OPENING FILE: {FQN}")
    NUM = int(sys.argv[2])
    print(f"GENERATING {NUM} VALUES")
    write_sequence(FQN,NUM)