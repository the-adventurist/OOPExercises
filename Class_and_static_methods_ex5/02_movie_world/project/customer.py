from typing import List


class Customer:
    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: List[dvd] = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's " \
               f"({', '.join(d.name for d in self.rented_dvds)})"

