from supyplex.game import SuPyplex
from os import path

ROOT_DIR = path.dirname(path.abspath("main.py"))

if __name__ == '__main__':
    game = SuPyplex(ROOT_DIR)
    game.setup()
    game.main_loop()
