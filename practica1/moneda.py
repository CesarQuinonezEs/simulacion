import random
import matplotlib.pyplot as plt
from os import system
def moneda():
    val = []
    aguila = 0
    sello = 0
    flag = True
    while(flag):
        n = int(input("Ingrese el numero de tiros "))
        for i in range(n):
            moneda = random.randint(0, 1)
   
            if moneda == 0:
                val.insert(i,"aguila")
                aguila = aguila + 1
            else:
                val.insert(i,"sello")
                sello = sello + 1
   
            if i > 0:
                auxA = aguila/n
                auxB = sello/n
        print("probabilidad de aguila",auxA)
        print("probabilidad de sello",auxB)
        fig, ax = plt.subplots()
        plt.title("Experimento: numero de tiros " + str(n))
        plt.suptitle("Tirar dos monedas")
        plt.hist(val)
        plt.show()
        p = input("quieres continuar ?: ")
        if p == "no":
            flag = False
        system("cls")