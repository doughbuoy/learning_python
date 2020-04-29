import sys

def BANNER(message, border='-'):
    '''
    Purpose: this function prints a border around the argument message
    for example BANNER("Test") will print Test with a boarder of -
    whereas BANNER("Test", "*") will print Test with a boarder of *

    Arguments
        message - string value
        border - string value
    Returns (nothing)
    '''
    line = border * len(message)
    print(line)
    print(message)
    print(line)


def main(m,b):
    BANNER(m,b)
    print(" ")
    BANNER("if this was a real emergency ... you would be screwed")


if __name__ == '__main__':
    '''
        this program is an example that takes 2 argiments from the user and prints them by calling the main module passing those values
        and the main in turn calls the BANNER function
        after the initial printing of the args then main will call banner as well with its own input

    '''
    message = sys.argv[1]
    wrapper = sys.argv[2]
    main(message,wrapper)
