from typing import Dict

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int,) -> None:
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[str: int] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value:
            self.__dough = value
        else:
            raise ValueError("You should add dough to the pizza")

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value > 0:
            self.__max_number_of_toppings = value
        else:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

    def add_topping(self, topping: Topping):
        if self.__max_number_of_toppings == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        this_topping = [t for t in self.toppings if topping.topping_type == t]
        if this_topping:
            this_topping_name = this_topping[0]
            self.toppings[this_topping_name] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self) -> str:
        topping_weight = sum([w for w in self.toppings.values()])
        total_pizza_weight = topping_weight + self.dough.weight
        return total_pizza_weight

