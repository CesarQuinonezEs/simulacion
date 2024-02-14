import dados
import dosDados
import moneda
import os
f = True
while(f):
   opc =  int(input("Elije una opcion: \n1) Moneda \n2) Dados\n3) Dos dados \n4) Salir \n"))
   os.system('cls')
   if opc == 1:
      moneda.moneda()
   elif opc == 2:
      dados.dados()
   elif opc == 3:
      dosDados.dosDados()
   elif opc == 4:
      f = False 
   else:
      print("Opcion no encontrada")
