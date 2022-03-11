from car import Car


class Bomb(Car):

    def drive(self, distance: float) -> float:
        if distance > self.fuel:
            self.fuel = 0
        else:
            self.fuel -= distance
        return 0
