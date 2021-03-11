import unittest
from fifteen import Fifteen


class TestFifteen(unittest.TestCase):
    def test_initial_state(self):
        size = 4
        fifteen = Fifteen(size)
        self.assertEqual(fifteen.field[-1][-1], 0)

        for i in range(15):
            self.assertEqual(fifteen.get_value_at(i % size, i // size), str(i + 1))

    def test_move(self):
        size = 4
        fifteen = Fifteen(size)

        self.assertEqual(fifteen.is_win(), True)

        fifteen.move(3, 2)
        self.assertEqual(fifteen.get_value_at(3, 2), "")
        self.assertEqual(fifteen.get_value_at(3, 3), "12")

        fifteen.move(2, 2)
        self.assertEqual(fifteen.get_value_at(2, 2), "")
        self.assertEqual(fifteen.get_value_at(3, 2), "11")

        fifteen.move(1, 1)
        self.assertEqual(fifteen.get_value_at(2, 2), "")
        self.assertEqual(fifteen.get_value_at(3, 2), "11")

        self.assertEqual(fifteen.is_win(), False)
        fifteen.move(3, 2)
        self.assertEqual(fifteen.is_win(), False)
        fifteen.move(3, 3)
        self.assertEqual(fifteen.is_win(), True)
