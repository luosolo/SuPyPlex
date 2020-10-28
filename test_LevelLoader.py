from unittest import TestCase
from LevelLoader import *


class TestLevelLoader(TestCase):
    def test_load_level(self):
        s = LevelLoader()
        for i in range(40):
            k = s.load_level(0)
            assert k.title is not None
