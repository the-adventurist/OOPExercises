from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name= name
        self.country= country
        self.advantage= advantage
        self.budget= budget
        self.wins= 0
        self.equipment = []  # take equipment objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    def get_total_equipment_price(self):
        total_price = sum([e.price for e in self.equipment])
        return total_price

    def _get_avr_protection(self):
        avr_protection = 0
        if self.equipment:
            avr_protection = sum([e.protection for e in self.equipment]) / len(self.equipment)
            return avr_protection
        return avr_protection

    def get_total_protection(self):
        total_protection = sum([e.protection for e in self.equipment])
        return total_protection

    def get_statistics(self):
        return f"""Name: {self.name}
Country: {self.country}
Advantage: {self.advantage} points
Budget: {self.budget:.2f}EUR
Wins: {self.wins}
Total Equipment Price: {self.get_total_equipment_price():.2f}
Average Protection: {int(self._get_avr_protection())}"""

