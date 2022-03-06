# 1.
with open("name.txt", "w") as wf:
    user_name = input("Enter your name: ")
    wf.write(f"Your name is {user_name}")

# 2.
with open("name.txt", "r") as rf:
    print(rf.read())

# 3.
with open("numbers.txt", "r") as rf:
    num1 = int(rf.readline())
    num2 = int(rf.readline())
    print(f"The sum of first two numbers is: {num1 + num2}")

# 4.
with open("numbers.txt", "r") as rf:
    sum = 0
    for line in rf:
        sum += int(line)
    print(f"The sum of all numbers is: {sum}")
