import sys

FILENAME = sys.argv[1]
HOMEDIR = r'c:\Users\dohbu\batchdata'
SEP = '\\'
print(f'DATA HOME DIRECTORY: {HOMEDIR}')
FQN = HOMEDIR + SEP + FILENAME
print(f"OPENING FILE: {FQN}" )


infile = open(FQN, mode='rt', encoding ='ansi')
counter = 0
for line in infile:
    counter = counter + 1
infile.close()
print(f"RECORDS READ: {counter}")