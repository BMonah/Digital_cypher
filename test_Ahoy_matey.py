import unittest
from Ahoy_matey import Ship


class LootingTest(unittest.TestCase):

    def test_for_draft_greater_than_20(self):
        self.Zeus = Ship(50, 10)
        self.assertEqual(self.Zeus.is_worth_it(), True, msg='wrong testing method')

    def test_dor_draft_lesser_than_20(self):
        self.Titanic = Ship(30, 10)
        self.assertEqual(self.Titanic.is_worth_it(), False, msg='wrong testing method')

    def test_for_draft_equal_to_20(self):
        self.Titan = Ship(35, 15)
        self.assertEqual(self.Titan.is_worth_it(), False, msg='wrong testing method')

    def test_empty_ship(self):
        self.Sparta = Ship(0, 0)
        self.assertEqual(self.Sparta.is_worth_it(), False, msg='wrong testing method')

    def test_zero_draft(self):
        self.MVMombasa = Ship(15, 10)
        self.assertEqual(self.MVMombasa.is_worth_it(), False, msg='wrong testing method')
