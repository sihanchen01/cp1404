import random


def main():
    # method 1
    # return True if random.randint(1, 2) == 1 else False

    # method 2
    # return random.choice([True, False])

    # method 3
    return bool(random.getrandbits(1))
