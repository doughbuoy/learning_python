DIGIT_MAP = {
    'ZERO': '0',
    'ONE': '1',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9',
}
#--------------------------------------------------------------------------------------------------#
#  This is just a little more streamlined that 1 this removes thprint in the exception but creates a problem because nothing is indented
# IndentationError: expected an indented block
#  THE PASS OPERATOR IS NO-OP AND IS JUST PLACED TO HAVE THE INDENT but do nothing

#---------------------------------------------------------------------------------------------------#


def convert(s):
# SET INITIAL VALUE OF BAD RETURN
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"conversion success : x = {x}")
    except (KeyError, TypeError):
        pass
    return x


if __name__ == '__main__':
   a = convert("ONE THREE SEVEN NINE".split())
   print(a)
   b = convert("NINE")
   print(b)