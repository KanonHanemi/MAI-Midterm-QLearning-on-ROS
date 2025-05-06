import numpy as np

class Robot:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t  # 朝向角度（度）

    def move_forward(self, step=1):
        # 依朝向移動
        theta = np.radians(self.t)
        self.x += step * np.sin(theta)
        self.y += step * np.cos(theta)
