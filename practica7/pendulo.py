import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros físicos
g = 9.81  # Aceleración gravitatoria (m/s^2)
omega = 2*np.pi / (24*3600)  # Velocidad angular de la Tierra (rad/s)

# Condiciones iniciales
theta_0 = np.pi / 4  # Ángulo inicial (en radianes)
theta_dot_0 = 0      # Velocidad angular inicial (en rad/s)

# Función para actualizar la animación en cada fotograma
def update(frame):
    global theta, theta_dot
    theta_dot_dot = - (g / 1) * np.sin(theta)  # Ecuación de movimiento
    theta_dot += theta_dot_dot * dt
    theta += theta_dot * dt + 0.5 * theta_dot_dot * dt**2
    line.set_data([0, np.sin(theta)], [0, -np.cos(theta)])
    return line,

# Inicialización de la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
line, = ax.plot([], [], lw=2)

# Configuración de la animación
dt = 1  # Paso de tiempo (en segundos)
theta = theta_0
theta_dot = theta_dot_0
ani = FuncAnimation(fig, update, frames=np.arange(0, 24*3600, dt), blit=True)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Animación del Péndulo de Foucault')

plt.show()
