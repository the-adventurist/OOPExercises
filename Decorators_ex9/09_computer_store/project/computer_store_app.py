from abc import ABC, abstractmethod

from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp(DesktopComputer, Laptop):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer != "DesktopComputer" or type_computer != "Laptop":
            raise ValueError(f"{type_computer} is not a valid type computer!")
        else:
            pass
