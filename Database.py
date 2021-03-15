class Database:
    def __init__(self, lidar, control, car):
        self.lidar = lidar
        self.control = control
        self.car = car
        self.stop = False
        self.run_time = 0.0
        self.run_dist = 0.0
        self.v2x_data = dict()
