# if letra in "aeiou":  No se puede usar según el enunciado.
# si necesitamos convertir de mayusculas a minusculas:

# if 'A' <= caracter <= 'Z':
#   caracter = chr(ord(caracter) + 32)  

# Ejercicio 2: ¿Vocales o consonantes?

frase = input("Ingrese una frase: ")

vocales = 0
consonantes = 0

for caracter in frase:
  if 'a' <= caracter <= 'z':
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
      vocales += 1
    else:
      consonantes +=1

print("Vocales:", vocales)
print("Consonantes:", consonantes)

if vocales > consonantes:
    print("Hay más vocales que consonantes")
elif consonantes > vocales:
    print("Hay más consonantes que vocales")
else:
    print("Hay empate entre vocales y consonantes")
