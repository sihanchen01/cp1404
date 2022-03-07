
NUMBER_COUNTS = int(input("How many numbers? "))
while NUMBER_COUNTS >= 0:
    if NUMBER_COUNTS == 0:
        print("It can't be 0! Try again.")
    else:
        numbers = []
        for i in range(1, NUMBER_COUNTS+1):
            number = int(input(f"Number {i}: "))
            numbers.append(number)

        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    NUMBER_COUNTS = int(input("How many numbers? "))

print("Finished.")
