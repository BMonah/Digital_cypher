import unittest
from Elevators import elevator


class TestElevator(unittest.TestCase):
    def test_near_left_elevator(self):
        self.case1 = elevator(0, 1, 0)
        self.assertEqual(self.case1, 'left')

    def test_equally_distant(self):
        self.case2 = elevator(0, 1, 2)
        self.assertEqual(self.case2, 'right')
        self.case3 = elevator(0, 0, 0)
        self.assertEqual(self.case3, 'right')
        self.case4 = elevator(0, 2, 1)
        self.assertEqual(self.case4, 'right')

    def test_near_right_elevator(self):
        self.case5 = elevator(0, 1, 1)
        self.assertEqual(self.case5, 'right')
