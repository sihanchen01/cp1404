from datetime import date

# # Version 1

# NUMBER_OF_PEOPLE = 5

# name_to_dob = {}
# for _ in range(NUMBER_OF_PEOPLE):
#     name = input("Name: ")
#     dob = input("DOB (MM/DD/YYYY): ")
#     name_to_dob[name] = dob

# print()
# for name, dob in name_to_dob.items():
#     age = date.today().year - int(dob.split("/")[-1])
#     print(f"{name} is {age} years old.")


# Version 2, I/O added
FILENAME = "name_to_dob.txt"

name_to_dob = {}
with open(FILENAME, "r") as rf:
    for line in rf:
        name, dob = line.split()
        name_to_dob[name] = dob

with open("ages.txt", "w") as wf:
    for name, dob in name_to_dob.items():
        age = date.today().year - int(dob.split("/")[-1])
        wf.write(f"{name} is {age} years old.\n")

print("Completed!")
