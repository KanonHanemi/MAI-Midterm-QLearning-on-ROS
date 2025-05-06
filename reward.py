from utils import collision_detect

def reward(robot, obs, goal):
    if collision_detect(robot, obs):
    
    return