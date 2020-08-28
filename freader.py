infile = open(r'c:\Users\dohbu\batchdata\wasteland.txt', mode = 'rt', encoding = 'utf-8' )
# Read All Btyes in file
infile.read()
# Go back to begining of file
infile.seek(0)
#Read a line
infile.readline()

# Go back to begining of file
infile.seek(0)

# Read All Lines
infile.readlines()

# CLose File 
infile.close()