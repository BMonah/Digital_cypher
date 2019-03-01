def adventure_game(current_location, movement):

    # initialization of variables is done here
    rooms = {'starting': {'name': 'starting zone', 'north': 'booby trap', 'description':
                          'giant wooden door ahead, no sign of people'},
             'booby trap': {'name': 'booby trap room', 'south': 'starting', 'west':
                            'weapons', 'description': 'A dead lion hanging on a leg-hold trap'},
             'weapons': {'name': 'weapon room', 'east': 'booby trap', 'description':
                         'sub machine guns, m13s, and riffles hanged on the wall'}}
    directions = ['north', 'south', 'east', 'west']

    # conditional if-else statements giving the game output according to command
    if current_location in rooms:
        current_room = rooms[current_location]
        if movement in directions:
            if movement in current_room:
                current_location = rooms[current_room[movement]]
                return 'you are in the {} \n{}'.format(current_location['name'],
                                                       current_location['description'])
            else:
                return '\nYou hit the wall\nYou are still in the {}\n{}'.format(current_room['name'],
                                                                                current_room['description'])
        else:
            return '\nPlease proceed using the four cardinal points'
    else:
        return'\nyou are caged for damnation'
