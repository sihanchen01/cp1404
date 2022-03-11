from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi(
    "Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

MENU = """q)uit, c)hoose taxi, d)rive"""


class TaxiSimulator:
    current_taxi: Taxi = None
    bill = 0

    def drive(self):
        if self.current_taxi:
            distance = float(input("Drive how far? "))
            self.current_taxi.drive(distance=distance)
            print(
                f"Your {self.current_taxi.name} trip cost you ${self.current_taxi.get_fare():.2f}")
            self.update_bill()
        else:
            print("You need to choose a taxi before you can drive")

    def get_taxis_infos(self):
        for index, taxi in enumerate(TAXIS):
            print(str(index) + " - " + str(taxi))

    def choose_taxi(self):
        print("Taxis available:")
        self.get_taxis_infos()
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice >= len(TAXIS) or taxi_choice < 0:
            print("Invalid taxi choice")
        else:
            self.current_taxi = TAXIS[taxi_choice]
            self.current_taxi.start_fare()

    def update_bill(self) -> None:
        if self.current_taxi:
            self.bill += self.current_taxi.get_fare()

    def print_bill(self):
        print(f"Bill to date: ${self.bill:.2f}")

    def get_exit_message(self):
        print(f"Total trip cose: ${self.bill:.2f}")
        print('Taxis are now:')
        self.get_taxis_infos()

    def play(self):
        print("Let's drive!")
        print(MENU)
        user_choice = input(">>> ").lower()
        while user_choice != "q":
            if user_choice == "d":
                self.drive()
            elif user_choice == "c":
                self.choose_taxi()
            else:
                print("Invalid option")
            self.print_bill()
            print(MENU)
            user_choice = input(">>> ").lower()
        self.get_exit_message()


if __name__ == "__main__":
    s = TaxiSimulator()
    s.play()
