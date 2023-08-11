from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player1 = TennisPlayer("Grigor", 26, 60)
        self.player2 = TennisPlayer("Agaci", 45, 70)
        self.wins = []

    def test_correct_initialization(self):
        self.assertEqual("Grigor", self.player1.name)
        self.assertEqual(26, self.player1.age)
        self.assertEqual(60, self.player1.points)

    def test_with_invalid_format_of_name(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.name = 'fd'

        self.assertEqual("Name should be more than 2 symbols!",
                         str(ex.exception))

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ex:
            self.player1.age = 14

        self.assertEqual("Players must be at least 18 years of age!",
                         str(ex.exception))

    def test_successfully_adding_name_to_wins_list(self):
        self.player1.add_new_win("Australian open")
        self.assertEqual(1, len(self.player1.wins))

    def test_adding_for_second_time_the_same_name_expected_falls(self):
        self.player1.add_new_win("Australian open")
        self.assertEqual("Australian open has been already"
                         " added to the list of wins!",
                         self.player1.add_new_win("Australian open"))

    def test__lt__happy_path(self):

        result = self.player1 < self.player2
        self.assertEqual(result, "Agaci is a top seeded player"
                         " and he/she is better than Grigor")

    def test_lt_another_case(self):
        self.player1.points = 90
        result = self.player1 < self.player2
        self.assertEqual(result, 'Grigor is a better player than Agaci')

    def test__str__without_tournament(self):
        expected = f"Tennis Player: Grigor\n" \
               f"Age: 26\n" \
               f"Points: 60.0\n" \
               f"Tournaments won: "
        result = str(self.player1)
        self.assertEqual(expected, result)

    def test__str__with_tournament(self):
        self.player1.wins.append("Australian open")
        expected = f"Tennis Player: Grigor\n" \
               f"Age: 26\n" \
               f"Points: 60.0\n" \
               f"Tournaments won: Australian open"
        result = str(self.player1)
        self.assertEqual(expected, result)

    def test__str__with_two_tournament(self):
            self.player1.wins.append("Australian open")
            self.player1.wins.append("American open")
            expected = f"Tennis Player: Grigor\n" \
                   f"Age: 26\n" \
                   f"Points: 60.0\n" \
                   f"Tournaments won: Australian open, American open"
            result = str(self.player1)
            self.assertEqual(expected, result)

if __name__ == '__main__':
    main()