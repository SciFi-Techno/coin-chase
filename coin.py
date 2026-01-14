import pyray as pr

class Coin:
    def __init__(self):
        self.position = None

    def set_position(self, position):
        self.position = position

    def get_position_x(self):
        return self.position.x

    def get_position_z(self):
        return self.position.y