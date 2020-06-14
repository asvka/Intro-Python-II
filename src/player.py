
class Player:
    def __init__(self, name=None, current_room=None, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = list(items)

    def __str__(self):
        return f'{self.name}, location: {self.current_room}.'

    # def take_item(self, item):
    #     self.items.insert(item)
    #     for i in item:
    #         if self.items == Player.current_room.items:
    #
    #     print('Item was picked up!')

    # def drop_item(self, string):
    #     for i in self.items:
    #         self.items.remove(i)
    #         return i
    #     print('Item was dropped!')
