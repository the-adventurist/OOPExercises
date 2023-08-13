from project.toy_store import ToyStore
from unittest import TestCase, main

class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy1 = ToyStore()
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_toy_shelf_H_fail(self):
        with self.assertRaises(Exception) as ex:
            self.toy1.add_toy("H", "Fox")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_toy_is_already_put(self):
        self.toy1.toy_shelf["A"] = "Bear"
        with self.assertRaises(Exception) as ex:
            self.toy1.add_toy("A", "Bear")

        self.assertEqual(str(ex.exception),
                         "Toy is already in shelf!")

    def test_toy_shelf_is_taken(self):
        self.toy1.toy_shelf["B"] = "Fox"
        with self.assertRaises(Exception) as ex:
            self.toy1.add_toy("B", "Hipo")

        self.assertEqual(str(ex.exception),
                         "Shelf is already taken!")

    def test_toy_shelf_A(self):
        result = self.toy1.add_toy("A", "Bear")
        self.assertEqual("Bear", self.toy1.toy_shelf["A"])
        self.assertEqual(result, "Toy:Bear placed successfully!")

    def test_remove_toy_shelf_doesnt_exist_fail(self):
        with self.assertRaises(Exception) as ex:
            self.toy1.remove_toy("H", "Bear")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_doesnt_exist_fail(self):
        with self.assertRaises(Exception) as ex:
            self.toy1.remove_toy("A", "Bear")
        self.assertEqual(str(ex.exception),
                         "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.toy1.toy_shelf["A"] = "Bear"
        result = self.toy1.remove_toy("A", "Bear")
        self.assertEqual(None, self.toy_shelf["A"])
        self.assertEqual(result, "Remove toy:Bear successfully!")
        self.assertEqual(self.toy1.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

if __name__ == '__main__':
    main()