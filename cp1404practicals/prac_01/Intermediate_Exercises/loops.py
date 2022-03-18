for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b. count down from 20 to 1
for i in range(20, 0):
    print(i, end=" ")
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
num = int(input("Number of stars: "))
for _ in range(num):
    print("*", end="")
print()

# d. print n lines of increasing stars. Using the same number as above print lines of increasing stars, starting at 1.
# Example: if 4 was the number entered, your single loop should print
lines = int(input("Number of lines: "))
for line in range(lines):
    for _ in range(line + 1):
        print("*", end="")
    print()
