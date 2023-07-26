from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def food_that_eats(self) -> List[Food]:
        ...

    @property
    @abstractmethod
    def gained_weight(self) -> float:
        ...

    @abstractmethod
    def make_sound(self) -> str:
        ...

    

class Bird(Animal, ABC):
    pass