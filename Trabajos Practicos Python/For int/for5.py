""" print("Este programa pide dos número y muestra la lista de multiplos de 2, 3 y 5")

num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese un número: "))
mul2= 0
mul3= 0
mul5= 0

for multiplos2 in range (num1, num2 + 1):
    if multiplos2 % 2 == 0:
        print("Los multiplos de 2 son: ", multiplos2)
        mul2 += 1

for multiplos3 in range (num1, num2 + 1):
    if multiplos3 % 3 == 0:
        print("Los multiplos de 3 son: ", multiplos3)
        mul3 += 1

for multiplos5 in range(num1, num2 + 1):
    if multiplos5 % 5 == 0:
        print("Los multiplos de 5 son: ", multiplos5)
        mul5 += 1

print("Hay", mul2, "números multiplos de 2")
print("Hay", mul3, "números multiplos de 3")
print("Hay", mul5, "números multiplos de 5")
 """
""" Corrección """

print("Este programa pide dos número y muestra la lista de multiplos de 2, 3 y 5")

numeroMenor = int(input("Ingrese el numero mas chico "))
numeroMayor = int(input("Ingrese el numero mas grande "))

cantidadDeMultiplosDe2 = 0
cantidadDeMultiplosDe3 = 0
cantidadDeMultiplosDe5 = 0
multiplosDe2 = ""
multiplosDe3 = ""
multiplosDe5 = ""


for indice in range(numeroMenor, numeroMayor + 1):
  if(indice % 2 == 0):
    cantidadDeMultiplosDe2 += 1
    multiplosDe2 += str(indice) + " "

  if(indice % 3 == 0):
    cantidadDeMultiplosDe3 += 1
    multiplosDe3 += str(indice) + " "
  
  if (indice % 5 == 0):
    cantidadDeMultiplosDe5 += 1
    multiplosDe5 += str(indice) + " "

print("Hay ", cantidadDeMultiplosDe2, " multiplos de 2, y son: ", multiplosDe2)
print("Hay ", cantidadDeMultiplosDe3, " multiplos de 3, y son: ", multiplosDe3)
print("Hay ", cantidadDeMultiplosDe5, " multiplos de 5, y son: ", multiplosDe5)