from utils import collision_detect
from laser import laser

def reward(robot, action, obs, goal):
    if collision_detect(robot, obs):
        return -100
    if goal.arrived_goal(robot.x, robot.y):
        return 100
    laser_length = laser(robot, obs)[action]
    goal_distance = ((robot.x-goal.x)**2 + (robot.x-goal.x)**2)**(1/2)
    return laser_length/10 + goal_distance/292*10