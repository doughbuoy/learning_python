def sqrt(x):
    """ Comput square roots using old method 
    
    args: 
        x is the #
    
    returns 
        quare root 
    """

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


    def main():
        print(sqrt(9))
        print(sqrt(2))

    if __name__ == '__main__'
        main()