from unittest import TestCase
from supyplex.LevelLoader import *
from os import path

ROOT_DIR = path.dirname(path.abspath("."))


class TestLevelLoader(TestCase):
    def test_load_level(self):
        s = LevelLoader(ROOT_DIR)
        for i in range(40):
            k = s.load_level(0)
            assert k.title is not None
