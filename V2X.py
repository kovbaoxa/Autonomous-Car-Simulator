import numpy as np


class V2X:
    MAX_DISTANCE = 100

    def __init__(self, position, name="V2X"):
        self.name = name
        self.position = position

    def is_in_range(self, pos):
        x0, y0 = self.position
        x, y = pos
        distance = np.sqrt((x0 - x) ** 2 + (y0 - y) ** 2)

        if distance > V2X.MAX_DISTANCE:
            return False
        else:
            return True
