import math

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

while x < y:
    # i. Show the even numbers from x to y
    print(f"The even numbers from {x} to {y} are:")
    if x % 2 == 0:
        for i in range(x, y+1, 2):
            print(i, end=" ")
    else:
        for i in range(x+1, y+1, 2):
            print(i, end=" ")
    print()
    # ii. Show the odd numbers from x to y
    print(f"The odd numbers from {x} to {y} are:")
    if x % 2 == 0:
        for i in range(x+1, y+1, 2):
            print(i, end=" ")
    else:
        for i in range(x, y+1, 2):
            print(i, end=" ")
    print()

    # iii. Show the squares from x to y
    print(f"The squaures from {x} to {y} are:")
    first_root = math.ceil(math.sqrt(x))
    first_square = first_root ** 2
    if first_square > y:
        print("None")
    else:
        square = first_square
        root = first_root
        while square <= y:
            print(square, end=" ")
            root += 1
            square = root ** 2
    print()

    # Start next loop
    x = int(input("Enter value for x: "))
    y = int(input("Enter value for y: "))

# iv. Exit the program
print("Finished.")
