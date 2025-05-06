import matplotlib.pyplot as plt
import matplotlib.animation as animation
from robot import Robot
from utils import collision_detect
import numpy as np

# 這裡用內建的雷射函數來畫出五條線
def plot_laser(robot, ax):
    laser_angles = [-30, -15, 0, 15, 30]
    max_range = 100
    obstacle_center = (150, 150)
    obstacle_radius = 20

    for angle in laser_angles:
        theta = np.radians(robot.t + angle)
        x0, y0 = robot.x, robot.y

        for r in range(1, max_range + 1):
            x = x0 + r * np.sin(theta)
            y = y0 + r * np.cos(theta)
            if x < 0 or x > 300 or y < 0 or y > 300 or ((x - 150)**2 + (y - 150)**2 <= obstacle_radius**2):
                ax.plot([x0, x], [y0, y], color='blue')
                break
        else:
            x = x0 + max_range * np.sin(theta)
            y = y0 + max_range * np.cos(theta)
            ax.plot([x0, x], [y0, y], color='blue')

# 畫整張地圖
def draw_map(robot, ax):
    ax.clear()
    ax.set_xlim(0, 300)
    ax.set_ylim(0, 300)
    ax.set_aspect('equal')

    # 障礙物與終點
    ax.add_patch(plt.Circle((150, 150), 20, color='black'))
    ax.plot(150, 250, 'rx', markersize=10, markeredgewidth=2)

    # 畫機器人
    ax.add_patch(plt.Circle((robot.x, robot.y), 5, color='blue'))

    # 畫雷射
    plot_laser(robot, ax)

    # 網格與標題
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.set_xticks(range(0, 301, 50))
    ax.set_yticks(range(0, 301, 50))
    ax.set_title("Robot Animation")

# 主動畫流程
def run_simulation():
    robot = Robot(150, 50, 0)
    obs = (150, 150)

    fig, ax = plt.subplots(figsize=(6, 6))

    def update(frame):
        if not collision_detect(robot, obs):
            robot.move_forward(step=2)  # 每次移動2單位
        draw_map(robot, ax)

    ani = animation.FuncAnimation(fig, update, frames=200, interval=50, repeat=False)
    plt.show()

if __name__ == "__main__":
    run_simulation()
