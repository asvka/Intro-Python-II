from room import Room
from player import *
from item import Item

# items
torch = Item('Torch', 'Weathered oak branch with cloth wrapped around it.')
athame = Item('Athame', 'Ornate silver ceremonial dagger.')
finger = Item('Finger', 'Crudely severed finger, there is a wedding band on it.')
phylactery = Item('Phylactery', 'Small vial of blood... Creepy.')
tome = Item('Black Tome', 'Very heavy book written in an alien language in what looks like blood.')
letter = Item('Letter',
              """A letter written by you... to you.
              You can barely understand what it says in the flickering light of your torch.
              You look at the hand holding the letter and realize you're missing your ring finger.
              The last words in the letter say...
              DON'T LOOK BACK""")

# Declare all the rooms

outside = Room("""Great dark cliffs bordering the brackish, roaring waters. """
               """The cliffs seem to be made of a black oily stone""",
               """Up ahead is is a small, strange shrine that seems to make the area around it get darker""", [torch])
foyer = Room("The shrine", """Dim light filters in from the south. Dusty
passages run north and east.""", [tome])
overlook = Room("A view into the abyss", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [athame])
narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [phylactery, finger])
treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [letter])
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
item = player.items


def del_cr_item():
    for i in player.current_room.items:
        player.current_room.items.remove(i)
        return i


while True:

    print(player.current_room)
    print(f'Item(s) in this area: ', len(player.current_room.items))
    choice = input('Please enter a cardinal direction to move (N, E, W, S), (I) for inventory, or (A) for action: ')
    if choice in {'n', 'e', 'w', 's'}:
        if hasattr(player.current_room, f'{choice}_to'):
            player.current_room = getattr(player.current_room, f'{choice}_to')
    elif choice in {'a'}:
        action_choice = input('Enter (E) to examine items, (GET) to pick up items, (I) for inventory: ')
        if action_choice in {'e'}:
            print(repr(player.current_room.items))
        elif action_choice in {'get '}:
            pickup = input(f'Get: {str(player.current_room.items[0])}? (Y or N)')

            print(pickup)
            if pickup in {'y'}:
                item.insert(0, player.current_room.items[0])
                del_cr_item()
                print(f'{player.name} picked up the {item[0]}')
    elif choice in {'i'}:
        print('In your inventory: ')
        for i in item:
            print(f'{str(i)}')
        inv_choice = input('Enter (E) to examine inventory item, or (DROP) to drop items.')
        print(inv_choice)
        if inv_choice in {'e'}:
            print(str(player.items))
        elif inv_choice in {'drop'}:
            drop = input('Drop items? (Y or N)')
            if drop in {'y'}:
                player.current_room.items.insert(0, item)
                print(f'{str(item[0]).strip("[]")} was dropped.')
    elif choice in {'q'}:
        break
    else:
        print('Location out of bounds.')
    print('Type q to exit')
