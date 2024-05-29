import matplotlib.pyplot as plt
import numpy as np

# Parámetros del generador congruencial mixto
a = 1664525
c = 1013904223
m = 2**32
X0 = 42

# Generador congruencial mixto
def lcg(a, c, m, seed, n):
    numbers = []
    Xn = seed
    for _ in range(n):
        Xn = (a * Xn + c) % m
        numbers.append(Xn)
    return numbers

# Generar n números aleatorios
n = 6000
random_numbers = lcg(a, c, m, X0, n)
random_numbers2 = lcg(a, c+1, m, X0, n)
# Transformar números aleatorios al rango [1, 6]
dice_1 = [(num % 6) + 1 for num in random_numbers]
dice_2 = [(num % 6) + 1 for num in random_numbers2]

for i in range(10):
    print(dice_1[i],"-",dice_2[i])
# Sumar los resultados de los dos dados
dice_sum = [d1 + d2 for d1, d2 in zip(dice_1, dice_2)]

# Calcular la media y la varianza
mean = np.mean(dice_sum)
variance = np.var(dice_sum)

# Mostrar los primeros 10 lanzamientos de dados
print(f"\nMedia de la suma de los lanzamientos: {mean}")
print(f"Varianza de la suma de los lanzamientos: {variance}")

# Graficar la distribución de la suma de los dos dados
plt.hist(dice_sum, bins=range(2, 14), edgecolor='black', align='left')
plt.xlabel('Suma de los dos dados')
plt.ylabel('Frecuencia')
plt.title('Simulación de lanzamiento de dos dados')
plt.xticks(range(2, 13))
plt.show()
plt.hist(dice_1,bins=range(1, 8), edgecolor='black', align='left')

plt.xlabel('Numero de los dados')
plt.ylabel('Frecuencia')
plt.title('Lanzamiento del dado 1')

plt.show()

plt.hist(dice_2,bins=range(1, 8), edgecolor='black', align='left')

plt.xlabel('Numero de los dados')
plt.ylabel('Frecuencia')
plt.title('Lanzamiento del dado 2')

plt.show()