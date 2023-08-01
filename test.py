class Person:
    def __init__(self, age):
        self.age = age

    def change_age(self, new_age):
        self.age = new_age


anna = Person(43)
print(anna.age)

anna.change_age(23)
print(anna.age)