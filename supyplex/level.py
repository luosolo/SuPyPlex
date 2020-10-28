from os import path


class LevelInfo(object):

    def __init__(self, title=None, infotrons=0, gravity=False, map=[]):
        self.title = title
        self.infotrons = infotrons
        self.gravity = gravity
        self.map = map

    def __repr__(self):
        return f"<LevelInfo {self.title} >"


class LevelLoader(object):
    """
    The Level Loader class is responsible to reads levels.dat
    This is a very simple, uncompressed format where each level is stored sequentially and takes up 1536 bytes each.
    The levels.dat distributed with the game is 170496 bytes in size (111 levels).
    ---------------------------------------------------------------------
    Offset    Length	    Contents	Details
    --------------------------------------------------------------------
    0	        1440	    Tile data	    60x24 in size, one byte per tile.
    1440	    4	        Unknown	        Unused
    1444	    1	        Gravity	        0 = off, 1 = on.
    1445	    1	        Unknown	        Used by the SpeedFix-version as a version indicator. In the original version it's always 0x20.
    1446	    23	        Title	        Always 23 characters, no null-termination, normally padded with spaces.
    1469	    1	        Freeze zonks    0 = off, 2 = on.
    1470	    1	        Infotrons       needed	The minimum number of infotrons needed to be able to clear the level. 0 = all of them.
    """
    def __init__(self, base_dir):
        self.levels = None
        self.path = base_dir

    def load_level(self, i):
        self.levels = open(str(path.join(self.path, "resources/LEVELS.DAT")), "rb")
        self.levels.read(i * 1536)
        data_bytes = self.levels.read(1536)
        current_map = []
        cnt = 0
        for x in range(24):
            tmp = []
            for y in range(60):
                tmp.append(data_bytes[cnt])
                cnt += 1
            current_map.append(tmp)
        self.levels.close()

        info = LevelInfo(map=current_map)
        info.gravity = data_bytes[1444]
        info.title = data_bytes[1446:1446 + 23]
        info.infotrons = data_bytes[1470]
        return info
