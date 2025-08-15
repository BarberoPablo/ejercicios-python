# Ejercicio 7: Contar mayúsculas y minúsculas

frase = input("Ingrese una frase: ")

mayusculas = 0
minusculas = 0

for caracter in frase:
    if 'A' <= caracter <= 'Z':
        mayusculas += 1
    elif 'a' <= caracter <= 'z':
        minusculas += 1

print("Cantidad de mayúsculas:", mayusculas)
print("Cantidad de minúsculas:", minusculas)

if mayusculas > minusculas:
    print("Hay más mayúsculas que minúsculas")
elif minusculas > mayusculas:
    print("Hay más minúsculas que mayúsculas")
else:
    print("Hay la misma cantidad de mayúsculas y minúsculas")