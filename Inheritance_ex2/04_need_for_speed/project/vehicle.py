class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = 1.25
        self.DEFAULT_FUEL_CONSUMPTION = self.fuel_consumption

    def drive(self, kilometers: int):
        potential_consumption = self.fuel_consumption * kilometers
        if self.fuel >= potential_consumption:
            self.fuel -= potential_consumption


