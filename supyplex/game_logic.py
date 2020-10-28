from supyplex.level import LevelLoader
from supyplex.commons import *

ZONK = 1
INFOTRON = 4
MURPHY = 3
EMPTY = 0

slicks = [ZONK, INFOTRON, 5, 26, 27, 38, 39]


class GameLogic(object):
    """
    This is the controller of the game.
    here is implemented a sort of physics of the game
    """

    def __init__(self, level, base_dir):
        # The map is a matrix 24x60
        self.levelInfo = LevelLoader(base_dir).load_level(level)
        self.map = self.levelInfo.map

    def can_move(self, p: Point):
        """
        this function tells if the player murphy can move to the position in the map
        :param p: The point where the player want to move
        :return:
        """
        val = self.map[p.y][p.x]
        return val in {0, 2, 4}

    def move_complete(self, from_position: Point, to_position: Point):
        """
        this function is called every time the player completes its movement
        :param from_position: start position
        :param to_position:  end position
        :return:
        """
        # TODO i need to check if there is an elegant way to implement such behaviour
        self.map[from_position.y][from_position.x] = EMPTY
        self.map[to_position.y][to_position.x] = MURPHY

    def calculate_g_item_movement(self, y, x, tp):
        if self.map[y][x] == tp:
            if self.map[y + 1][x] == EMPTY:
                self.map[y][x] = EMPTY
                self.map[y + 1][x] = tp
            elif self.map[y + 1][x] in slicks:
                if self.map[y][x + 1] == EMPTY and self.map[y + 1][x + 1] == EMPTY:
                    self.map[y][x] = EMPTY
                    self.map[y][x + 1] = tp
                elif self.map[y][x - 1] == EMPTY and self.map[y + 1][x - 1] == EMPTY:
                    self.map[y][x] = EMPTY
                    self.map[y][x - 1] = tp

    def calculate_next_move(self):
        for y in range(24):
            for x in range(60):
                self.calculate_g_item_movement(y, x, ZONK)
                self.calculate_g_item_movement(y, x, INFOTRON)
        pass
