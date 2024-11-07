import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def ballistic_trajectory(h, v0, theta):
    theta_rad = np.radians(theta)

    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)

    g = 9.81

    t_flight = (v0y + np.sqrt(v0y**2 + 2 * g * h)) / g

    t = np.linspace(0, t_flight, 500)

    x = v0x * t
    y = h + v0y * t - 0.5 * g * t**2

    return t, x, y

def create_animation(t, x, y, filename, color):
    fig, ax = plt.subplots()
    ax.set_xlim(0, max(x))
    ax.set_ylim(0, max(y))
    ax.set_xlabel('x (м)')
    ax.set_ylabel('y (м)')
    ax.set_title('Траектория движения тела')

    line, = ax.plot([], [], 'o-', lw=2, color=color)

    def init():
        line.set_data([], [])
        return line,

    def update(i):
        line.set_data(x[:i], y[:i])
        return line,

    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=20)

    ani.save(filename, writer='pillow')

def plot_speed_time(t, v0, theta, filename, color):
    theta_rad = np.radians(theta)
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)
    g = 9.81

    vx = v0x * np.ones_like(t)

    vy = v0y - g * t

    v = np.sqrt(vx**2 + vy**2)

    plt.figure()
    plt.plot(t, v, label='Скорость', color=color)
    plt.xlabel('Время (с)')
    plt.ylabel('Скорость (м/с)')
    plt.title('Зависимость скорости от времени')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def plot_coordinate_time(t, x, filename, color):
    plt.figure()
    plt.plot(t, x, label='Координата x', color=color)
    plt.xlabel('Время (с)')
    plt.ylabel('Координата x (м)')
    plt.title('Зависимость координаты x от времени')
    plt.legend()
    plt.savefig(filename)
    plt.close()

def main():

    h = float(input("Введите высоту, с которой брошено тело в метрах: "))
    v0 = float(input("Введите начальную скорость в м/c: "))
    theta = float(input("Введите угол, под которым брошено тело в градусах: "))

    color = '#ff73f1'

    t, x, y = ballistic_trajectory(h, v0, theta)

    create_animation(t, x, y, 'ballistic_trajectory.gif', color)

    plot_speed_time(t, v0, theta, 'speed_time.png', color)

    plot_coordinate_time(t, x, 'coordinate_time.png', color)

if __name__ == "__main__":
    main()
