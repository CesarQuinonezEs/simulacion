def von(semilla, digitos=4, iteraciones=10):
    numeros = []
    for i in range(iteraciones):

        cuadrado = semilla ** 2
        
        
        cuadrado_str = str(cuadrado).zfill(2 * digitos)
        

        centro = len(cuadrado_str) // 2
        nuevo = int(cuadrado_str[centro - digitos : centro + digitos])

        semilla = nuevo
        
        numeros.append(nuevo)
        
    return numeros

# Ejemplo de uso
semilla = int(input("Ingrese la semilla (numero de 4 digitos) \n"))
n = int(input("ingrese la cantidad de numeros a generar \n"))
numeros = von(semilla, digitos=4, iteraciones=n)
print("Números generados:", numeros)
