from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLES = [s.__name__ for s in BaseVehicle.__subclasses__()]
    VALID_VEHICLES_REFERENCES = [s for s in BaseVehicle.__subclasses__()]

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        registration = [u for u in self.users if u.driving_license_number == driving_license_number]
        if registration:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)

        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        already_present = [n for n in self.vehicles if n.license_plate_number == license_plate_number]
        if already_present:
            return f"{license_plate_number} belongs to another vehicle."

        class_vehicle = [cl for cl in self.VALID_VEHICLES_REFERENCES if cl.__name__ == vehicle_type]
        new_vehicle = class_vehicle[0](brand, model, license_plate_number, class_vehicle[0].MAX_MILEAGE)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self,start_point: str, end_point: str, length: float):
        existing_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                          if r.length == length]

        if existing_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        similar_route = [r for r in self.routes if r.start_point == start_point if r.end_point == end_point
                         if r.length < length]
        if similar_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        new_route = Route(start_point, end_point, length, route_id=len(self.routes) + 1)
        self.routes.append(new_route)
        longer_route = [r for r in self.routes if r.length > length]
        if longer_route:
            longer_route[0].is_locked = True

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int,  is_accident_happened: bool):
        this_route = [r for r in self.routes if r.is_locked is True]
        if this_route:
            self.routes.remove(this_route[0])
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        this_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number
                        if v.is_damaged is True]
        if this_vehicle:
            self.vehicles.remove(this_vehicle[0])
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        this_route = [r for r in self.routes if r.route_id == route_id if r.is_locked is True]
        if this_route:
            self.routes.remove(this_route[0])
            return f"Route {route_id} is locked! This trip is not allowed."

        drive_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
