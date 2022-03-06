LOWER = 33
UPPER = 127


def main():
    char = input("Enter a character: ")
    while ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
        print("Invalid character! Try again")
        char = input("Enter a character: ")
    print(f"The ASCII code for {char} is {ord(char)}")

    num = int(input("Enter a number between 33 and 127: "))
    while num < LOWER or num > UPPER:
        print("Invalid number! Try again")
        num = int(input("Enter a number between 33 and 127: "))
    print(f"The character for {num} is {chr(num)}")

    for i in range(LOWER, UPPER + 1):
        print(f"{i:>3}  {chr(i)}")


main()
