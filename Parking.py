from V2X import V2X


class Parking(V2X):
    def __init__(self, position, width, height, stay_time=10):
        V2X.__init__(self, position, name="Parking")
        self.mission_compelte = False
        self.time_left = stay_time

    def update():
        pass
