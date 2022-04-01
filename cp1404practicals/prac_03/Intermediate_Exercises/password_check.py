"""Module docstring"""
# imports
# CONSTANTS
MINIMUM_LENGTH = 6


def main():
    user_password = get_password()
    print_astericks(user_password)


def print_astericks(user_password):
    for char in user_password:
        print("*", end="")


def get_password():
    user_password = input("Password: ")
    while len(user_password) < MINIMUM_LENGTH:
        print("Password is too short! Try again!")
        user_password = input("Password: ")
    return user_password


main()
