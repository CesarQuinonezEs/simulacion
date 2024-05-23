import numpy as np


distribucion_dias = {
    "Domingo": 0,
    "Lunes": 0.35,
    "Martes": 0.05,
    "Miércoles": 0.10,
    "Jueves": 0.15,
    "Viernes": 0.25,
    "Sábado": 0.10
}

clientes_semanales = np.random.randint(350, 781)

tiempos_atencion = np.random.randint(5, 31, size=clientes_semanales)
print("clientes de esta semana: ",clientes_semanales)

horario_diario = 480


modulos_por_dia = {}


def calcular_modulos(clientes_dia, tiempos_atencion, horario_diario):
    total_tiempo = np.sum(tiempos_atencion[:clientes_dia])
    print(total_tiempo)
    modulos_necesarios = np.ceil(total_tiempo / horario_diario).astype(int)
    return modulos_necesarios

for dia, porcentaje in distribucion_dias.items():
    if porcentaje == 0:
        modulos_por_dia[dia] = 0
    else:
        clientes_dia = int(clientes_semanales * porcentaje)
        tiempos_atencion_dia = tiempos_atencion[:clientes_dia]
        tiempos_atencion = tiempos_atencion[clientes_dia:]
        modulos_por_dia[dia] = calcular_modulos(clientes_dia, tiempos_atencion_dia, horario_diario)

# Resultados
for dia, modulos in modulos_por_dia.items():
    print(f"{dia}: {modulos} módulos")

