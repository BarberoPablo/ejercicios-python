print("Este programa pide un número entero y muestra todos sus divisores")

num= int(input("Ingrese un número: "))

for numero in range (num + 2):
    if numero % 2 == 0:
        print(numero)

""" Correccion """
print("Divisores: Pedir un número entero y mostrar todos los números que lo dividen.")

numeroSeleccionado = int(input("Ingrese un número: "))

for numeroIncremental in range (1, numeroSeleccionado + 1):
    if numeroSeleccionado % numeroIncremental == 0:
        print(numeroIncremental)