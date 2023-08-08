from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=CargoVan.MAX_MILEAGE)

    def drive(self, mileage: float):
        reduce_battery_energy = round((mileage / self.max_mileage * 100) * 0.95)
        return self.battery_level - reduce_battery_energy

