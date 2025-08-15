# Ejercicio 8: Mostrar solo las vocales

frase = input("Ingrese una frase: ")

solo_vocales = ""

for caracter in frase:
    if (caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u' 
        or caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U'):
        solo_vocales += caracter

print("Frase solo con vocales:", solo_vocales)