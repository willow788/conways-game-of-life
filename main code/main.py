import matplotlib
matplotlib.use("TkAgg")


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d

N= 100  
interval = 80

alive_prob= 0.25
max_age=  10

paused = False

grid = np.zeros((N, N), dtype=int)

def randomise():
    global grid
    grid = np.random.choice(
        [0, 1], size=(N, N), p=[1 - alive_prob, alive_prob]

    )

kernel = np.array([[1,1,1],
             [1,0,1],
             [1,1,1]])

def step():
    global grid
    neighbours = convolve2d(grid > 0, kernel, mode='same', boundary='wrap')
    
    birth = (grid == 0) & (neighbours == 3)
    # Survive if currently alive and has 2 or 3 neighbours
    survive = (grid > 0) & ((neighbours == 2) | (neighbours == 3))
    new_grid = np.zeros_like(grid)
    new_grid[survive] = np.minimum(grid[survive] + 1, max_age)
    new_grid[birth] = 1
    grid = new_grid

def on_click(event):
    if event.xdata is None or event.ydata is None:
        return
    i, j = int(event.ydata), int(event.xdata)
    grid[i, j] = 0 if grid[i, j] > 0 else 1

def on_key(event):
    global paused
    if event.key== ' ':
        paused = not paused

    elif event.key== 'r':
        randomise()
    elif event.key== 'c':
        grid[:] = 0
    elif event.key== 'g':
        add_glider(N//2, N//2)


def add_glider(x,y):
    glider = [(0,1), (1,2), (2,0), (2,1),(2,2)]
    for dx, dy in glider:
        grid[(x+dx)%N , (y+dy)%N] = 1


fig, ax = plt.subplots(figsize=(12, 12))
mat = ax.imshow(
    grid,
    cmap='inferno',  # higher contrast
    vmin=0,
    vmax=max_age,
    interpolation='nearest',
    animated=True,
)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("conway's game of life")
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('key_press_event', on_key)

def update(frame):
    if not paused:
        step()
    mat.set_data(grid)
    return [mat]


if __name__ == "__main__":
    # Seed with a random grid for visible output
    randomise()
    ani = FuncAnimation(fig, update, interval=interval, blit=True)
    plt.show(block=True)

