import sys
from math import log
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
#  uses the "as" to get more details around the exception
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
    except (KeyError, TypeError) as error:
        print (f"Conversion Error : {error!r}",
            file=sys.stderr)
#instead of returning a value this just reraises the exception
        raise
    return x
def string_log(s):
    v = convert(s)
    return(log(v))


if __name__ == '__main__':
   a = string_log("ONE THREE SEVEN NINE".split())
   print(a)
   b = string_log("NINE SEVEN TWO".split())
   print(b)
   c = string_log("ONE MONKEY".split())