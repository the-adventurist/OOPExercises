from project.trip import Trip
from unittest import TestCase

class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(2000, 3, True)

    def test_corr_init(self):
        self.assertEqual(2000, self.trip1.budget)
        self.assertEqual(3, self.trip1.travelers)
        self.assertEqual(True, self.trip1.is_family)

    def test_invalid_travelers(self):
        with self.assertRaises(ValueError) as ex:
            self.trip1.travelers = 0
        self.assertEqual(str(ex.exception),
                         'At least one traveler is required!')

    def test_family_1_number(self):
        self.trip2 = Trip(200, 1, True)
        self.assertEqual(False, self.trip2._is_family)

