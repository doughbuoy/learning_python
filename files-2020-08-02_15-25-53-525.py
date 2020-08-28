import sys

FILENAME = sys.argv[1]
HOMEDIR = r'c:\Users\dohbu\batchdata'
SEP = '\\'
print(f'DATA HOME DIRECTORY: {HOMEDIR}')
FQN = HOMEDIR + SEP + FILENAME
print(f"Opening File: {FQN}" )


