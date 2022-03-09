from car import Car

CHOICES = ["d", "r", "q"]
WELCOME = """
Let's drive!
Enter your car name: """
MENU = """Menu:
d) drive
r) refuel
q) quit
Enter your choice: """


def main():
    car = create_car()

    show_car_info(car)
    user_choice = input(MENU)
    while user_choice != "q":
        if user_choice == "d":
            drive_car(car)
        elif user_choice == "r":
            refuel_car(car)
        else:
            print("Invalid choice")
        print()
        show_car_info(car)
        user_choice = input(MENU)

    print(f"\nGood bye {car.name}'s driver.")


def create_car() -> Car:
    car_name = input(WELCOME)
    return Car(fuel=100, name=car_name)


def show_car_info(car: Car) -> None:
    print(f"{car.name}, fuel={car.fuel}, odo={car.odometer}")


def drive_car(car: Car) -> None:
    distance = validate_number(
        "How many km do you wish to drive? ", "Distance")
    if distance > car.fuel:
        print(f"The car drove {car.fuel}km and ran out of fuel.")
    else:
        print(f"The car drove {distance}km.")
    car.drive(distance)


def refuel_car(car: Car) -> None:
    refuel_amount = validate_number(
        "How many units of fuel do you want to add to the car? ", "Fuel amount")
    car.add_fuel(refuel_amount)
    print(f"Added {refuel_amount} units of fuel.")


def validate_number(prompt: str, subject: str) -> int:
    """looping prompt for user input until a valid input, return the valid integer"""
    user_input = int(input(prompt))
    while user_input < 0:
        print(f"{subject} must be >= 0")
        user_input = int(input(prompt))
    return user_input


if __name__ == "__main__":
    main()
