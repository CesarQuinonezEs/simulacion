import random
import matplotlib.pyplot as plt
from os import system

def dosDados():
    flag = True;
    while(flag):
        n = int(input("Ingrese el numero de tiradas: "))
        listD = []
        for i in range(n):
            listD.insert(i,(random.randint(1,6) + random.randint(1,6)) )

        a2 = listD.count(2)
        a3 = listD.count(3)
        a4 = listD.count(4)
        a5 = listD.count(5)
        a6 = listD.count(6)
        a7 = listD.count(7)
        a8 = listD.count(8)
        a9 = listD.count(9)
        a10 = listD.count(10)
        a11 = listD.count(11)
        a12 = listD.count(12)

        print("probabilidad de que salga 2: ", a2/n)
        print("probabilidad de que salga 3: ", a3/n)
        print("probabilidad de que salga 4: ", a4/n)
        print("probabilidad de que salga 5: ", a5/n)
        print("probabilidad de que salga 6: ", a6/n)
        print("probabilidad de que salga 7: ", a7/n)
        print("probabilidad de que salga 8: ", a8/n)
        print("probabilidad de que salga 9: ", a9/n)
        print("probabilidad de que salga 10: ", a10/n)
        print("probabilidad de que salga 11: ", a11/n)
        print("probabilidad de que salga 12: ", a12/n)
        fig,ax = plt.subplots()
        ax.hist(listD)
        plt.show()
        p = input("quieres continuar ?: ")
        if p == "no":
            flag = False
        system("cls")
