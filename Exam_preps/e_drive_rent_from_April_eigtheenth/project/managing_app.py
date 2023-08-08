from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    _vehicle_types = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        already_registered = [u for u in self.users if u.driving_license_number == driving_license_number]

        if already_registered:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self._vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        doubled_license_plate_number = [n for n in self.vehicles if n.license_plate_number == license_plate_number]
        if doubled_license_plate_number:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self._vehicle_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        exact_the_same_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                                if r.length == length]
        if exact_the_same_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        shorter_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                         if r.length < length]
        longer_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                        if r.length > length]

        if shorter_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        longer_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                        if r.length > length]
        if longer_route:
            longer_route[0].is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        driver = [d for d in self.users if d.driving_license_number == driving_license_number if not d.is_blocked]
        if not driver:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number if not v.is_damaged]
        if not vehicle:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [r for r in self.routes if r.route_id == route_id if not r.is_locked]
        if not route:
            return f"Route {route_id} is locked! This trip is not allowed."

        driver = driver[0]
        vehicle = vehicle[0]
        route = route[0]

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            driver.decrease_rating()
        else:
            driver.increase_rating()

        status = "OK" if not vehicle.is_damaged else "Damaged"
        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number}" \
               f" Battery: {vehicle.battery_level}% Status: {status}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        ordered_damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        repaired_vehicles = 0
        for damaged_vehicle in ordered_damaged_vehicles:
            repaired_vehicles += 1
            if repaired_vehicles <= count:
                damaged_vehicle.change_status()
                damaged_vehicle.recharge()

        return f"{repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        text_for_print = "*** E-Drive-Rent ***" + "\n"

        ordered_users = sorted(self.users, key=lambda x: -x.rating)
        text_for_print += '\n'.join([u.__str__() for u in ordered_users])

        return text_for_print
