print("Cálculo de N números. Pedir al usuario cuántos números quiere ingresar. Luego pedir estos números uno por uno y mostrar cual es el promedio, cual es el menor y cuál es el mayor. ")
""" PASOS A REALIZAR: """
''' Pedir al usuario cuántos números quiere ingresar. '''
''' Pedir estos números uno por uno '''
''' Mostrar cual es el promedio, cual es el menor y cuál es el mayor. '''

""" Con None """

total = 0
menor = None
mayor = None

cantidadDeNumeros = int(input("Cuantos numeros va a ingresar?: "))

for indiceIncremental in range(1, cantidadDeNumeros + 1):
  num = int(input("Ingrese uno de sus números: "))
  total += num

  if mayor is None or num > mayor:
    mayor = num
  if menor is None or num < menor:
    menor = num

print("El promedio es ", total / cantidadDeNumeros)
print("El mayor es ", mayor)
print("El menor es ", menor)

""" Sin None """

print("Cálculo de N números. Pedir al usuario cuántos números quiere ingresar. Luego pedir estos números uno por uno y mostrar cual es el promedio, cual es el menor y cuál es el mayor. ")

total = 0
menor = 0
mayor = 0

''' Pedir al usuario cuántos números quiere ingresar. '''
cantidadDeNumeros = int(input("Cuantos numeros va a ingresar?: "))

''' Pedir estos números uno por uno '''
''' Mostrar cual es el promedio, cual es el menor y cuál es el mayor. '''
for indiceIncremental in range(1, cantidadDeNumeros + 1):
  num = int(input("Ingrese uno de sus numeros"))
  
  if indiceIncremental == 1:
    mayor = num
    menor = num
    total = num
  else:
    total += num
    if num < menor:
      menor = num
    if num > mayor:
      mayor = num

print("El promedio es ", total / cantidadDeNumeros)
print("El mayor es ", mayor)
print("El menor es ", menor)
