# Ejercicio 9: ¿La frase es capicúa?

frase = input("Ingrese una frase: ")
frase_limpia = ""
frase_invertida = ""

for caracter in frase:
    # Solo agregamos letras (ignoramos espacios y signos)
    if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z'):
        # Convertimos mayúsculas a minúsculas
        if 'A' <= caracter <= 'Z':
            caracter = chr(ord(caracter) + 32)  # 'A'->'a', 'B'->'b', etc.
        frase_limpia = frase_limpia + caracter
        frase_invertida = caracter + frase_invertida

if frase_limpia == frase_invertida:
    print("La frase es capicúa")
else:
    print("La frase no es capicúa")


""" 
Manera sencilla de hacerlo pero no tan eficiente:

frase = input("Ingrese una frase: ")

frase_invertida = ""
es_capicua = False

for caracter in frase:
    frase_invertida = caracter + frase_invertida

if frase == frase_invertida:
    es_capicua = True

print("La frase es capicuada:", es_capicua)
"""