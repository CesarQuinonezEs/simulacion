import random
import matplotlib.pyplot as plt
from os import system
def dados():
    flag = True;
    while(flag):
        n = int(input("Ingrese el numero de tiradas: "))
        listD = []
        for i in range(n):
            listD.insert(i,random.randint(1,6))

        unos = listD.count(1)
        dos = listD.count(2)
        tres = listD.count(3)
        cuatro = listD.count(4)
        cinco = listD.count(5)
        seis = listD.count(6)
        print("probabilidad de que salga 1: ", unos/n)
        print("probabilidad de que salga 2: ", dos/n)
        print("probabilidad de que salga 3: ", tres/n)
        print("probabilidad de que salga 4: ", cuatro/n)
        print("probabilidad de que salga 5: ", cinco/n)
        print("probabilidad de que salga 6: ", seis/n)
        fig,ax = plt.subplots()
        ax.hist(listD)
        plt.show()
        p = input("quieres continuar ?: ")
        if p == "no":
            flag = False
        system("cls")
