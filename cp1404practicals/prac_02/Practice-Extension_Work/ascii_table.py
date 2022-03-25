LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    while ord(char) < LOWER or ord(char) > UPPER:
        print("Invalid character! Try again")
        char = input("Enter a character: ")
    print(f"The ASCII code for {char} is {ord(char)}")

    num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    while num < LOWER or num > UPPER:
        print("Invalid number! Try again")
        num = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
    print(f"The character for {num} is {chr(num)}")

    for i in range(LOWER, UPPER + 1):
        print(f"{i:>3}  {chr(i)}")


main()
