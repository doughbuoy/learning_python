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
        print(f"guessing: {guess}")
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))

    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cant calc root of a negitve number")
    print("Program continues")


if __name__ == '__main__':
    main()