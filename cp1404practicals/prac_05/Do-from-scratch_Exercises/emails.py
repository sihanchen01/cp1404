name_to_email = {}

user_email = input("Email: ")
while user_email != "":
    username = " ".join(user_email.split("@")[0].split(".")).title()
    confirm = input(f"Is your name {username}? (Y/n) ").lower()
    if confirm not in ["", "y"]:
        username = input("Name: ")
    name_to_email[username] = user_email
    user_email = input("Email: ")

print()
for name, email in name_to_email.items():
    print(f"{name} ({email})")
