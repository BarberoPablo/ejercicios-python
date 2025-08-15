""" 
* Cuando usamos for con un string, el bucle recorre cada carácter de ese string.
palabra = "hola"
for letra in palabra:
    print(letra)

  - palabra tiene los caracteres 'h', 'o', 'l', 'a'.
  - El bucle for toma cada carácter uno por uno.
  - letra representa el carácter actual en cada vuelta del bucle.

* Cuando “sumamos” strings en Python, no se hace una suma matemática, sino concatenación, es decir, juntar texto.
  - "Hola " + "mundo" = "Hola mundo"
  - "Hola" + 5 = Error

Para “sumar” un string con un número, hay que convertir el número a string:
  - "Hola" + str(5) = "Hola5"

"""

# Ejercicio 1: Contar una letra específica

frase = input("Ingrese una frase")
letra = input("Ingrese una letra")

cantidad = 0

for caracter in frase:
  if(caracter == letra):
    cantidad += 1

print("La letra ", letra, " aparece ", cantidad, " veces")

""" 
Explicación:
1) Pedimos los datos al usuario:
  frase → la frase completa que quiere analizar.
  letra → la letra que queremos contar.
2) Inicializamos un contador:
  contador = 0 → empieza en cero porque aún no encontramos la letra.
3) Recorremos la frase con un for:
  for caracter in frase: → toma cada carácter de la frase uno por uno.
  Comparamos if caracter == letra: → si el carácter coincide con la letra buscada, aumentamos el contador.
4) Imprimimos el resultado:
  "La letra '" + letra + "' aparece", contador, "veces" → mostramos cuántas veces apareció la letra.
"""