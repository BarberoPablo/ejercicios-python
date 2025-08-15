print("Serie de Fibonacci: El usuario indica cuántos términos quiere ver. Mostrar esa cantidad de términos de la serie de Fibonacci (inicia en 0 y 1)")
""" 0 1 1 2 3 5 8 13 21 34 55 
    El numero siguiente es la suma de los dos anteriores
    | a -> b -> siguiente | Empezamos en a y vamos actualizando los valores de las variables
    Primera iteracion:
    a = 0, b = 1, siguiente = 1
    Segunda iteracion:
    a = 1, b = 1, siguiente = 2
    Tercera iteracion:
    a = 1, b = 2, siguiente = 3
    Cuarta iteracion:
    a = 2, b = 3, siguiente = 5
"""
terminos = int(input("Cuántos términos quiere ver?: "))

a = 0
b = 1

for i in range(terminos):
  print(str(a) + " ")  # mostramos el término actual
  # Calculamos el siguiente término
  siguiente = a + b
  a = b
  b = siguiente

""" 
1)  a y b guardan los dos últimos números de la serie.
2)  En cada iteración:
      - Mostramos a (el número actual).
      - Calculamos el siguiente número (a + b).
      - Actualizamos a y b para la próxima vuelta.  
"""
