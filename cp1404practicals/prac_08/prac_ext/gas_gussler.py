from car import Car
import random


class GasGussler(Car):

    def drive(self, distance: float) -> float:
        """Gasgussler car uses 20% to 50% more gas"""
        coefficient: float = random.uniform(1.2, 1.5)

        if distance * coefficient > self.fuel:
            distance = self.fuel / coefficient
            self.fuel = 0
        else:
            self.fuel -= distance * coefficient
        self.odometer += distance
        return distance
