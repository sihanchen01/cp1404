def main():
    name_to_address = {}

    username = input("Name: ").strip()
    address = input("Address: ")
    while username != "":
        if username in name_to_address:
            want_to_change = input(
                "Want to change address (Y/n) -> ").strip().lower()
            while want_to_change not in ["", "y", "yes", "no", "n"]:
                print("Invalid input, try again!")
                want_to_change = input(
                    "Want to change address (Y/n) -> ").strip().lower()
            if want_to_change in ["", "y", "yes"]:
                name_to_address[username] = input("New address: ")
            else:
                print(
                    f"Name: {username} - Address: {name_to_address[username]}")
        else:
            name_to_address[username] = address
        print()
        username = input("Name: ").strip()


if __name__ == "__main__":
    main()
