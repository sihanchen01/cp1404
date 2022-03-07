import math

LOWER = 33
UPPER = 127


def main():
    col = int(input("Enter the number of columns: "))

    # # PRINT ROW BY ROW
    # i = LOWER
    # while i <= UPPER:
    #     for _ in range(col):
    #         if i <= UPPER:
    #             print(f"{i:>3}  {chr(i)}", end="\t")
    #         i += 1
    #     print()

    # # ANOTHER WAY TO PRINT ROW BY ROW
    # row = math.floor((UPPER - LOWER + 1) / col)
    # for r in range(row):
    #     for c in range(col):
    #         index = LOWER + r*col + c
    #         print(f"{index:>3}  {chr(index)}", end="\t")
    #     print()
    # reminder = (UPPER - LOWER + 1) % col
    # if reminder:
    #     for reminder_ in range(reminder, 0, -1):
    #         index = UPPER - reminder_ + 1
    #         print(f"{index:>3}  {chr(index)}", end="\t")

    # PRINT COL BY COL
    row = math.ceil((UPPER - LOWER + 1) / col)
    for r in range(row):
        for c in range(col):
            index = LOWER + r + c*row
            if index <= UPPER:
                print(f"{index:>3}  {chr(index)}", end="\t")
        print()


main()
