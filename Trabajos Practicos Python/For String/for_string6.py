# Ejercicio 6: Reemplazar una letra por otra

frase = input("Ingrese una frase: ")
letra_vieja = input("Ingrese la letra vieja: ")
letra_nueva = input("Ingrese la letra nueva: ")

nueva_frase = ""

for caracter in frase:
  if caracter == letra_vieja:
    nueva_frase += letra_nueva
  else:
    nueva_frase += caracter

print("Frase con reemplazo:", nueva_frase)
