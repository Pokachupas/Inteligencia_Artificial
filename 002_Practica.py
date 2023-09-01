## Practica 2 ##
##Esta practica abarca del capitulo 7 hasta el capitulo 9 ##

class Calculadora:
   operandos = []

   def Suma(self):
      sumaTotaL = 0
      x = 1
      while(x):
         x = input("Ingrese un numero a sumar o 0 para salir")
         if x != 0:
            operandos.append(x)
      #for number in range operandos:
      #  sumaTotal += number
      sumaTotal = sum(operandos)
      print("La suma es: " + sumaTotal)
   
         
