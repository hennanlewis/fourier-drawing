import numpy as np


class Trace:
    def __init__(self, max_points):
        self.max_points = max_points

        self.x = []
        self.y = []

    def add(self, point):
        self.x.append(point[0])
        self.y.append(point[1])

        if len(self.x) > self.max_points:
            self.x.pop(0)
            self.y.pop(0)

    def get_line_data(self):
        return self.x, self.y

    def get_fill_data(self):
        return np.column_stack((
            self.x,
            self.y
        ))
