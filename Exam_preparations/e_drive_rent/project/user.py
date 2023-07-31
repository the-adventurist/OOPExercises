class User:
    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating: float = 0
        self.is_blocked: bool = False
        
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        if value.strip() == "":
            raise ValueError("First name cannot be empty!")

        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value.strip() == "":
            raise ValueError("Last name cannot be empty!")

        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if value.strip() == "":
            raise ValueError("Driving license number is required!")

        self.__driving_license_number = value

    def increase_rating(self):
        self.rating += 0.5
        if self.rating > 10:
            self.rating = 10

    def decrease_rating(self):
        self.rating -= 2
        if self.rating < 0:
            self.rating = 0
            self.is_blocked = True

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} Driving license: {self.__driving_license_number} " \
               f"Rating: {self.rating}"

# user1 = User("Georgi", "Georgiev", "fetsj5")
#
# print(user1)
