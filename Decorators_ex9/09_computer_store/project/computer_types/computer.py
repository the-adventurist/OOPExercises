from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def __init__(self, manufacturer: str, model: str):
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value:
            raise ValueError("Manufacturer name cannot be empty.")
        else:
            self.__manufacturer = value
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if not value:
            raise ValueError("Model name cannot be empty.")
        else:
            self.__model = value

    @abstractmethod
    def configure_computer(self, *args, **kwargs):
        ...

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

