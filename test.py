class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()