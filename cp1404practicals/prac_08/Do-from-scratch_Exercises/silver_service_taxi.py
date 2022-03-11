from taxi import Taxi


class SilverServiceTaxi(Taxi):
    # extra charge for each new fare
    flagfall = 4.5

    def __init__(self, name: str, fuel: float, fanciness: float):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
