from abc import ABC, abstractmethod


class BaseService(ABC):
    MINIMAL_CAPACITY = 0

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Service name cannot be empty!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= self.MINIMAL_CAPACITY:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    @abstractmethod
    def details(self):
        ...
