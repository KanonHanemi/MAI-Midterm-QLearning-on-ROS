import numpy as np

class Robot:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t  # 朝向角度（度）

    def move_forward(self, step=1):
        # 依朝向移動
        theta = np.radians(self.angle())
        self.x += step * np.sin(theta)
        self.y += step * np.cos(theta)
    
    def angle(self):
        if self.t >= 180:
            self.t = self.t - 360
        elif self.y <= -181:
            self.t = self.t + 360
        return self.t

class Obstacle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    
    def is_hit(self, px, py):
        return (px - self.x)**2 + (py - self.y)**2 <= self.r**2    