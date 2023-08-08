from unittest import TestCase, main

#from car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.my_car = Car("Honda", "Jazz", 5, 35)

    def test_check_correct_initialization(self):
        self.assertEqual(self.my_car.make, "Honda")
        self.assertEqual(self.my_car.model, "Jazz")
        self.assertEqual(self.my_car.fuel_consumption, 5)
        self.assertEqual(self.my_car.fuel_capacity, 35)
        self.assertEqual(self.my_car.fuel_amount, 0)

    def test_attempt_to_set_invalid_make(self):

        with self.assertRaises(Exception) as ex:
            self.my_car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_attempt_to_set_invalid_model(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_less_than_zero_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_or_less_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_less_than_zero_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_zero_amount(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_amount(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_amount_not_to_exceed_capacity(self):
        self.my_car.fuel_amount = 25
        self.my_car.refuel(8)
        self.assertEqual(self.my_car.fuel_amount, 33)

    def test_refuel_with_amount_exceeded_capacity(self):
        self.my_car.fuel_amount = 25
        self.my_car.refuel(15)
        self.assertEqual(self.my_car.fuel_amount, 35)

    def test_drive_with_enough_fuel(self):
        self.my_car.fuel_amount = 10
        self.my_car.drive(2)
        self.assertEqual(self.my_car.fuel_amount, 9.9)

    def test_drive_without_enough_fuel(self):
        self.my_car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.my_car.drive(21)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()