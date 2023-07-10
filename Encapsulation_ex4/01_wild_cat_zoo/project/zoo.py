from typing import List, Union

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Union[Tiger, Lion, Cheetah]] = []
        self.workers: List[Union[Keeper, Caretaker, Vet]] = []

    def add_animal(self, animal: Union[Tiger, Lion, Cheetah], price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Union[Keeper, Vet, Caretaker]) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        this_worker = [w for w in self.workers if w.name == worker_name]
        try:
            this_worker = this_worker[0]
            self.workers.remove(this_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum([s.salary for s in self.workers])
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_spends_for_bring_out_animals = sum([r.money_for_care for r in self.animals])
        if total_spends_for_bring_out_animals <= self.__budget:
            self.__budget -= total_spends_for_bring_out_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"

        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [ch for ch in self.animals if ch.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"

        for l in lions:
            result += f"Name: {l.name}, Age: {l.age}, Gender: {l.gender}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for t in tigers:
            result += f"Name: {t.name}, Age: {t.age}, Gender: {t.gender}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"

        for ch in cheetahs:
            result += f"Name: {ch.name}, Age: {ch.age}, Gender: {ch.gender}\n"

        return result[:-1]

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"

        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"

        for k in keepers:
            result += f"Name: {k.name}, Age: {k.age}, Salary: {k.salary}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for c in caretakers:
            result += f"Name: {c.name}, Age: {c.age}, Salary: {c.salary}\n"

        result += f"----- {len(keepers)} Vets:\n"

        for v in vets:
            result += f"Name: {v.name}, Age: {v.age}, Salary: {v.salary}\n"

        return result[:-1]