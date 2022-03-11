from taxi import Taxi


class EcoTaxi(Taxi):
    fuel_efficiency = 0.5
    discount = 0.2

    def drive(self, distance):
        if distance * self.fuel_efficiency > self.fuel:
            distance = self.fuel / self.fuel_efficiency
            self.fuel = 0
        else:
            self.fuel -= distance * self.fuel_efficiency
        self.odometer += distance
        self.current_fare_distance += distance
        return distance
