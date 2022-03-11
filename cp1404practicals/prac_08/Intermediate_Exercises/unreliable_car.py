from dis import dis
from car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name: str, fuel: float, reliability: float):
        """UnreliableCar has a reliability, a float from 0 to 100, 
        that represents the percentage chance that the drive method will actually work."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            print("Lucky, the car moved!")
            super().drive(distance)
        else:
            print("Unlucky, the car didn't move.")
            return 0
