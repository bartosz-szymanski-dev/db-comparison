import string
import random


def get_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))
