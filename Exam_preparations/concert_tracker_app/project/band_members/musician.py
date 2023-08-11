from abc import ABC, abstractmethod


class Musician(ABC):
    ERROR_MSG_NAME = "Musician name cannot be empty!"
    ERROR_MSG_AGE = "Musicians should be at least 16 years old!"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, value):
            if value.strip() == "":
                raise ValueError(self.ERROR_MSG_NAME)
            self.__name = value

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, value):
            if value < 16:
                raise ValueError(self.ERROR_MSG_AGE)

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        ...

