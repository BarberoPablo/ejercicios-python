print("Evaluar si un numero es primo o no.")

numero = int(input("Ingrese su numero: "))

if numero <= 1:
  print("El numero no es primo")
else:
  esPrimo = True
  for indice in range(2, numero):
    if(numero % indice == 0):
      esPrimo = False
      break

  if esPrimo:
    print("El numero ingresado es primo")
  else:
    print("El numero ingresado no es primo")

""" 
1) Primero verificamos si el número es menor o igual a 1 → automáticamente no es primo.
2) Creamos una variable esPrimo que empieza en True.
3) Probamos todos los números desde 2 hasta uno antes del número del usuario (variable numero).
4) Si encontramos que alguno lo divide exacto (numero % i == 0), entonces no es primo y salimos del bucle con break.
5) Al final mostramos si es o no primo según el valor de esPrimo.

Otra manera de hacerlo más eficiente es hacer el bucle (for) desde 2 hasta:  limite = int(math.sqrt(numero)) + 1  (hasta raíz cuadrada)
Ejemplo, los divisores de 36 son:1 x 36  
2 x 18  
3 x 12  
4 x 9  
6 x 6  
9 x 4  
12 x 3  
18 x 2  
36 x 1

Después de 6 x 6 los divisores se repiten en orden inverso.
- 2 y 18 → ya aparecieron
- 3 y 12 → ya aparecieron
- 4 y 9 → ya aparecieron

Esto pasa porque si un número tiene un divisor mayor que su raíz cuadrada, necesariamente el otro divisor es menor que su raíz cuadrada.

"""

