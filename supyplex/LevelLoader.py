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
