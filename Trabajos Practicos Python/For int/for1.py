""" 
* Cuando usamos for con un número, normalmente lo hacemos usando range().
  range(5) genera los números 0, 1, 2, 3, 4.
  El bucle for recorre cada número en ese rango.
  i toma el valor de cada número en cada vuelta del bucle

* Cuando sumamos números en Python, el resultado es matemático, se hace la operación aritmética normal.
"""

""" for i in range (10):
    print(i + 1)
print("Fin") """

""" Correccion """

print("Tabla de multiplicar: Pedir al usuario un número y mostrar su tabla de multiplicar del 1 al 10.")

numero = int(input("Ingrese su numero "))

for indice in range(1, 11):
  print("indice * numero = ", indice * numero)