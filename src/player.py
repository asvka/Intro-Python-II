class Player:
    def __init__(self, name=None, current_room=None):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name}, location: {self.current_room}.'
