from unittest import TestCase
from supyplex.level import *
from os import path

ROOT_DIR = path.dirname(path.abspath("."))


class TestLevelLoader(TestCase):
    def test_load_level(self):
        s = LevelLoader(ROOT_DIR)
        k = s.load_level(0)
        for i in range(24):
            for j in range(60):
                print(k.map[i][j])
