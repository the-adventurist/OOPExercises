from project.car import Car


class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers: int):
        potential_consumption = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        if self.fuel >= potential_consumption:
            self.fuel -= potential_consumption