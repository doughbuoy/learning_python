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
#  This is just a little more streamlined that 1 by getting rid of code duplicattion
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
        print(f"Exception Caught - Conversion Fail : x = {x}")

    return x


if __name__ == '__main__':
   a = convert("ONE THREE SEVEN NINE".split())
   print(a)
   b = convert(167)
   print(b)