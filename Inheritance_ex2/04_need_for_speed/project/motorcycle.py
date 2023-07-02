from project.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 1.25
        self.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers: int):
        potential_consumption = self.fuel_consumption * kilometers
        if self.fuel >= potential_consumption:
            self.fuel -= potential_consumption
