import simRuleta
import matplotlib.pyplot as plt

flag = True
listR = []

while(flag):
    n = int(input("Cuantas veces quiere girar la ruleta: \n"))
    for i in range(n):
        aux = simRuleta.ruleta()
        listR.insert(i,aux)
    a0 = listR.count(0)
    a1 = listR.count(1)
    a2 = listR.count(2)
    a3 = listR.count(3)
    print("probabilidad de 0: ", a0/n)
    print("probabilidad de 1: ", a1/n)
    print("probabilidad de 2: ", a2/n)
    print("probabilidad de 3: ", a3/n)
    listPie = [a0,a1,a2,a3]
    nom = ["0","1","2","3"]
    plt.title("Distribucion no uniforme")
    plt.pie(listPie,labels=nom,autopct="%0.1f %%")
    fig, ax = plt.subplots()
    ax.set_title("Distribucion no uniforme")
    ax.hist(listR)
    plt.show()
    opc = input("Quieres volver a girarlo ? \n")
    
    if opc == "no":
        flag = False