from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver1 = TruckDriver("Alan", 23)

    def test_correct_initialization(self):
        self.assertEqual("Alan", self.driver1.name)
        self.assertEqual(23, self.driver1.money_per_mile)

    def test_pass_positive_earned_money(self):
        result = self.driver1.earned_money = 3500
        self.assertEqual(3500, result)

    def test_pass_negative_earned_money(self):
        with self.assertRaises(ValueError) as ex:
            self.driver1.earned_money = -1400

        self.assertEqual(str(ex.exception), "Alan went bankrupt.")

    def test_already_add_cargo_offer_expects_error(self):
        self.driver1.available_cargos = {"Chicago", 145}
        with self.assertRaises(Exception) as ex:
            self.driver1.add_cargo_offer("Chicago", 145)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_adding_cargo(self):
        self.driver1.available_cargos = {"Chicago": 145}
        result = self.driver1.add_cargo_offer("Minnesota", 525)
        self.assertEqual({"Chicago": 145, "Minnesota": 525},
                         self.driver1.available_cargos)
        self.assertEqual(result,
                             "Cargo for 525 to Minnesota was added as an offer.")

    def test_drive_best_offer(self):
        self.driver1.available_cargos = {
            "Chicago": 145,
            "Minnesota": 700,
            "Atlanta": 443
        }
        self.driver1.earned_money = 0
        result = self.driver1.drive_best_cargo_offer()
        self.assertEqual(result, "Alan is driving 700 to Minnesota.")
        self.assertEqual(16060, self.driver1.earned_money)
        self.assertEqual(700, self.driver1.miles)

    def test_drive_best_cargo_fail(self):
        self.driver1.drive_best_cargo_offer()
        self.assertEqual(self.driver1.drive_best_cargo_offer(),
                         "There are no offers available.")

    def test_eat_without_changing_earned_money(self):
        self.driver1.earned_money = 1000
        self.driver1.miles = 249
        self.driver1.eat(self.driver1.miles)
        self.assertEqual(1000, self.driver1.earned_money)

    def test_eat_with_one_changing_earned_money(self):
        self.driver1.earned_money = 1000
        self.driver1.miles = 250
        self.driver1.eat(self.driver1.miles)
        self.assertEqual(980, self.driver1.earned_money)

    def test_eat_with_two_changing_earned_money(self):
        self.driver1.earned_money = 1000
        self.driver1.miles = 250
        self.driver1.eat(self.driver1.miles)
        self.driver1.miles = 500
        self.driver1.eat(self.driver1.miles)
        self.assertEqual(960, self.driver1.earned_money)

    def test_sleep(self):
        self.driver1.earned_money = 1000
        self.driver1.sleep(1000)
        self.assertEqual(955, self.driver1.earned_money)
        self.driver1.sleep(2000)
        self.assertEqual(910, self.driver1.earned_money)

    def test_pump_gas(self):
        self.driver1.earned_money = 1000
        self.driver1.pump_gas(1500)
        self.assertEqual(500, self.driver1.earned_money)

    def test_repair_truck(self):
        self.driver1.earned_money = 20000
        self.driver1.repair_truck(10000)
        self.driver1.repair_truck(20000)
        self.assertEqual(5000, self.driver1.earned_money)

    def test__repr__(self):
        self.assertEqual(str(self.driver1), "Alan has 0 miles behind his back.")

