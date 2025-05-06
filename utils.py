import math

def collision_detect(robot, obs):
    ox, oy = obs
    dx = robot.x - ox
    dy = robot.y - oy
    return 1 if dx**2 + dy**2 <= 20**2 else 0  # 20 是障礙半徑
