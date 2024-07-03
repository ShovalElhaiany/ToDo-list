import random
import string


def generate_secret_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))