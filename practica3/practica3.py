from congrucialMixto import GPCM


flag = True

x0 = int(input("Ingrese la semilla "))
a = int(input("Ingrese el multiplicador (a) "))
c = int(input("Ingrese la constante aditiva (c) "))
m = int(input("Ingrese el modulo "))


while flag:
    gpcm = GPCM(a=a,semilla=x0,c=c,m=m)
    n = int(input("Ingrese el periodo "))
    print("Iteracion\t resultado\n")
    for i in range(n):
        
        print(i,"\t\t\t",gpcm.generate(),"\n")
    opc = input("Quiere volver a ingresar ? ")
    if opc == "no":
        flag = False