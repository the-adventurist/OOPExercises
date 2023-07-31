from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle


class ManagingApp():
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

