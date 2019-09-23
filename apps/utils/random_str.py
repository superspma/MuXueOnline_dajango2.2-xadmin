import string
from random import choice


def gencrate_random(random_length, type):
    if type == 0:
        random_seed = string.digits
    elif type == 1:
        random_seed = string.digits + string.ascii_letters
    elif type == 2:
        random_seed = string.digits + string.ascii_letters + string.punctuation
    randon_str = []
    while len(randon_str) < random_length:
        randon_str.append(choice(random_seed))
    return ''.join(randon_str)

if __name__ == '__main__':
    print(gencrate_random(4,0))
