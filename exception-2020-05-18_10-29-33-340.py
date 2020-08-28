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


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"conversion success : x = {x}")
    except KeyError:
        x = -1
        print(f"Conversion Fail : x = {x}")
    return x


if __name__ == '__main__':
   a = convert("ONE THREE SEVEN NINE".split())
   print(a)
   b = convert(167)
   print(b)