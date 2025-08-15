# Ejercicio 4: Contar palabras
# Asumiendo que:
# 1) La frase no empieza con espacios
# 2) Las palabras están separadas por un solo espacio

frase = input("Ingrese una frase: ")

contador = 1

dentro_palabra = False

for caracter in frase:
  if caracter == " ":
    contador += 1  

print("Cantidad de palabras:", contador)
