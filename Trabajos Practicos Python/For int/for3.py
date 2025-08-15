print("Este programa muestra los números impares que hay entre dos números")

num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese un número: "))

for numero in range(num1, num2 + 1):
    if numero % 2 != 0:
        print(numero)

""" Correccion """

print("Impares entre dos números: Pedir dos números al usuario y mostrar los números impares que hay entre ellos, inclusive si corresponde.")

primerNumero = int(input("Ingrese el numero mas chico: "))
segundoNumero = int(input("Ingrese el numero mas grande: "))

''' Opcional hacer un print antes del for:
print("Los numeros impares entre ", primerNumero, " y ", segundoNumero, "son: ") 
'''
for indice in range(primerNumero, segundoNumero + 1):
  if indice % 2 != 0:
    print(indice)
