import random

NUMBER_OF_PICKS = int(input("How many quick picks? "))
COLUMN_NUMBER = 6
LOW = 1
HIGH = 45

result = []

for _ in range(NUMBER_OF_PICKS):
    row_list = []
    for _ in range(COLUMN_NUMBER):
        random_number = random.randint(1, 45)
        while random_number in row_list:
            random_number = random.randint(1, 45)
        row_list.append(random_number)
    row_list.sort()
    result.append(row_list)

for row in result:
    for col in row:
        print(f"{col:>2}", end=" ")
    print()
