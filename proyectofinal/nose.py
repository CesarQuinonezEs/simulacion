import matplotlib.pyplot as plt

# Supongamos que tenemos dos listas de datos
# Estas son las listas de ejemplo. Reemplázalas con tus datos reales.
tiempo = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
serie1 = [10, 12, 15, 14, 13]
serie2 = [8, 9, 11, 10, 12]

# Convertir la lista de fechas en formato datetime
import pandas as pd
tiempo = pd.to_datetime(tiempo)

# Crear la gráfica
plt.figure(figsize=(10, 5))
plt.plot(tiempo, serie1, label='Serie 1', marker='o')
plt.plot(tiempo, serie2, label='Serie 2', marker='x')

# Añadir título y etiquetas a los ejes
plt.title('Gráfica de Serie de Tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Valores')

# Añadir una leyenda
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()