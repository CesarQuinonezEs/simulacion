import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def julia_set(width, height, c_real, c_imag, max_iter):
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    
    x_vals = np.linspace(x_min, x_max, width)
    y_vals = np.linspace(y_min, y_max, height)
    
    image = np.zeros((width, height))
    
    for i in range(width):
        for j in range(height):
            z = x_vals[i] + y_vals[j]*1j
            c = complex(c_real, c_imag)
            iteration = 0
            while abs(z) <= 2 and iteration < max_iter:
                z = z**2 + c
                iteration += 1
            image[i, j] = iteration / max_iter
    
    return image

width = 800
height = 800
c_real = -0.7
c_imag = 0.27015
max_iter = 100

fig, ax = plt.subplots()
im = ax.imshow(np.zeros((width, height)).T, cmap='hot', extent=(-2, 2, -2, 2))

def update(frame):
    c_imag_new = c_imag + frame * 0.005  # Incrementamos la parte imaginaria gradualmente
    julia_image = julia_set(width, height, c_real, c_imag_new, max_iter)
    im.set_data(julia_image.T)
    ax.set_title(f"Fractal Julia para c = {c_real} + {c_imag_new:.4f}i")

ani = FuncAnimation(fig, update, frames=range(200), interval=50)

plt.colorbar(im)
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.show()
