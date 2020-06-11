from room import Room
from player import Player

# Declare all the rooms

outside = Room("Outside Cave Entrance",
               "North of you, the cave mount beckons")
foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
# Link rooms together
outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

player = Player()
player.name = 'Anthony'
player.current_room = outside

while True:
    print(player.current_room)
    choice = input('Please enter a direction (N, E, W, S): ')
    if choice in {'n', 'e', 'w', 's'}:
        if hasattr(player.current_room, f'{choice}_to'):
            player.current_room = getattr(player.current_room, f'{choice}_to')
    elif choice in {'q'}:
        break
    else:
        print('Location out of bounds.')
    print('Type q to exit')

