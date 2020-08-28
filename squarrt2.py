import sys
def sqrt(x):
    """ Comput square roots using old method 
    
    args: 
        x is the #
    
    returns 
        quare root
    raise
        value error when negit number processing is attempted 
    """

    if x < 0:
        raise ValueError(
            "Cannot Compute value of an "
            f"Negitive {x}"
        )
    guess = x
    i = 0
    while guess * guess != x and i < 20:

        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():


    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program continues")


if __name__ == '__main__':
    main()