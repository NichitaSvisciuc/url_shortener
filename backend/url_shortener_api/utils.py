import string
import random

from .constants import DEFAULT_RANDOM_SHORTENED_STRING_LENGTH


def generate_random_string():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(DEFAULT_RANDOM_SHORTENED_STRING_LENGTH))
    return random_string
