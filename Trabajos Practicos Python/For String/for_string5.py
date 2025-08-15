# Ejercicio 5: Invertir una frase

frase = input("Ingrese una frase: ")

frase_invertida = ""

for caracter in frase:
  frase_invertida = caracter + frase_invertida

print("Frase invertida:", frase_invertida)