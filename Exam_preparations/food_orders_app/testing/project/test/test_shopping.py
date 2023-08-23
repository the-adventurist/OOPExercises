from project.shopping_cart import ShoppingCart

from unittest import TestCase

class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shop1 = ShoppingCart("Nanny", 50000)

    def test_correct_initializing(self):
        self.assertEqual("Nanny", self.shop1.shop_name)
        self.assertEqual(50000, self.shop1.budget)

    def test_incorrect_name_start_lower_case_letter(self):
        with self.assertRaises(ValueError) as ex:
            self.shop1.shop_name = "grosh"

        self.assertEqual(str(ex.exception),
                         "Shop must contain only letters and must start with capital letter!")

    def test_incorrect_name_with_number_in_it(self):
        with self.assertRaises(ValueError) as ex:
            self.shop1.shop_name = "4you"

        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

