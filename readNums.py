#  This program reads the numbers generated from numberGen.py and converst them to an integer

import sys
def read_series(FQN):
    INFILE = open(FQN, mode='rt', encoding='utf-8')
    SERIES = []
    for RECORD in INFILE:
        NUMBER = int(RECORD.strip())
        SERIES.append(NUMBER)
    INFILE.close()
    return SERIES


def main(FQN):
    SERIES = read_series(FQN)
    print(SERIES)


if __name__ == '__main__':
    FILENAME = sys.argv[1]
    HOMEDIR = r'c:\Users\dohbu\batchdata'
    SEP = '\\'
    print(f'DATA HOME DIRECTORY: {HOMEDIR}')
    FQN = HOMEDIR + SEP + FILENAME
    print(f"PROCESSING FILE: {FQN}")
    main(FQN)