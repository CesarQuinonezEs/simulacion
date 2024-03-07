import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk

# Función que describe el sistema de ecuaciones diferenciales del péndulo
def pendulum_equations(state, t, L, g, b):
    theta, omega = state
    dydt = [omega, -b*omega - (g/L)*np.sin(theta)]
    return dydt

# Función para resolver la ecuación diferencial y actualizar la animación
def update_pendulum(mass, length, theta_0, gravity):
    # Parámetros del péndulo
    m = mass       # Masa del péndulo
    L = length     # Longitud del péndulo
    g = gravity    # Aceleración debido a la gravedad
    b = 0.25      # Coeficiente de amortiguamiento
    
    # Condiciones iniciales
    theta0 = np.radians(theta_0)  # Ángulo inicial en radianes
    omega0 = 0.0          # Velocidad angular inicial
    state0 = [theta0, omega0]

    # Tiempo de integración
    t = np.linspace(0, 10, 1000)

    # Resolver la ecuación diferencial
    states = odeint(pendulum_equations, state0, t, args=(L, g, b))
    print(states)
    theta = states[:, 0]

    # Actualizar la animación
    def update(frame):
        plt.cla()  # Limpiar el plot anterior
        x = [0, L * np.sin(theta[frame])]
        y = [0, -L * np.cos(theta[frame])]
        plt.plot(x, y, marker='o')
        plt.xlim(-L, L)
        plt.ylim(-L, 0)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.xlabel('Posición en x')
        plt.ylabel('Posición en y')
        plt.title('Simulacion de un pendulo')

    # Crear la animación
    fig = plt.figure()
    ani = FuncAnimation(fig, update, frames=len(t), interval=50)
    plt.show()

# Función para manejar el evento del botón
def on_submit():
    mass = float(mass_entry.get())
    length = float(length_entry.get())
    theta_0 = float(theta_entry.get())
    gravity = float(gravity_entry.get())
    update_pendulum(mass, length, theta_0, gravity)

# Crear la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Simulación de un Péndulo")

# Crear etiquetas y campos de entrada para los parámetros del péndulo
mass_label = ttk.Label(root, text="Masa (kg): ")
mass_label.grid(row=0, column=0, padx=5, pady=5)
mass_entry = ttk.Entry(root)
mass_entry.grid(row=0, column=1, padx=5, pady=5)

length_label = ttk.Label(root, text="Longitud (m): ")
length_label.grid(row=1, column=0, padx=5, pady=5)
length_entry = ttk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)

theta_label = ttk.Label(root, text="Ángulo inicial (grados): ")
theta_label.grid(row=2, column=0, padx=5, pady=5)
theta_entry = ttk.Entry(root)
theta_entry.grid(row=2, column=1, padx=5, pady=5)

gravity_label = ttk.Label(root, text="Gravedad (m/s^2): ")
gravity_label.grid(row=3, column=0, padx=5, pady=5)
gravity_entry = ttk.Entry(root)
gravity_entry.grid(row=3, column=1, padx=5, pady=5)

submit_button = ttk.Button(root, text="Simular", command=on_submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
