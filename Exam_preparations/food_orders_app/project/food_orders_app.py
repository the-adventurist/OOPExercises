from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    MINIMAL_COUNTS_OF_MEALS = 5

    def __init__(self):
        self.menu = []  # contains all meals
        self.clients = []  # contains all clients

    def register_client(self, client_phone_number: str):
        client_obj_obj = [c for c in self.clients if c.phone_number == client_phone_number]
        if client_obj_obj:
            raise Exception("The client has already been registered!")
        new_client_obj = Client(client_phone_number)
        self.clients.append(new_client_obj)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < self.MINIMAL_COUNTS_OF_MEALS:
            raise Exception("The menu is not ready!")

        result = ""
        for meal in self.menu:
            result += meal.details() + "\n"

        return result

