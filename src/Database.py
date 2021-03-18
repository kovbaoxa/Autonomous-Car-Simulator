class Database:
    def __init__(self, lidar, control, car):
        self.lidar = lidar
        self.control = control
        self.car = car
        self.stop = False
        self.timestamp = 0
        self.run_time = 0.0
        self.run_dist = 0.0
        self.checkpoint_time = dict()
