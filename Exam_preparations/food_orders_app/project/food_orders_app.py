from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []  # contains all meals
        self.clients = []  # contains all clients

    def register_client(self, client_phone_number: str):
        result = self._check_for_registration(client_phone_number)
        if result:
            raise Exception("The client has already been registered!")
        new_client_obj = Client(client_phone_number)
        self.clients.append(new_client_obj)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_readiness_menu()
        client_obj_list = [c for c in self.clients if c.phone_number == client_phone_number]
        if not client_obj_list:
            self.register_client(client_phone_number)
        client_obj = [c for c in self.clients if c.phone_number == client_phone_number][0]

        temp_cart = []
        temp_bill = 0
        for meal_name, meal_qty in meal_names_and_quantities.items():
            for meal_menu in self.menu:
                if meal_name == meal_menu.name:
                    if meal_menu.quantity >= meal_qty:
                        temp_cart.append(meal_menu)
                        temp_bill += meal_menu.price * meal_qty
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal_menu).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client_obj.shopping_cart.extend(temp_cart)
        client_obj.bill += temp_bill

        for meal_name, meal_qty in meal_names_and_quantities.items():
            if meal_name not in client_obj.ordered_meals:
                client_obj.ordered_meals[meal_name] = 0
            client_obj.ordered_meals[meal_name] += meal_qty
            for meal in self.menu:
                if meal_name == meal.name:
                    meal.quantity -= meal_qty

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(p.name for p in client_obj.shopping_cart)} for {client_obj.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client_obj = [c for c in self.clients if c.phone_number == client_phone_number][0]
        if client_obj.shopping_cart:
            for order, qty in client_obj.oredered_meals.items():
                for meal_menu in self.menu:
                    if order == meal_menu.name:
                        meal_menu.quantity += qty
            client_obj.shopping_cart = []
            client_obj.ordered_meals = {}
            client_obj.bill = 0
        else:
            raise Exception("There are no ordered meals!")

    def finish_order(self, client_phone_number: str):
        client_obj = [c for c in self.clients if c.phone_number == client_phone_number][0]
        if client_obj.shopping_cart:
            self.receipt_id += 1
            total_pay = client_obj.bill
            client_obj.bill = 0
            client_obj.shopping_cart = []
            client_obj.ordered_meals = {}
            return f"Receipt #{self.receipt_id} with total amount of {total_pay:.2f}" \
                   f" was successfully paid for {client_phone_number}."
        else:
            raise Exception("There are no ordered meals!")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients)} clients."

    # helper methods and tools
    def _check_readiness_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    # HELPER METHODS AND TOOLS

    def _check_for_registration(self, phone_number):
        result = [c for c in self.clients if c.phone_number == phone_number]
        return result
