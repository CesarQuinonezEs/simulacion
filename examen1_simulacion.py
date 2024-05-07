import random
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
def getWiner(p1,p2):
    if p1 == 0:
      if p2 == 1:
        return "jugador 2"
      elif p2 == 2:
        return "jugador 1"
      else:
        return "empate"
    elif p1 == 1:
      if p2 == 1:
        return "empate"
      elif p2 == 2:
        return "jugador 2"
      else:
        return "jugador 1"
    else:
      if p2 == 1:
        return "jugador 1"
      elif p2 == 2:
        return "empate"
      else:
        return "jugador 2"

def getOpc(opc):
  if opc == 0:
    return "piedra"
  elif opc == 1:
    return "papel"
  else:
    return "tijeras"

nJuegos = 500
resultados = []
jugador1His =[]
jugador2His = []

for i in range(nJuegos):
  p1 = random.randint(0,2)
  p2 = random.randint(0,2)
  jugador1His.insert(i,getOpc(p1))
  jugador2His.insert(i,getOpc(p2))
  res = getWiner(p1,p2)
  resultados.insert(i,res)
frecJugador1 = resultados.count("jugador 1")
frecJugador2 = resultados.count("jugador 2")
frecEmp = resultados.count("empate")
print("Frecuencia en la que gana el jugador 1: ",frecJugador1,'\n')
print("Frecuencia en la que gana el jugador 2: ",frecJugador2,'\n')
print("Frecuencia en la que hay empate: ",frecEmp,'\n')
mediaRes = (frecEmp + frecJugador1 + frecJugador2)/3
print("Media en los resultados de cada juego: ", mediaRes,'\n')
varRes = (((frecEmp-mediaRes)**2) + ((frecEmp-mediaRes)**2) + ((frecEmp-mediaRes)**2))/3
print("La varianza de los resultados es: ", varRes, '\n')
desEstandar = np.sqrt(varRes)
print("La desviacion estandar de los resultados es: ", desEstandar,'\n')
#Para el jugador 1 -----------------------------------------------------------------------------
print("Para el jugador 1 -----------------------------------------------------------------------------\n")
frecPi = jugador1His.count("piedra")
frecPap = jugador1His.count("papel")
frecT = jugador1His.count("tijeras")
print("Frecuencia en la que el jugador 1 tiene piedra: ",frecPi,'\n')
print("Frecuencia en la que el jugador 1 tiene papel: ",frecPap,'\n')
print("Frecuencia en la que el jugador 1 tiene tijeras:",frecT,'\n')
mediaRes = (frecPi + frecPap + frecT)/3
print("Media en las opciones jugadas por el jugador 1: ", mediaRes,'\n')
varRes = (((frecPi-mediaRes)**2) + ((frecPap-mediaRes)**2) + ((frecT-mediaRes)**2))/3
print("La varianza de las opciones jugadas por el jugador 1: ", varRes, '\n')
desEstandar = np.sqrt(varRes)
print("La desviacion estandar de las opciones jugadas por el jugador 1: ", desEstandar,'\n')

print("Para el jugador 2 -----------------------------------------------------------------------------\n")
frecPi = jugador2His.count("piedra")
frecPap = jugador2His.count("papel")
frecT = jugador2His.count("tijeras")
print("Frecuencia en la que el jugador 2 tiene piedra: ",frecPi,'\n')
print("Frecuencia en la que el jugador 2 tiene papel: ",frecPap,'\n')
print("Frecuencia en la que el jugador 2 tiene tijeras:",frecT,'\n')
mediaRes = (frecPi + frecPap + frecT)/3
print("Media en las opciones jugadas por el jugador 2: ", mediaRes,'\n')
varRes = (((frecPi-mediaRes)**2) + ((frecPap-mediaRes)**2) + ((frecT-mediaRes)**2))/3
print("La varianza de las opciones jugadas por el jugador 2: ", varRes, '\n')
desEstandar = np.sqrt(varRes)
print("La desviacion estandar de las opciones jugadas por el jugador 2: ", desEstandar,'\n')

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].hist(jugador1His, bins=3, color='skyblue', edgecolor='black')
axs[0].set_title('Opciones del jugador 1')
axs[0].set_xlabel('Opcion')
axs[0].set_ylabel('Frecuencia')
axs[0].grid(True)

# Histograma 2
axs[1].hist(jugador2His, bins=3, color='salmon', edgecolor='black')
axs[1].set_title('Opciones del jugador 2')
axs[1].set_xlabel('Opcion')
axs[1].set_ylabel('Frecuencia')
axs[1].grid(True)

# Histograma 3
axs[2].hist(resultados, bins=3, color='lightgreen', edgecolor='black')
axs[2].set_title('Resultados del juego')
axs[2].set_xlabel('Ganador o Resultado')
axs[2].set_ylabel('Frecuencia')
axs[2].grid(True)

# Ajustar espaciado entre subgráficos
plt.tight_layout()

# Mostrar el histograma
plt.show()