name = input("Enter name: ")

MENU = """(H)ello
(G)oodbye
(Q)uit"""

print(MENU)
user_choice = input(">>> ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {name}")
    elif user_choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").upper()
print("Finished.")
