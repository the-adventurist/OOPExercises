from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []  # takes boots objects
        self.delicacies = []  # takes boots objects
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        self._check_existence_by_name(name, self.delicacies)
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        new_delicacy_obj = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy_obj)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        self._check_existence_by_booth_number(booth_number, self.booths)
        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth_obj = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth_obj)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth_obj_list = [b for b in self.booths if not b.is_reserved if b.capacity >= number_of_people]
        if not booth_obj_list:
            raise Exception(f"No available booth for {number_of_people} people!")
        booth_obj = booth_obj_list[0]
        booth_obj.reserve(number_of_people)
        return f"Booth {booth_obj.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        self._check_no_existence_by_booth_number(booth_number, self.booths)
        self._check_no_existence_by_name(delicacy_name, self.delicacies)
        delicacy_obj = self._find_obj_by_name(delicacy_name, self.delicacies)
        booth_obj = self._find_obj_by_number(booth_number, self.booths)
        booth_obj.delicacy_orders.append(delicacy_obj)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth_obj = self._find_obj_by_number(booth_number, self.booths)
        total_income = booth_obj.price_for_reservation
        total_income += sum([d.price for d in booth_obj.delicacy_orders])
        self.income += total_income
        booth_obj.undo_reservation()
        return f"Booth {booth_number}:\nBill: {total_income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."



    # helper methods and tools

    @staticmethod
    def _check_existence_by_name(name, collection):
        obj_list = [o for o in collection if o.name == name]
        if obj_list:
            raise Exception(f"{name} already exists!")

    @staticmethod
    def _check_no_existence_by_name(name, collection):
        obj_list = [o for o in collection if o.name == name]
        if not obj_list:
            raise Exception(f"No {name} in the pastry shop!")

    @staticmethod
    def _check_existence_by_booth_number(number, collection):
        obj = [o for o in collection if o.booth_number == number]
        if obj:
            raise Exception(f"Booth number {number} already exists!")

    @staticmethod
    def _check_no_existence_by_booth_number(number, collection):
        obj = [o for o in collection if o.booth_number == number]
        if not obj:
            raise Exception(f"Could not find booth {number}!")

    @staticmethod
    def _find_obj_by_name(name, collection):  # the object will always exist
        obj = [o for o in collection if o.name == name][0]
        return obj

    @staticmethod
    def _find_obj_by_number(number, collection):  # the object will always exist
        obj = [o for o in collection if o.booth_number == number][0]
        return obj

