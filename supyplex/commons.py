
MAX_X = 60 * 32
MAX_Y = 24 * 32
CELL_SIZE = 32
FPS = 60


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"<Point {self.x}, {self.y}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def tuple(self):
        return self.x, self.y

    def map_tuple(self):
        return Point(self.x // 32, self.y // 32)

    def from_map_tuple(self, t):
        self.x = t[1] // 32
        self.y = t[0] // 32


POINT_UP = Point(0, -32)
POINT_DOWN = Point(0, 32)
POINT_LEFT = Point(-32, 0)
POINT_RIGHT = Point(32, 0)
