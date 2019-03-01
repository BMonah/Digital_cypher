import unittest
from Digital_Cypher import decode


class TestDigitalCypher(unittest.TestCase):

    def test_word_greater_than_key(self):
        self.greater = decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939)
        self.assertEqual(self.greater, 'masterpiece')

    def test_word_equal_to_key(self):
        self.equal = decode([3, 24, 18, 22], 1939)
        self.assertEqual(self.equal, 'boom')

    def test_word_lesser_than_key(self):
        self.lesser = decode([9, 14, 28], 1939)
        self.assertEqual(self.lesser, 'hey')
