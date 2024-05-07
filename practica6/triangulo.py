import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski_triangle(ax, depth, p1, p2, p3):
    if depth == 0:
        ax.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'k')
    else:
        mid1 = midpoint(p1, p2)
        mid2 = midpoint(p2, p3)
        mid3 = midpoint(p3, p1)

        sierpinski_triangle(ax, depth-1, p1, mid1, mid3)
        sierpinski_triangle(ax, depth-1, mid1, p2, mid2)
        sierpinski_triangle(ax, depth-1, mid3, mid2, p3)

def update(frame):
    ax.clear()
    depth = frame % max_depth
    sierpinski_triangle(ax, depth, (0, 0), (1, 0), (0.5, np.sqrt(3)/2))

# Configuración inicial
max_depth = 16

fig, ax = plt.subplots()
ax.axis('equal')
ax.axis('off')

# Configuración de la animación
ani = FuncAnimation(fig, update, frames=range(2 * max_depth), interval=800)

plt.show()
