def BANNER(message, border='-'):
    ''' Purpose: this function prints a border around the argument message
        for example BANNER("Test") will print Test with a boarder of -
        whereas BANNER("Test", "*") will print Test with a boarder of *

        Arguments
            message - string value
            border - string value
        Returns (nothing)
    '''
    line = boarder * len(message)
    print(line)
    print(message)
    print(line)

    if __name__ == '__main__':
        BANNER("Test of the Emergency Broadcast System")    
