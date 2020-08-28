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
    #SUBSTRING REC_TYPE = first four bytes in file
    REC_TYPE = (line[0:4])
    counter = counter + 1
    print(f'RECORD TYPE: {REC_TYPE}')
infile.close()
print(f"RECORDS READ: {counter}")