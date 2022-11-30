import string
import random


def generate_password(pass_len:any):
    symbols = string.ascii_lowercase + string.ascii_uppercase + \
              string.digits + string.punctuation
    pass_len = int(pass_len)
    password = ''
    for i in range(pass_len):
        password += random.choice(symbols)
    return password