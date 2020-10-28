from LevelLoader import LevelLoader
from commons import Point


class GameLogic(object):

    def __init__(self, level):
        self.levelInfo = LevelLoader().load_level(level)
        self.map = self.levelInfo.map

    def can_move(self, p: Point):
        val = self.map[p.y][p.x]
        return val in {0, 2, 4}

    def move_complete(self, from_position: Point, to_position: Point):
        print(f"move complete -> from:{from_position}, end: {to_position}")
        self.map[from_position.y][from_position.x] = 0
        self.map[to_position.y][to_position.x] = 3

    def calculate_next_move(self):
        pass
