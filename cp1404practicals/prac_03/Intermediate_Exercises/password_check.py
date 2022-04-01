MINIMUM_LENGTH = 6

user_password = input("Password: ")
while len(user_password) < MINIMUM_LENGTH:
    print("Password is too short! Try again!")
    user_password = input("Password: ")
for char in user_password:
    print("*", end="")
