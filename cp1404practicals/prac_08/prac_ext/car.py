"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self,  name: str = "Car",  fuel: float = 0) -> None:
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.odometer = 0
        # 7. Add a name field
        self.name = name

    # 6. Now add the __str__ method to the Car class in car.py.
    def __str__(self) -> str:
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount: float) -> None:
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance: float) -> float:
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
