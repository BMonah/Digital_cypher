import string
from itertools import cycle


def decode(code, key):
    dictionary = dict()
    for index, letter in enumerate(string.ascii_lowercase, 1):
        dictionary[index] = letter

    key = [int(i) for i in str(key)]
    corresponding_digits = [x1 - x2 for x1, x2 in zip(code, cycle(key))]

    corresponding_letter = [dictionary[x] for x in corresponding_digits]
    word = ''.join(corresponding_letter)
    return word
