import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(1000)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

#Dots data
num_dots = 1000
dots = np.zeros(num_dots, dtype=[('position', float, 2),
                                 ('size',     float, 1),
                                 ('red_color', float, 4),
                                 ('green_color', float, 4),
                                 ('blank_color', float, 4),
                                 ('edge',    float, 4)])

#Random position for new dots
dots['position'] = np.random.uniform(0, 1, (num_dots, 2))

# Construct the scatter which will update during animation
scatter = ax.scatter(dots['position'][:, 0], dots['position'][:, 1],
                     s=dots['size'], lw=5, edgecolors=dots['edge'],
                     facecolors=dots['green_color'])


def update(frame_number):
    current_index = frame_number
    blank_dot = current_index - 2

    # New dots position
    dots['position'][current_index] = np.random.uniform(0, 1, 2)
    dots['size'][current_index] = 5
    dots['edge'][current_index] = (0, 0, 0, 1)
    dots['green_color'][current_index] = (0, 1, 0, 1)  # will always be the current index
    #dots['red_color'][red_dot] = (1, 0, 0, 1)  # current - 1
   # dots['blank_color'][blank_dot] = (0, 0, 0, 0)  # current - 2


    #Update new dots
    scatter.set_edgecolors(dots['edge'])
    scatter.set_sizes(dots['size'])
    scatter.set_offsets(dots['position'])
    scatter.set_facecolor(dots['green_color'])

    if(current_index > 0):
        red_dot = current_index - 1
        dots['red_color'][red_dot] = (1, 0, 0, 1)  # current - 1
        scatter.set_facecolor(dots['red_color'])

        dots['green_color'][current_index] = (0, 1, 0, 1)
        scatter.set_facecolor(dots['green_color'])


animation = FuncAnimation(fig, update, interval=1000)
plt.show()