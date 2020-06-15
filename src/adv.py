from room import Room
from player import *
from item import Item

# items
torch = Item('Torch', 'Weathered oak branch with cloth wrapped around it.')
athame = Item('Athame', 'Ornate silver ceremonial dagger.')
finger = Item('Finger', 'Crudely severed finger, there is a wedding band on it.')
phylactery = Item('Phylactery', 'Small vial of blood... Creepy.')
tome = Item('Tome', 'Very heavy book written in an alien language in what looks like blood.')
letter = Item('Letter',
              """A letter written by you... to you.
              You can barely understand what it says in the flickering light of your torch.
              You look at the hand holding the letter and realize you're missing your ring finger.
              The last words in the letter say...
              DON'T LOOK BACK""")

# Declare all the rooms

cliffs = Room("Great dark cliffs", """Bordering the brackish, roaring waters. """
                                   """You wake up on a freezing, jagged bed of rock...
The cliffs seem to be made of a black oily stone.
How did you get here? What happened before this?
Up ahead is is a small, strange shrine that seems to make the area around it get darker""", [torch])
shrine = Room("The shrine",
              """Carved in the black oily stone, """ """is a strange arcane idol sitting among countless lit candles""",
              [tome])
stairs = Room("Stairs", """A seemingly endless flight of steps lies before you, with each step a powerful 
miasma takes hold of you. Your vision begins tunneling. There is a glimmer of a bloodied, silvery blade""", [athame])
eyrie = Room("Eyrie", """Finally reaching the top of the stairs, your vision is not just tunneling,
but you're seeing trails and can scarcely breathe.
High among the clouds is the eyrie overlooking the black abyss you came from.
You swear, for a moment you saw hooded figures praying to the ocean...
but it must've been your eyes playing tricks on you.
The winds are punishing, and the saltwater is chafing your face""", [phylactery, finger])
altar = Room("The cursed altar", """You've found a twisted altar. It looks almost made of blackish tentacles.
The altar... is moving. Or is it? Have you descended into madness?
At it's center, is a a small envelope... It's addressed to you.
As you walk up closer, you hear a faint whisper in a language you've never heard.
It gets louder, and louder... but you still don't understand.
""", [letter])
# Link rooms together
cliffs.n_to = shrine
shrine.s_to = cliffs
shrine.n_to = stairs
shrine.e_to = eyrie
stairs.s_to = shrine
eyrie.w_to = shrine
eyrie.n_to = altar
altar.s_to = eyrie

player = Player()
player.name = 'Asuka'
player.current_room = cliffs
item = player.items


def del_cr_item():
    for i in player.current_room.items:
        player.current_room.items.remove(i)
        return i


# def del_inv_item():
#     for i in player.items:



while True:

    print(player.current_room)
    print(f'Item(s) in this area: ', len(player.current_room.items))
    choice = input('Please enter a cardinal direction to move (N, E, W, S), (I) for inventory, or (A) for action: ')
    if choice in {'n', 'e', 'w', 's'}:
        if hasattr(player.current_room, f'{choice}_to'):
            player.current_room = getattr(player.current_room, f'{choice}_to')
    elif choice in {'a'}:
        action_choice = input('Enter (E) to examine items in the area, (GET) to pick up items, (I) for inventory: ')
        if action_choice in {'e'}:
            print(repr(player.current_room.items))
            action_choice2 = input('Enter (M) to return to previous screen')
            print(action_choice2)
            if action_choice2 in {'m'}:
                pass
        elif 'get ' in action_choice:
            item_unit = action_choice.replace('get ', '')
            pickup = input(f'Get: {item_unit}? (Y or N)')
            print(pickup)
            if pickup in {'y'}:
                item.insert(0, player.current_room.items[0])
                del_cr_item()
                print(f'{player.name} picked up the {item_unit}')
    elif choice in {'i'}:
        print('In your inventory: ')
        for i in item:
            print(f'{str(i)}')
        inv_choice = input('Enter (E) to examine inventory item, or (DROP) to drop items.')
        print(inv_choice)
        if inv_choice in {'e'}:
            print(str(player.items))
            inv_choice2 = input('Return to previous menu by entering (M)')
            print(inv_choice2)
            if inv_choice2 in {'m'}:
                pass
        elif 'drop ' in inv_choice:
            drop_unit = inv_choice.replace('drop ', '')
            drop = input(f'Drop {drop_unit}? (Y or N)')
            if drop in {'y'}:
                item.remove(item[0])
                player.current_room.items.insert(0, item)
                # print(f'{str(item[0]).strip("[]")} was dropped.')
    elif choice in {'q'}:
        break
    else:
        print('Location out of bounds.')
    print('Type q to exit')
