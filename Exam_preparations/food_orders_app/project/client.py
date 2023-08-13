class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []  # contains meals (objects) added to the client
        self.bill = 0.0  # total amount of money for all meals added to the cart

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or int(value[0]) != 0 or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

