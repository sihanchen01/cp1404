repeated_strings = []
check_list = []
user_input = input("Enter a string: ").strip()
while user_input != "":
    if user_input in check_list:
        repeated_strings.append(user_input)
    else:
        check_list.append(user_input)
    user_input = input("Enter a string: ").strip()

if repeated_strings:
    print(f"Strings repeated: {', '.join(repeated_strings)}")
else:
    print("No repeated strings entered.")
