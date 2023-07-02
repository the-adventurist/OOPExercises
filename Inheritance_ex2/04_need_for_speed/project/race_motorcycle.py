from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 8
        self.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers: int):
        potential_consumption = self.fuel_consumption * kilometers
        if self.fuel >= potential_consumption:
            self.fuel -= potential_consumption
