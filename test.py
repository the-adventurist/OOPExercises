class Person:
    def __init__(self, name, age, id_card, insurance_number):
        self.name = name
        self.age = age
        self.id_card = id_card
        self.insurance_number = insurance_number


person = Person("Ivan", 23, 324, "D343")
delattr(person, "insurance_number")
print(person.insurance_number)