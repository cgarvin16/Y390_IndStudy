import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(1000)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

#Dots data
num_dots = 1000
dots = np.zeros(num_dots, dtype=[('position', float, 2),
                                 ('size',     float, 1),
                                 ('red_color', float, 4),
                                 ('green_color', float, 4),
                                 ('color',    float, 4)])

#Random position for new dots
dots['position'] = np.random.uniform(0, 1, (num_dots, 2))

# Construct the scatter which will update during animation
scatter = ax.scatter(dots['position'][:, 0], dots['position'][:, 1],
                     s=dots['size'], lw=5, edgecolors=dots['color'],
                     facecolors=dots['green_color'])


def update(frame_number):
    current_index = frame_number % num_dots

    #New dots position
    dots['position'][current_index] = np.random.uniform(0, 1, 2)
    dots['size'][current_index] = 5
    dots['color'][current_index] = (0, 0, 0, 1)
    dots['green_color'][current_index] = (0, 1, 0, 1)
    dots['red_color'][current_index] = (1, 0, 0, 1)

    #Update new dots
    scatter.set_edgecolors(dots['color'])
    scatter.set_sizes(dots['size'])
    scatter.set_facecolor(dots['green_color'])
    scatter.set_offsets(dots['position'])
    if(current_index == 1):
        scatter.set_facecolor(dots['green_color'])
    elif(current_index > 1):
        scatter.set_facecolor(dots['red_color'])


animation = FuncAnimation(fig, update, interval=750)
plt.show()