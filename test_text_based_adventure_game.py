import unittest
from text_based_adventure_game import adventure_game


class TestAdventureGame(unittest.TestCase):

    def test_room_movement(self):
        self.room = adventure_game('starting', 'north')
        self.assertEqual(self.room, 'you are in the booby trap room \nA dead lion hanging on a leg-hold trap')

        self.room = adventure_game('booby trap', 'west')
        self.assertEqual(self.room,
                         'you are in the weapon room \nsub machine guns, m13s, and riffles hanged on the wall')

        self.room = adventure_game('booby trap', 'south')
        self.assertEqual(self.room, 'you are in the starting zone \ngiant wooden door ahead, no sign of people')

        self.room = adventure_game('weapons', 'east')
        self.assertEqual(self.room, 'you are in the booby trap room \nA dead lion hanging on a leg-hold trap')

    def test_walls(self):
        self.room = adventure_game('starting', 'south')
        self.assertEqual(self.room, '\nYou hit the wall\nYou are still in the starting zone\ngiant wooden door ahead, '
                                    'no sign of people')

        self.room = adventure_game('booby trap', 'east')
        self.assertEqual(self.room, '\nYou hit the wall\nYou are still in the booby trap room'
                                    '\nA dead lion hanging on a leg-hold trap')

        self.room = adventure_game('weapons', 'south')
        self.assertEqual(self.room, '\nYou hit the wall\nYou are still in the weapon room'
                                    '\nsub machine guns, m13s, and riffles hanged on the wall')

    def test_unspecified_location(self):
        self.room = adventure_game('jupiter', 'south')
        self.assertEqual(self.room, '\nyou are caged for damnation')

        self.room = adventure_game('Mukuru kwa Njenga', 'kusini')
        self.assertEqual(self.room, '\nyou are caged for damnation')

    def test_invalid_direction(self):
        self.room = adventure_game('starting', 'kaskazini-mashariki')
        self.assertEqual(self.room, '\nPlease proceed using the four cardinal points')
