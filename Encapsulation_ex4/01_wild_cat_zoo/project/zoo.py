from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name: str = name
        self.__budget: int = budget
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        is_budget = self.__budget >= price
        is_free_space = self.__animal_capacity > len(self.animals)

        if is_budget and is_free_space:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_free_space and not is_budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name:str) -> str:
        this_worker = [w for w in self.workers if w.name == worker_name][0]
        try:
            self.workers.remove(this_worker)
            return f"{this_worker.name} fired successfully"
        except ValueError:
            return  f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        payslips = sum([pay.salary for pay in self.workers])
        if payslips <= self.__budget:
            self.__budget -= payslips
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def profit_amount(self, amount):
        self.__budget += amount

    def animal_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"

        for l in lions:
            result += f"{l}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for t in tigers:
            result += f"{t}\n"

        result += f"----- {len(cheetahs)} Cheetahs:"

        for ch in cheetahs:
            result += f"{ch}\n"

        return result[:-1]

